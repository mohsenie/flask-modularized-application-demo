import module_loader.events
import module_loader.base_module
import module_event.event_registry
from flask import Blueprint


class UserView(module_loader.base_module.BaseWebViewModule):
    def __init__(self):
        self.description = 'user view module'
        self.events = module_loader.events.get_events()
        super(UserView, self).__init__(__file__)
        self.subscribed_events = []

    def register_view(self, app):
        controller = Blueprint('greeting_controller', __name__, url_prefix='/user1',
                               template_folder=self.get_template_path())

        @controller.route('/hello')
        def hello():
            """Renders the page"""
            # we now trigger an event
            self.events.trigger_event(payload='triggered from hello method of user view module',
                                      event_name=module_event.event_registry.EventNames.on_log_to_file.value)

            return self.render_page_from(app, controller.name, 'user.html', title='hello')

        app.register_blueprint(controller)
