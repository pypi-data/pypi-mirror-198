import spacy
from spacy.tokens import Doc

def test_to_bytes():
    nlp = spacy.blank("en")
    nlp.add_pipe('universal_sentence_encoder')
    doc = nlp("This is a test")
    vector = doc.vector

    bytes = doc.to_bytes()
    doc_restored = Doc(nlp.vocab).from_bytes(bytes)