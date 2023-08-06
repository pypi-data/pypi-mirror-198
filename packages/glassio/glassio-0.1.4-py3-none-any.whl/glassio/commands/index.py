import os
import importlib
import inspect
from typing import Dict, Type
from glassio import ctx
from glassio.uorm.models.storable_model import StorableModel
from glassio.uorm.models.counter import Counter
from ..command import Command


class Index(Command):

    NAME = "index"
    HELP = "Create indexes for the application models"

    async def run_async(self) -> None:
        app_dir = ctx.project_dir
        models_dir = os.path.join(app_dir, "models")
        app_module = app_dir.split("/")[-1]
        classes: Dict[str, Type['StorableModel']] = {
            "counter": Counter
        }

        for filename in os.listdir(models_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                modulename = filename[:-3]
                module = importlib.import_module(f"{app_module}.models.{modulename}")

                for attr in dir(module):
                    cls = getattr(module, attr)
                    if inspect.isclass(cls) and issubclass(cls, StorableModel) and not cls is StorableModel:
                        classes[cls.__name__] = cls

        for cls_name, cls in classes.items():
            ctx.log.debug(f"Creating index for model {cls_name}")
            await cls.ensure_indexes(loud=True)
