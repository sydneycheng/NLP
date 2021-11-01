from nltk import text
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
#nltk.download("stopwords")
from nltk.corpus import stopwords

#import matplotlib.pyplot as plt

import imageio
from wordcloud import WordCloud

##create List of stopwords
stops = stopwords.words("english")
more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops




##import Book of John txt
john = TextBlob(Path("book of John text.txt").read_text())
#john = Path("book of John text.txt").read_text()
#print(john.words)
nouns = john.noun_phrases
#cleanlist = [word for word in john.words if word not in stops if word in nouns]
#print(cleanlist)



##count word occurences and get top 15 most recurring words
items = john.word_counts.items()
#print(items)
clean_items = [word for word in items if word[0] not in stops if word[0] in nouns]
#print(clean_items[:15])

from operator import itemgetter
sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)
print(sorted_list[:15])

john15 = ""
top15 = sorted_list[:15]

for x in top15[0]:
    john15[0] += x
    x + " "
print(john15)

##create mask_image using imageio
#mask_image = imageio.imread('mask_heart.png')

wordcloud = WordCloud(colormap='prism', background_color='white')
wordcloud = wordcloud.generate(john15)
wordcloud = wordcloud.to_file('BookOfJohnImage.png')

print('done')

