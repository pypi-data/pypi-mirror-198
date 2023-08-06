from nami.registry import COLLATE, TOKENIZERS


@COLLATE.register_module()
class RMCollate:
    def __init__(self, tokenizer, max_length=512, ignore_index=-100, **kwargs):
        self.tokenizer = TOKENIZERS.build(tokenizer)
        self.max_length = max_length
        self.ignore_index = ignore_index

    def _align(self, texts):
        tokens = self.tokenizer(texts, padding=True, truncation=True, max_length=self.max_length, return_tensors="pt")

        return tokens

    def __call__(self, data_batch):
        texts = []
        sample_idx = []

        for db in data_batch:
            text = db['text']
            answer = db['answer']
            idx = db['sample_idx']
            for ans in answer:
                texts.append(text+ans)
                sample_idx.append(idx)

        tokens = self._align(texts)
        tokens['sample_idx'] = sample_idx

        return tokens
