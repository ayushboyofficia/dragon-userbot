import glob
import importlib.util
import os

def load_all_modules(app):
    for module in glob.glob("modules/*.py"):
        if module.endswith("__init__.py"):
            continue
        name = os.path.basename(module)[:-3]
        path = f"modules.{name}"
        imported = importlib.import_module(path)
        if hasattr(imported, "init"):
            imported.init(app)
