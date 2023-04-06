from pathlib import Path
from tqdm import tqdm
import sys
from nli_xy.constants import AMNESIC_PATH, MODEL_NAMES, model_pretrained_paths, model_label_mapper
sys.path.append(AMNESIC_PATH)
import torch
import numpy as np
from amnesic_probing.tasks.utils import rand_direction_control

# get all control reps and get accuracies


if __name__ == '__main__':

    for label_column in ['control']:
        for model_name in MODEL_NAMES:

            results_dir = Path(f'experiments/interventions/results/{label_column}/{model_name}/')
            control_reps_dir = results_dir.joinpath('control_reps/')
            meta_path = results_dir.joinpath('meta.tsv')


            if not os.path.exists(results_dir):
                os.makedirs(control_reps_dir)

            intervened_dir = control_reps_dir
            for control_dims in range(1, 15):
                try:
                    with open(intervened_dir.joinpath(f'control_{control_dims}.npy'), 'rb') as file:
                        rand_control = np.load(file)

                except FileNotFoundError:
                    rand_control, rand_direction_p = generate_control(x_test, control_dims, intervened_dir=intervened_dir)

                    remain_p = np.identity(x_test.shape[1]) - rand_direction_p
                    print(remain_p.shape)
                    rand_directions = sp.linalg.orth(remain_p)
                    print(len(rand_directions))
                    print(rand_directions[0].shape)

                    rand_rank = np.linalg.matrix_rank(rand_control)
                    print(f'Rank of Control Matrix: {rand_rank}\n')

                    rand_accuracy = get_prediction_accuracy(rand_control, model, gold_labels)
                    print(f'control accuracy with {control_dims} remaining dimensions: {rand_accuracy}')

                    Ws = []
                    for i in range(b_rank):
                        W = np.load(Path(out_dir).joinpath(f'W_{i}.npy'))
                        Ws.append(W)
                    dot_matrix = np.asarray([[np.dot(r,w.T)/(norm(r)*norm(w)) for r in rand_directions] for w in Ws])
                    dot_matrix = dot_matrix.reshape(len(rand_directions), len(Ws))
                    print(f'DOT Product Matrix Shape: {dot_matrix.shape}')
                    plt.imshow(dot_matrix, cmap='hot', interpolation='nearest')
                    plt.show()

                    project_and_show(rand_control, meta_df)

                if show:
                    project_and_show(x_test, meta_df)
                    project_and_show(debiased, meta_df)

            #     MOST COMPELLING SO FAR (or... it just flips stuff so performs poorly? compare reflection)
            #     debiased = (P-np.identity(P.shape[0])).dot(x_test.T).T

            #     TODO: weird inverse
            #     debiased = np.dot(x_test, (np.identity(P.shape[0]) - P))

            #     SANITY CHECK4
            #     Ensure probing dataset model predictions and eval_on_nli_xy  predictions match up
            #     other_df = pd.read_csv(f'experiments/nli/eval_on_nli_xy/results/{model_name}/nli_xy_meta.tsv', sep='\t')

            #     for test_context in set(df.context.to_list()):
            #         a = df.loc[(df.context==test_context)]
            #         b = other_df.loc[other_df.context==test_context]

            #         test_pairs  = a.insertion_pair.to_list()
            #         for test_pair in test_pairs:
            #             part_a = a.loc[a.insertion_pair==test_pair]
            #             part_b = b.loc[b.insertion_pair==test_pair]

            #             gold_a = set(part_a['model_predictions'].to_list())
            #             gold_b = set(part_b['model_predictions'].to_list())

            #             try:
            #                 print(test_pair)
            #                 print(gold_a)
            #                 print(gold_b)
            #                 break

            # #other_df always has two_label predictions
