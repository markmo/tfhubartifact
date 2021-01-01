# tfhubartifact

BentoML artifact framework for TensorFlow Hub models.

Installation:

    pip install tfhubartifact==0.0.1

Usage example (decorate service):

    from tfhubartifact.TensorFlowHubModelArtifact import TensorFlowHubModelArtifact

    @artifacts([TensorFlowHubModelArtifact('embedder')])
    class MyBentoService(BentoService):


Usage example (package model):

    svc = MyBentoService()

    svc.pack('embedder', my_embedding_model_path)

Alternatively, during training:

    svc.pack('embedder', {'embedder': my_embedder})
