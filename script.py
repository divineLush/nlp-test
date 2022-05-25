import spacy
import json

nlp = spacy.load('en_core_web_sm')

with open ("test.txt", "r") as f:
    text = f.read()
    doc = nlp(text)

    with open('output.json', 'w') as output_f:
        labels_arr = [{ "begin": ent.start_char, "end": ent.end_char, "label": ent.label } for ent in doc.ents]
        data = [{"labels": labels_arr, "text": text}]
        json.dump(data, output_f)
