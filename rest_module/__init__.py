import module_loader.base_module
import module_registry
from flask import Flask

app = Flask(__name__)

# registering all views

for module in module_registry.WebViewModules:
    module_instance = module_loader.RequiredFeature(
        module.value.module_name.value,
        module_loader.has_methods(module.value.get_view_register_method.value)).request()
    module_instance.register_view(app)


if __name__ == "__main__":
    app.run()
