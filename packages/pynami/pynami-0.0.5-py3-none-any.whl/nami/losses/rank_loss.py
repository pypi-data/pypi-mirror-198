import torch
import torch.nn as nn
import torch.nn.functional as F

from nami.registry import MODELS


@MODELS.register_module()
class RankLoss(nn.Module):
    def __init__(self):
        super(RankLoss, self).__init__()

    def forward(self,
                cls_score,
                sample_idx,
                **kwargs):
        losses = torch.FloatTensor([0]).to(cls_score.device)
        count = 0
        for i in range(cls_score.shape[0] - 1):
            for j in range(i + 1, cls_score.shape[0]):
                if sample_idx[i] != sample_idx[j]:
                    continue
                loss = -1 * F.logsigmoid(cls_score[i] - cls_score[j])
                losses += loss
                count += 1
        loss = losses / count
        return loss
