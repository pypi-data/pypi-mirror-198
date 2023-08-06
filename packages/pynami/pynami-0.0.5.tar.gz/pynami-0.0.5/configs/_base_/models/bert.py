transformers_pretrained_model_dir = 'bert-base-chinese'

model = dict(
    type='NamiBertForSequenceClassification',
    bert=dict(
        type='NamiAutoModel',
        model_type='BertForSequenceClassification',
        config_type='BertConfig',
        num_labels=1,
        config_pretrained=transformers_pretrained_model_dir,
        model_pretrained=transformers_pretrained_model_dir,
    ),
    loss=dict(type='RankLoss'),
)
