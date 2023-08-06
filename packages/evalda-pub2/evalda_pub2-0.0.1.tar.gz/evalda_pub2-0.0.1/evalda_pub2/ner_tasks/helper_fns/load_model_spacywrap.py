### load hugginface model with spacywrap 
from spacy_langdetect import LanguageDetector
from spacy.language import Language

@Language.factory('language_detector')
def language_detector(nlp, name):
    return LanguageDetector()


import spacy, spacy_wrap
nlp = spacy.blank("en")

# specify model from the hub
config = {"model": {"name": "dslim/bert-base-NER"}}

# add it to the pipe
nlp.add_pipe('language_detector', last=True)
nlp.add_pipe("token_classification_transformer", config=config)

doc = nlp("My name is Wolfgang and I live in Berlin.")

print(doc.ents)
# (Wolfgang, Berlin)



