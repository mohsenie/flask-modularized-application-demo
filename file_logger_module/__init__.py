import module_loader.events
import module_loader.base_module
import module_event


class FileLogger(module_loader.base_module.BaseModule):
    def __init__(self):
        self.description = 'file logger module'
        self.events = module_loader.events.get_events()
        super(FileLogger, self).__init__()

    def event_triggered(self, event_name=None, event=None):
        print('event_triggered captured by file logger :' + str(event))
        print('writing a log file')

        with open("C:\\Users\\mohsen\Downloads\\request_logs.txt", "a") as myfile:
            myfile.write(event_name + ' ' + str(event) + '\n')

        # capture that event and trigger another one
        self.events.trigger_event(self, 'triggering print to condole event from file logger',
                                  module_event.event_registry.EventNames.on_print_to_console.value)
