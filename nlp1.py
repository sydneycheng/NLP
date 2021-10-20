from textblob import TextBlob

# text = "Today is a beautiful day.  Tomorrow looks like bad weather."
# text = "I REALLY HATE YOU"

# blob = TextBlob(text)

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

# from textblob.sentiments import NaiveBayesAnalyzer

# blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

# for sentence in blob.sentences:
#     print(sentence.sentiment)



# spanish = blob.translate(to='es')

# print(spanish)

# chinese = blob.translate(to='zh')

# print(chinese)

# print(chinese.translate())



#changing words to their singular or plural form
from textblob import Word

index = Word('index')   #this creates a word object called index
print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())


#spellcheck and correction
word = Word('theyr')

print(word.spellcheck())
print(word.correct())

#Normalization: lemmatization or stemming
word1 = Word("studies")
word2 = Word("varieties")

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())

#Definitions, Synonyms and Antonyms from WordNet
happy = Word("happy")

print(happy.definitions)
print(happy.synsets)    # A set of synonyms

for s in happy.synsets:
    for l in s.lemmas():
        print(l.name())

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

antonym = happy.synsets[0].lemmas()[0].lemmas()[0].antonyms()[0].name()
print(antonym)