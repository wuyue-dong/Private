
import digital_machine
import digital_machine.templates as tmpl
from digital_machine import dmCompile

from .company import company
from .plant import plant
from .shebei import shebei


try:
    from ._legacy import models as legacy_models
except ModuleNotFoundError:
    legacy_models = {}

py_model_collection = tmpl.PyModelCollection()



company().generate_model(digital_machine.digital_twin_model("xiaofanggui", "company"), py_model_collection)
plant().generate_model(digital_machine.digital_twin_model("xiaofanggui", "plant"), py_model_collection)
shebei().generate_model(digital_machine.digital_twin_model("xiaofanggui", "shebei"), py_model_collection)


models = py_model_collection.models
models.update(legacy_models)
