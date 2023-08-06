import ckan.plugins as plugins

from ckan.model import Session

from flask import Blueprint

from ckanext.datapackage_creator.controllers import datapackage_creator
from ckanext.datapackage_creator.converter import ckan_resource_to_frictionless, extract_resource_metadata
from ckanext.datapackage_creator.logic import (
    save_datapackage, inference_data, save_datapackage_resource, datapackage_show,
    datapackage_resource_show, generate_datapackage_json
)
from ckanext.datapackage_creator.cli import get_commands


class DatapackageCreatorPlugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IClick)
    plugins.implements(plugins.IResourceController)

    def get_blueprint(self):
        blueprint = Blueprint('datapackage_creator', __name__, url_prefix='/datapackage-creator')
        blueprint.add_url_rule(
            "/inference", view_func=datapackage_creator.inference,
            endpoint='inference', methods=['POST']
        )
        blueprint.add_url_rule(
            "/save-resource", view_func=datapackage_creator.save_resource,
            endpoint='save_resource', methods=['POST']
        )
        blueprint.add_url_rule(
            "/delete-resource/<resource_id>", view_func=datapackage_creator.delete_resource,
            endpoint='delete_resource', methods=['DELETE']
        )
        blueprint.add_url_rule(
            "/save-package", view_func=datapackage_creator.save_package,
            endpoint='save_package', methods=['POST']
        )
        blueprint.add_url_rule(
            "/publish-package", view_func=datapackage_creator.publish_package,
            endpoint='publish_package', methods=['POST']
        )
        blueprint.add_url_rule(
            "/show-datapackage/<package_id>", view_func=datapackage_creator.datapackage_show,
            endpoint='datapackage_show', methods=['GET']
        )
        blueprint.add_url_rule(
            "/show-datapackage-resource/<resource_id>", view_func=datapackage_creator.datapackage_resource_show,
            endpoint='datapackage_resource_show', methods=['GET']
        )
        blueprint.add_url_rule(
            "/show-datapackage-json/<package_id>", view_func=datapackage_creator.datapackage_json_show,
            endpoint='datapackage_json_show', methods=['GET']
        )
        blueprint.add_url_rule(
            "/show-validation/<package_id>", view_func=datapackage_creator.datapackage_validation_show,
            endpoint='datapackage_validation_show', methods=['GET']
        )
        blueprint.add_url_rule(
            "/show-diagram/<package_id>", view_func=datapackage_creator.entity_diagram_show,
            endpoint='datapackage_entity_diagram_show', methods=['GET']
        )
        blueprint.add_url_rule(
            "/download-resources/<package_id>", view_func=datapackage_creator.download_resources,
            endpoint='datapackage_download_resources', methods=['GET']
        )
        blueprint.add_url_rule(
            "/show-settings", view_func=datapackage_creator.settings_show,
            endpoint='settings_show', methods=['GET']
        )
        return blueprint
    
    def before_resource_create(self, context, resource) -> None:
        pass

    def after_resource_create(self, context, resource) -> None:
        pass

    def before_resource_update(self, context, current, resource) -> None:
        pass

    def after_resource_update(self, context, resource) -> None:
        pass

    def before_resource_delete(self, context, resource, resources) -> None:
        pass

    def after_resource_delete(self, context, resources) -> None:
        pass

    def before_resource_show(self, resource_dict):
        resource_dict['tableschema'] = extract_resource_metadata(resource_dict)
        return resource_dict

    def update_config(self, config):
        plugins.toolkit.add_public_directory(config, 'public')
        plugins.toolkit.add_template_directory(config, 'templates')

    def get_actions(self):
        return {
            'save_datapackage': save_datapackage,
            'save_datapackage_resource': save_datapackage_resource,
            'inference_data': inference_data,
            'datapackage_show': datapackage_show,
            'datapackage_resource_show': datapackage_resource_show,
            'generate_datapackage_json': generate_datapackage_json,
        }

    def get_commands(self):
        return get_commands()
