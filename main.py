import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#Load dataset from CSV file
data = pd.read_csv("omicron.csv")
print(data.head())
print(data.isnull().sum())

#Import additions libraries for text preprocessing
import nltk
import re
nltk.download('stopwords')
stemmer=nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stopwords=set(stopwords.words('english'))

#Define a function to clean the text data
def clean_text(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopwords]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return text

#Apply the cleaning function to the 'text' column in dataset
data["text"] = data["text"].apply(clean_text)

#Generate word cloud from cleanded text
text= " ".join(i for i in data.text)
stopwords = set(STOPWORDS)
wordcloud=WordCloud(stopwords=stopwords,background_color="white").generate(text)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()
#perform sentiment analysis using VADER
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
data['sentiments'] = data['text'].apply(lambda x: sia.polarity_scores(x))
print(data[['cleaned_text', 'sentiment']].head())
#Extract sentiment scores for each text entry
data ["Positive"]= [sentimets.polarity_scores (i)["pos"] for i in data["text"]] # Postive score
date ["Negative"]= [sentimets.polarity_scores (i)["neg"] for i in data["text"]] # Negative score
data ["Neutral"]= [sentimets.polarity_scores (i)["neu"] for i in data["text"]] # Neutral score

#Keep only relevant columns
data = data[["text", "Positive", "Negative", "Neutral"]]
print(data.head())
results

#Sum up sentiment scores across all text entries
x = sum(data["Positive"])
y = sum(data["Negative"])
z = sum(data["Neutral"])

#Define a function to determibe overall sentiment
def sentiment_score(a,b,c):
    if (a>b) and (a>c):
        return "Positive"
    elif (b>a) and (b>c):
        return "Negative"
    else:
        return "Neutral"
#Call function with aggregated sentiment Scores
sentiment = sentiment_score(a,b,c)
print(f"Overall sentiment: {sentiment_results}")