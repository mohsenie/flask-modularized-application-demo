import module_loader
import module_loader.base_module
import module_registry
import module_event.event_registry
from events import Events


class MyEvents(Events):
    __events__ = (
        module_event.event_registry.EventNames.on_log_to_file.value,
        module_event.event_registry.EventNames.on_print_to_console.value)


class Dispatcher(object):
    def __init__(self, event_name):
        self.event_name = event_name

    def get_dispatch_function(self, event=None):
        # attach triggers to modules
        for module in module_registry.Modules:
            module_instance = module_loader.RequiredFeature(
                module.value.module_name.value,
                module_loader.has_methods('event_triggered', 'get_subscribed_events')).request()

            # checking if module has subscribed to this event or not
            if self.event_name not in module_instance.get_subscribed_events():
                continue

            assert isinstance(module_instance, module_loader.base_module.BaseModule), "Module must extend 'BaseModule'"

            # does not propagate event to the event originator
            if isinstance(event, tuple):
                if module_instance.__class__ != event[0].__class__:
                    module_instance.event_triggered(event_name=self.event_name, event=event[1])
            else:
                module_instance.event_triggered(event_name=self.event_name, event=event)


class AllEvents(object):
    def __init__(self):
        self.description = 'events module'
        self.events = MyEvents()

        # Attaching dispatch handler for all events
        for event_name in module_event.event_registry.EventNames:
            getattr(self.events, event_name.value).targets.append(Dispatcher(event_name.value).get_dispatch_function)

        super(AllEvents, self).__init__()

    def trigger_event(self, event_originator=None, payload=None, event_name=None):
        assert event_name, "Event name is empty"
        assert payload, 'Event payload is empty'
        assert event_name in [ev.value for ev in module_event.event_registry.EventNames], 'Event name not valid'

        # add the originator only if instance of BaseModule
        # (needed to stop recursion since we only dispatch events to modules)
        if event_originator and isinstance(event_originator, module_loader.base_module.BaseModule):
            getattr(self.events, event_name)((event_originator, payload))
        else:
            getattr(self.events, event_name)(payload)
