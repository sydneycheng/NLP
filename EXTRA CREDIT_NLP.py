# Create a text file with each comment as a line. Use a For loop to read
# one comment at a time and analyze its sentiment.
# Create a simple bar graph showing the number of positive comments vs
# the negative comments based on the sentiment analysis (using matplotlib).

from textblob import TextBlob
from pathlib import Path
import textblob

text = Path("social media.txt").read_text()
blob = TextBlob(text)

sentences = blob.sentences

for x in sentences:
    print(x)
    print(round(x.sentiment.polarity, 3))


from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)


