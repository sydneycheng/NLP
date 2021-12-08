# Create a text file with each comment as a line. Use a For loop to read
# one comment at a time and analyze its sentiment.
# Create a simple bar graph showing the number of positive comments vs
# the negative comments based on the sentiment analysis (using matplotlib).

from textblob import TextBlob
from pathlib import Path

text = TextBlob(Path("social media.txt").read_text())