# Mnestic Probing: Interventional Probing in High Dimensions

# Introduction

# Reproducing Experiments

This project depends on the [amnesic probing]() repository. Clone it and change
``` AMNESIC_PATH = {YOUR PATH HERE}```
in experiments/constants.py

## Download Models and Encode Data
Download models at this online [model folder](sdfsds.gm)

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