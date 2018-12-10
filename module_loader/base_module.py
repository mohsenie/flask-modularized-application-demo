import os
import module_event.event_registry
from flask import render_template


class BaseModule(object):
    def __init__(self):
        self.description = 'module_loader'
        # by default subscribe to all events
        self.subscribed_events = [evt.value for evt in module_event.event_registry.EventNames]

    def event_triggered(self, event_name=None, event=None):
        pass

    def get_subscribed_events(self):
        return self.subscribed_events


class BaseWebViewModule(BaseModule):
    def __init__(self, filename=__file__):
        self.filename = filename
        super(BaseWebViewModule, self).__init__()

    def register_view(self, app):
        pass

    def get_template_path(self):
        return os.path.join(os.path.dirname(os.path.abspath(self.filename)), 'html_templates')

    def render_page_from(self, app, controller_name, template_name_or_list, **context):
        # here you can choose any controller or use default
        app.jinja_loader.searchpath.clear()
        blueprint = app.blueprints[controller_name]
        app.jinja_loader.searchpath.append(blueprint.template_folder)
        return render_template(template_name_or_list, context=context)
