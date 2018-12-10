import module_loader.events
import module_loader.base_module
import module_event.event_registry


class ConsoleLogger(module_loader.base_module.BaseModule):
    def __init__(self):
        self.description = 'console logger module'
        self.events = module_loader.events.get_events()
        super(ConsoleLogger, self).__init__()
        self.subscribed_events = [module_event.event_registry.EventNames.on_print_to_console.value]

    def event_triggered(self, event_name=None, event=None):
        print(event_name + ' event triggered by file logger and captured by console logger :' + str(event))
