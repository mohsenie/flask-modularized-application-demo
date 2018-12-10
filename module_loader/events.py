import module_loader
import module_registry


def get_events():
    return module_loader.RequiredFeature(
        module_registry.ModuleEvent.module_name.value,
        module_loader.has_methods(module_registry.ModuleEvent.get_trigger_event_method.value)).request()
