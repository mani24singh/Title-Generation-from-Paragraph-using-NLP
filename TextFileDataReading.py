from bs4 import BeautifulSoup  # Handling or parsing html files

import nltk  # toolkit

from nltk.corpus import stopwords

r = open(r"file.txt", "r")

html = r.read()

soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)

tokens = [t for t in text.split()]

sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)