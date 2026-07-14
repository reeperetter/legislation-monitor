import importlib
import pkgutil


def load_parsers():

    package = __name__

    for _, module_name, _ in pkgutil.iter_modules(__path__):

        if module_name.startswith("_"):
            continue

        if module_name == "base":
            continue

        importlib.import_module(f"{package}.{module_name}")
