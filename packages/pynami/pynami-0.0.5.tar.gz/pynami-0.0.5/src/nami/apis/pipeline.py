from transformers import pipeline, AutoTokenizer

from nami import models  # noqa
from nami import pipelines  # noqa


class Pipeline:
    def __init__(self, task, model_dir, device=-1, batch_size=1, **kwargs):
        tokenizer = AutoTokenizer.from_pretrained(model_dir)

        self.pipe = pipeline(task, model=model_dir, tokenizer=tokenizer, device=device, batch_size=batch_size, **kwargs)

    def __call__(self, texts, **kwargs):
        return self.pipe(texts, **kwargs)
