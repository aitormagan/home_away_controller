import importlib
import os


def import_class(module_name, cls):
    for submodule_name in filter(lambda x: "__" not in x, os.listdir(module_name)):
        submodule_name = '.'.join(submodule_name.split(".")[:-1])
        submodule = importlib.import_module(f"{module_name}.{submodule_name}")
        if cls in dir(submodule):
            return getattr(submodule, cls)

    raise StopIteration()
