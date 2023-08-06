import sys

import click

from .config import get_config_dict, get_used_settings_message, parse_config_dict
from .generators.package import PackageGenerator
from .plugins.explorer import get_plugins_types
from .plugins.manager import PluginManager
from .schema import (
    filter_fragments_definitions,
    filter_operations_definitions,
    get_graphql_queries,
    get_graphql_schema_from_path,
    get_graphql_schema_from_url,
)


@click.command()
@click.version_option()
@click.option("--config", default=None, help="Path to custom configuration file.")
def main(config=None):
    config_dict = get_config_dict(config)
    settings = parse_config_dict(config_dict)
    if settings.schema_path:
        schema = get_graphql_schema_from_path(settings.schema_path)
        schema_source = settings.schema_path
    else:
        schema = get_graphql_schema_from_url(
            url=settings.remote_schema_url, headers=settings.remote_schema_headers
        )
        schema_source = settings.remote_schema_url

    definitions = get_graphql_queries(settings.queries_path)
    queries = filter_operations_definitions(definitions)
    fragments = filter_fragments_definitions(definitions)

    sys.stdout.write(get_used_settings_message(settings))

    package_generator = PackageGenerator(
        package_name=settings.target_package_name,
        target_path=settings.target_package_path,
        schema=schema,
        client_name=settings.client_name,
        client_file_name=settings.client_file_name,
        base_client_name=settings.base_client_name,
        base_client_file_path=settings.base_client_file_path,
        input_types_module_name=settings.input_types_module_name,
        queries_source=settings.queries_path,
        schema_source=schema_source,
        include_comments=settings.include_comments,
        fragments=fragments,
        convert_to_snake_case=settings.convert_to_snake_case,
        async_client=settings.async_client,
        files_to_include=settings.files_to_include,
        custom_scalars=settings.scalars,
        plugin_manager=PluginManager(
            schema=schema,
            config_dict=config_dict,
            plugins_types=get_plugins_types(settings.plugins),
        ),
    )
    for query in queries:
        package_generator.add_operation(query)
    generated_files = package_generator.generate()

    sys.stdout.write("\nGenerated files:\n  " + "\n  ".join(generated_files) + "\n")


if __name__ == "__main__":
    main()
