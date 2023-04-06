from pathlib import Path
# import wandb

# # for a single model: 

# # Part 1: P0...Pn(X)

# ## run probing: save projection matrices and basis vectors 

# ## create/load debiased reps

# ## create/load random removal reps

# ## Predict task metrics 

# label_column = 'insertion_rel'
# token_choice = 'CLS'
# classification_type = label_column
# layer = 'last'

# wandb.init(
#     name=f'nli_xy_{model}_{rep_name}',
#     project=f"amnesic_{label_column}_{token_choice}",
#     tags=["nli_xy", classification_type],
#     config=config,
#     reinit=True
# )

# # Part 2:  (I-P0...Pn)X

# ## run probing on leftover dims

# ## 