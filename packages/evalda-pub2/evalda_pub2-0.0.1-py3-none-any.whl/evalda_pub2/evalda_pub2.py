#from .ner_tasks.evaluate import run_ner

class Evaluator:
    def __init__(self, model_type: str = None):
        
        self.model_type = model_type
        
        if model_type is None or model_type.lower() not in ['coref', 'ner', 'language model']:
            raise ValueError('This package only supports testing coref, ner and language models.')
        elif model_type.lower() == 'ner':
            print('You can test your NER model by running Evaluator.eval_ner()')
    
    def eval_ner(self, n, model_name, outstyle):
        #model_name = "dacy_large"
        #n = 5
        from .ner_tasks.helper_fns.load_model import model
        from .ner_tasks.helper_fns.performance import eval_model_augmentation, get_table
        from dacy.datasets import dane
        testdata = dane(splits=["test"], redownload=True, open_unverified_connected=True)

        # define augmenters 
        from .ner_tasks.helper_fns.augmentation import dk_aug, muslim_aug, f_aug, m_aug, muslim_f_aug, muslim_m_aug, unisex_aug
        # augmenter, name, n repetitions 
        augmenters = [
            (dk_aug, "Danish names", n),
            (muslim_aug, "Muslim names", n),
            #(f_aug, "Female names", n),
            #(m_aug, "Male names", n),
            #(muslim_f_aug, "Muslim female names", n),
            #(muslim_m_aug, "Muslim male names", n),
            #(unisex_aug, "Unisex names", n),
        ]

        # run model 
        output = eval_model_augmentation(model, model_name, str(n), augmenters, testdata, outstyle)
        #print("created outfile!")
        #get_table(outpath, model_name, str(n))
        #print("created output table!")
        return output
    
        '''

        def print_results(self, model_type):
            if model_type == "ner":
                eval_ner()
            elif model_type == "coref":
                eval_coref()
        '''
