from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd

#nltk.download("stopwords")

from nltk.corpus import stopwords

#create List of stopwords
stops = stopwords.words("eng")

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]

#import Book of John txt
blob = TextBlob(Path("book of John text.txt").read_text())

cleanlist = [word for word in blob.words if word not in stops]

print(cleanlist)

