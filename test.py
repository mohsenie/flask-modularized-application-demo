import module_loader.events
import module_event

events_module = module_loader.events.get_events()

events_module.trigger_event(payload='ffff', event_name=module_event.event_registry.EventNames.on_log_to_file.value)
