""""
Python script that generates a sample dataset from the given structure
and possible values. Each entry will be randomly populated with a combination of values based on the provided options.

generating sample dataset from this ""phrase_features ={
            'phrase_type':"",
            "tense":"",
            'negative':"",
            "voice":"",
            "tense_verb":"",
            "pronoun_verb":"",
            "has_verb":False,
            "has_auxiliary":False,
            "has_object":False,
            "has_subject":False,
        }
possible values are
        tense_verb in {TenseImperative, TensePast, TenseFuture}
        phrase_type in VERBAL_PHRASE, NOMINAL_PHRASE,
        voice in PASSIVE_VOICE, ACTIVE_VOICE
        negative in AFFIRMATIVE, NEGATIVE,
        pronoun_verb: PRONOUN_ANTA, PRONOUN_HUWA
"""

import random

# Possible values for each attribute
tense_verb_values = ["{TenseImperative}", "{TensePast}", "{TenseFuture}"]
phrase_type_values = ["{VERBAL_PHRASE}", "{NOMINAL_PHRASE}"]
voice_values = ["{PASSIVE_VOICE}", "{ACTIVE_VOICE}"]
negative_values = ["{AFFIRMATIVE}", "{NEGATIVE}"]
pronoun_verb_values = ["{PRONOUN_ANTA}", "{PRONOUN_HUWA}"]
transitive_type_values = ["مشترك", "متعدي بحرف", "متعدي لمفعولين", "لازم"]

# Boolean fields
boolean_values = [True, False]

# Generate sample dataset
def generate_sample_data(num_samples):
    dataset = []
    for _ in range(num_samples):
        phrase_features = {
            "phrase_type": random.choice(phrase_type_values),
            "tense": random.choice(tense_verb_values),
            "negative": random.choice(negative_values),
            "voice": random.choice(voice_values),
            "tense_verb": random.choice(tense_verb_values),
            "pronoun_verb": random.choice(pronoun_verb_values),
            "transitive": random.choice(pronoun_verb_values),
            "transitive_type": random.choice(transitive_type_values),
            "has_verb": random.choice(boolean_values),
            "has_auxiliary": random.choice(boolean_values),
            "has_object": random.choice(boolean_values),
            "has_subject": random.choice(boolean_values),
        }
        dataset.append(phrase_features)
    return dataset
def gen_testset_feature(count =10):
    # Generate and print a dataset with 10 samples
    sample_data = generate_sample_data(10)

    testset = []
    for i, entry in enumerate(sample_data, start=1):
        d = {"id":i,
             "components":entry,
             "valid":True,
             "note":""}
        testset.append(d)
    text = repr(testset)
    text = text.replace("\'{", '')
    text = text.replace("}\'", '')
    text = text.replace("{'id'", "\n{'id'")
    text = text.replace("'components'", "\n'components'")
    text = text.replace("'valid'", "\n'valid'")
    text = text.replace("'note': ''}", "\n'note': ''\n}")
    text = text.replace("'pronoun_verb':", "\n\t\t'pronoun_verb':")
    return text

print(gen_testset_feature(10))


