from nltk import text
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
#nltk.download("stopwords")
from nltk.corpus import stopwords
import imageio
from operator import itemgetter
from wordcloud import WordCloud

##create List of stopwords
stops = stopwords.words("english")
more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops


##import Book of John txt
john = TextBlob(Path("book of John text.txt").read_text())
nouns = []
nouns += john.noun_phrases


##count word occurences and get top 15 most recurring words
items = john.word_counts.items()

clean_items = [word for word in items if word[0] in nouns and word[0] not in stops]
sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

top_sorted = str(sorted_list[:15])
print(top_sorted)

top15 = " "
for i in top_sorted:
    top15 += i[0]
    top15 += ""
print(top15)


#wordcloud
wordcloud = WordCloud(colormap='prism', background_color='gray')
wordcloud = wordcloud.generate(top15)
wordcloud = wordcloud.to_file('BookOfJohnImage.png')

print('done')


