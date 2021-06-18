
#%%
import S01_generate_instances, S02_generate_dataset, S03_train_gcnn, S04_test
from types import SimpleNamespace

#%%
if __name__ == '__main__':

    # %%

    problem = "setcover"
    samplingStrategy = "depthK2" # choices: uniform5, depthK, depthK2
    sampling_seed = 1
    train_seeds = "range(0,10)"
    gpu = 0 # CUDA GPU id (-1 for CPU).

    # %%
    # S01_args = {
    #     'problem' : problem,
    #     'n_instances' : "(100, 20, 10, 20)",
    #     'seed' : 0,
    # }
    # S01_args = SimpleNamespace(**S01_args)
    # S01_generate_instances.exp_main(S01_args)


    # strategies = ["uniform5", "depthK"]
    # for samplingStrategy in strategies:

    # %%
    S02_args = {
        'problem' : problem,
        'sampling' : samplingStrategy,
        'seed' : sampling_seed,
        'njobs' : 9,
        'n_samples' : "(1000, 200, 200)" # Number of generated n_samples as (train_size, valid_size, test_size).
    }
    S02_args = SimpleNamespace(**S02_args)
    S02_generate_dataset.exp_main(S02_args)

    # %%
    S03_args = {
        'model' : 'baseline',
        'gpu' : gpu,
        'problem' : problem,
        'sampling' : samplingStrategy,
        'sample_seed' : sampling_seed,
        'seeds' : train_seeds # python expression as string, to be used with eval(...)
    }
    S03_args = SimpleNamespace(**S03_args)
    S03_train_gcnn.exp_main(S03_args)

    # %%
    S04_args = {
        'gpu': gpu,
        'problem': problem,
        'sampling' : samplingStrategy,
        'sample_seed' : sampling_seed,
        'seeds' : train_seeds, # python expression as string, to be used with eval(...)
    }
    S04_args = SimpleNamespace(**S04_args)
    S04_test.exp_main(S04_args)