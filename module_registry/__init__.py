from enum import Enum
import module_event
import file_logger_module
import console_logger_module
import user_view_module


######################################################################################
# this is used for registering the event handler module itself
######################################################################################
class ModuleEvent(Enum):
    module_name = 'module_event'
    module_class = module_event.AllEvents
    get_trigger_event_method = 'trigger_event'


######################################################################################
# all none web modules should be listed here
######################################################################################
class Modules(Enum):
    class FileLoggerModule(Enum):
        module_name = 'file_logger_module'
        module_class = file_logger_module.FileLogger

    class ConsoleLoggerModule(Enum):
        module_name = 'console_logger_module'
        module_class = console_logger_module.ConsoleLogger


#####################################################################################
# ass web view modules
#####################################################################################
class WebViewModules(Enum):

    class UserViewModule(Enum):
        module_name = 'user_view_module'
        module_class = user_view_module.UserView
        get_view_register_method = 'register_view'
