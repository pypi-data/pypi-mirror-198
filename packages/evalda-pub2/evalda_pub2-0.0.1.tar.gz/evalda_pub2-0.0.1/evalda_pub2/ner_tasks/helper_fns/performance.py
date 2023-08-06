from dacy.score import n_sents_score, score
from pathlib import Path
import spacy
import dacy
import os 
import pandas as pd


def get_table(df):
    '''
    Compute mean F1 for each augmenter of a single model. 

    input:
     - fpath : path to CSV file with model performance of a single model. 

    output: 
    - CSV file in folder "robustness" (creates directory if it does not exist)
    '''
    #df = pd.read_csv(fpath)
    df["f1"] = df["ents_excl_MISC_ents_f"]*100
    df = df[df["augmenter"].isin(["Danish names", "Female names", "Male names", "Unisex names", "Muslim names", "Muslim male names", "Muslim female names"])]
    augs, means, sds = [],[],[]
    for aug in set(df["augmenter"]):
        augs.append(aug)
        sub = df[df["augmenter"]==aug]
        means.append(round(sub["f1"].mean(),1))
        sds.append(round(sub["f1"].std(),1))
    out_df = pd.DataFrame({"augmenter": augs, "F1": means, "SD": sds})
    return out_df
    #out_df.to_csv(os.path.join(Path(__file__).parents[2], "output", f"{mname}_{n}_f1_table.csv"))


def eval_model_augmentation(mdl, model_name, n, augmenters, dataset, outstyle):
    '''
    Return CSV file of model performance on NER task with different name augmentations
    using DACY score function
    input:
    - model_dict : dictionary of models to be run
    - dataset : test dataset for model eval
    - augmenters 
    output: 
    - CSV file in folder "robustness" (creates directory if it does not exist)
    '''

    # loop over all models in model_dict 
    #outpath = os.path.join(Path(__file__).parents[2], "output", f"{model_name}_{n}_augmentation_performance.csv")
    scores = []
    i = 0
    for aug, nam, k in augmenters:
        print(f"\t Running augmenter: {nam} | Amount of times: {k}")
        scores_ = score(corpus=dataset, apply_fn=mdl, augmenters=aug, k=k)
        scores_["model"] = model_name
        scores_["augmenter"] = nam
        scores_["i"] = i
        scores.append(scores_)
        i += 1
    scores_df = pd.concat(scores)
    
    if outstyle == "verbose":
        scores_df = scores_df
    elif outstyle == "condensed":
        scores_df = get_table(scores_df)
    else:
        raise ValueError("outstyle must be either 'verbose' or 'condensed'")
    
    #scores_df.to_csv(outpath)
    return scores_df
