from textblob import TextBlob
import random
import sys

# stdin's read() method just reads in all of standard input as a string;
# use the decode method to convert to ascii (textblob prefers ascii)
text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(text)

short_sentences = list()
for sentence in blob.sentences:
    if len(sentence.words) <= 5:
        short_sentences.append(sentence.replace("\n", " "))

for item in random.sample(short_sentences, 10):
	print item