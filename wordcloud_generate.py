from bs4 import BeautifulSoup
import requests

import matplotlib.pyplot as plt
from wordcloud import WordCloud


with open('index.html', encoding="utf-8") as f:
    data = f.read()

soup = BeautifulSoup(data, "html.parser")

complete_text = ""


results = soup.findAll("p")
for element in results:
    
    complete_text+=element.text+" "

results = soup.findAll("h2")
for element in results:
    complete_text+=element.text+" "

results = soup.findAll("h3")
for element in results:
    complete_text+=element.text+" "

results = soup.findAll("td")
for element in results:
    complete_text+=element.text+" "


print(complete_text)

text = complete_text

'''
word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(text)

# Display the generated Word Cloud

plt.imshow(word_cloud2)

plt.axis("off")

figure = plt.gcf()

figure.set_size_inches(15, 9.375)

#plt.show()bbox_inches='tight' ,pad_inches=2
#plt.savefig('images/wordcloud.jpg',dpi=96,bbox_inches = 'tight',pad_inches = 0)

'''
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(text)
 
# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)





plt.savefig('images/wordcloud.jpg')