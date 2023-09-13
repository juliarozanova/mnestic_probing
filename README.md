# Mnestic Probing: Interventional Probing in High Dimensions

# Introduction
This is the research code repository for the paper [Interventional Probing in High Dimensions: An NLI Case Study](https://aclanthology.org/2023.findings-eacl.188/).

```
@inproceedings{rozanova-etal-2023-interventional,
    title = "Interventional Probing in High Dimensions: An {NLI} Case Study",
    author = "Rozanova, Julia  and
      Valentino, Marco  and
      Cordeiro, Lucas  and
      Freitas, Andr{\'e}",
    booktitle = "Findings of the Association for Computational Linguistics: EACL 2023",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-eacl.188",
    pages = "2489--2500",
    abstract = "Probing strategies have been shown to detectthe presence of various linguistic features inlarge language models; in particular, seman-tic features intermediate to the {``}natural logic{''}fragment of the Natural Language Inferencetask (NLI). In the case of natural logic, the rela-tion between the intermediate features and theentailment label is explicitly known: as such,this provides a ripe setting for interventionalstudies on the NLI models{'} representations, al-lowing for stronger causal conjectures and adeeper critical analysis of interventional prob-ing methods. In this work, we carry out newand existing representation-level interventionsto investigate the effect of these semantic fea-tures on NLI classification: we perform am-nesic probing (which removes features as di-rected by learned linear probes) and introducethe mnestic probing variation (which forgetsall dimensions except the probe-selected ones).Furthermore, we delve into the limitations ofthese methods and outline some pitfalls havebeen obscuring the effectivity of interventionalprobing studies.",
}

```
# Reproducing Experiments

This project depends on the [amnesic probing]() repository. Clone it and change
``` AMNESIC_PATH = {YOUR PATH HERE}```
in experiments/constants.py

## Download Models and Encode Data
The relevant models are in the huggingface transformers model hub.

To encode the data for the set of models in 'encode_configs.json':
```
python -m experiments.encode_nli_xy
```


## Mnestic and Amnesic Interventions
The intervention experiment consists of the following subsequent parts, which should be run in order.
When prompted, feel free to link to a WandB account for visualizations, or simply select the option "(3) Don't visualize my results".

To run the amnesic probing step (generating all projection matrices): 
```
python -m experiments.interventions.amnesic_probing
```

To run the representation intervention step:
```
python -m.experiments.intervene_project
```

To run the post-intervention evaluation:
```
python -m experiments.interventions.insert_predict
```


<!-- # Cite Us!
```python
``` -->
