from nami.registry import MODELS
from .configuration_bert import NamiBertConfig
from ..utils import HFModel


@MODELS.register_module()
class NamiBertForSequenceClassification(HFModel):
    config_class = NamiBertConfig

    def forward(
            self,
            input_ids=None,
            attention_mask=None,
            token_type_ids=None,
            position_ids=None,
            head_mask=None,
            inputs_embeds=None,
            labels=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None,
            mode: str = 'pred', **kwargs):

        output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            labels=None,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict
        )
        if mode == 'train':
            loss = self.loss(output.logits, kwargs['sample_idx'])
            return dict(loss=loss)
        elif mode == 'eval':
            return output.logits,
        else:
            return output
