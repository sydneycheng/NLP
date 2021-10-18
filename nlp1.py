from textblob import TextBlob

text = "Today is a beautiful day.  Tomorrow looks like bad weather."
text = "I REALLY HATE YOU"

blob = TextBlob(text)

# #functions
# print(blob.sentences)

# print(blob.words)

# #tagging
# print(blob.tags)


# print(blob.noun_phrases)

# #tells us how positive something is or how negative something is
# print(round(blob.sentiment.polarity, 3))
# print(round(blob.sentiment.subjectivity, 3))
# #returns polarity and subjectivity
# #round returns 3 decimal places


# #scores polarity for each sentence
# for sentence in blob.sentences:
#     print(sentence)
#     print(round(sentence.sentiment.polarity, 3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)



spanish = blob.translate(to='es')

print(spanish)

chinese = blob.translate(to='zh')

print(chinese)

print(chinese.translate())