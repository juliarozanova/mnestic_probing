import os 
import sys

DIR_PATH = os.path.dirname(__file__)
HOME_PATH = os.path.join(DIR_PATH, '../')
AMNESIC_PATH = os.path.join(HOME_PATH, '../amnesic_probing/')
MODEL_NAMES = [
        'infobert',
        'roberta-large-mnli', 
        'roberta-large-mnli-help', 
        'roberta-large-mnli-double-finetuning',
        'bert-base-uncased-snli-help', 
        'bert-base-uncased-snli',
    ]

sys.path.append(AMNESIC_PATH)

def two_class_relabel(two_class_label):
    if two_class_label in [1, '1']:
        out_label = 'entailment'
    elif two_class_label in [0, '0']:
        out_label = 'non-entailment'
    elif two_class_label in [2, '2']:
        out_label = 'non-entailment'
    else:
        raise ValueError(f'Unexpected two class label: {two_class_label} of type {type(two_class_label)}')
    return out_label


# def three_class_relabel(three_class_label):
#     if three_class_label in [2, '2']:
#         out_label = 'entailment'
#     elif three_class_label in [0, '0', 1, '1']:
#         out_label = 'non-entailment'
#     return out_label

def three_class_relabel_2_is_entailment(three_class_label):
    if three_class_label in [2, '2']:
        out_label = 'entailment'
    elif three_class_label in [0, '0', 1, '1']:
        out_label = 'non-entailment'
    return out_label

def three_class_relabel_1_is_entailment(three_class_label):
    if three_class_label in [1, '1']:
        out_label = 'entailment'
    elif three_class_label in [0, '0', 2, '2']:
        out_label = 'non-entailment'
    return out_label

model_label_mapper = {
    'roberta-large-mnli': three_class_relabel_2_is_entailment,
    'roberta-large-mnli-help': two_class_relabel,
    'roberta-large-mnli-double-finetuning': two_class_relabel,
    'bert-base-uncased-snli': three_class_relabel_1_is_entailment,
    'bert-base-uncased-snli-help': two_class_relabel, 
    'infobert': three_class_relabel_2_is_entailment
}

model_pretrained_paths = {
    'roberta-large-mnli': 'roberta-large-mnli',
    'roberta-large-mnli-help':  './models/roberta-large-mnli-help', 
    'roberta-large-mnli-double-finetuning':  './models/roberta-large-mnli-double_finetuning', 
    'facebook-bart-large-mnli': 'facebook/bart-large-mnli', 
    'facebook-bart-large-mnli-help': './models/facebook-bart-large-mnli-help',
    'bert-base-uncased-snli': 'textattack/bert-base-uncased-snli',
    'bert-base-uncased-snli-help': './models/bert-base-uncased-snli-help',
    'infobert': './models/infobert-checkpoint'
}

