import spacy
from spacy.util import minibatch, compounding

LABEL = ['I-geo-loc', 'B-geo-loc']

def main():
    output_dir = 'output'
    print("Enter Test Data : ")
    test_text = input()
    print("Loading from Trained Data")
    nlp2 = spacy.load(output_dir)
    doc2 = nlp2(test_text)
    print("Locations in Text : ")
    for ent in doc2.ents:
        print(ent.text ,)

if __name__ == '__main__':
    main()