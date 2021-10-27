import spacy

#loads the english version into our code
nlp = spacy.load("en_core_web_sm")

#bring in textfile
textfile = open("text for spacy2.txt", 'r').read()

document = nlp(textfile)

#ents allows us to extract the entities from this document
for entity in document.ents:
    print(f"{entity.text}: {entity.label_}")

print(spacy.explain("GPE"))
print(spacy.explain("LOC"))

#Similarity Detection
from pathlib import Path

document1 = nlp(Path("RomeoAndJuliet.txt").read_text())
document2 = nlp(Path("EdwardTheSecond.txt").read_text())

#testing to see how similar document2 is to document1
print(document1.similarity(document2))