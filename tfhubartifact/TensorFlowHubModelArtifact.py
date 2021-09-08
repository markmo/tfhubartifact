import os

import tensorflow as tf
import tensorflow_hub as hub
from bentoml.exceptions import (
    InvalidArgument,
)
from bentoml.service import BentoServiceArtifact


class TensorFlowHubModelArtifact(BentoServiceArtifact):
    """Abstraction for saving/loading TensorFlow Hub models

    Args:
        name (string): name of the artifact

    Raises:
        MissingDependencyException

        InvalidArgument: invalid argument type, model being packed must be 
            a dictionary of format
            {
                'model': <hub model object>,
            }
            or a directory path where the model is saved.

        NotFound: if the provided model name or model path is not found

    """
    def __init__(self, name):
        super(TensorFlowHubModelArtifact, self).__init__(name)
        self._model = None

    def _file_path(self, base_path):
        return os.path.join(base_path, self.name)

    def _load_from_directory(self, path):
        self._model = hub.load(path)

    def _load_from_dict(self, model):
        if 'embedder' not in model:
            raise InvalidArgument(
                "'embedder' key is not found in the dictionary. "
                "Expecting a dictionary with keys 'model', 'tokenizer' and 'embedder'"
            )
        self._model = model['embedder']

    def pack(self, model, opts=None, update=False):
        if isinstance(model, str):
            if os.path.isdir(model):
                self._load_from_directory(model)
            else:
                raise InvalidArgument('model should be the path name of a directory')
        elif isinstance(model, dict):
            self._load_from_dict(model)
        else:
            raise InvalidArgument(
                "Expecting a pretrained model path or dictionary of format "
                "{'embedder': <model object>}"
            )

        return self

    def load(self, path):
        path = self._file_path(path)
        return self.pack(path)

    def save(self, dst):
        path = self._file_path(dst)
        os.makedirs(path, exist_ok=True)
        tf.saved_model.save(self._model, path)
        return path

    def get(self):
        return self._model
