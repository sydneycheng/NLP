from pathlib import Path
import imageio
from wordcloud import WordCloud

#Brought in text by using path object
text = Path('RomeoAndJuliet.txt').read_text()

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap='prism', mask=mask_image, background_color='white')

#Fed it the text using generate method
wordcloud = wordcloud.generate(text)

#save it as a file
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

print("done")