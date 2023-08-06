from franky.hooks import Hook
from nami.registry import HOOKS


@HOOKS.register_module()
class ResizeTokenEmbeddingHook(Hook):
    priority = 'BELOW_NORMAL'

    def __init__(self, token_size: dict = None):
        self.token_size = token_size

    def before_run(self, runner) -> None:
        if self.token_size is not None:
            for module, size in self.token_size.items():
                obj = getattr(runner.model, module)
                obj.resize_token_embeddings(size)
