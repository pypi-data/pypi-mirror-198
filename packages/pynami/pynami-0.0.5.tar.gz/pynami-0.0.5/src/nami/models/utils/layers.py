import torch.nn as nn

from franky.model import BaseModule
from nami.registry import MODELS


@MODELS.register_module()
class LinearHead(BaseModule):
    def __init__(self,
                 num_classes,
                 in_channels,
                 dropout_prob=0.1,
                 init_cfg=dict(type='BasicNLP', layer='Linear'),
                 **kwargs):
        super(LinearHead, self).__init__(init_cfg=init_cfg)

        self.in_channels = in_channels
        self.num_classes = num_classes
        self.dropout = nn.Dropout(dropout_prob) if dropout_prob else nn.Identity()

        self.fc = nn.Linear(self.in_channels, self.num_classes)

    def forward(self, feats):
        output = self.dropout(feats)
        output = self.fc(output)

        return output
