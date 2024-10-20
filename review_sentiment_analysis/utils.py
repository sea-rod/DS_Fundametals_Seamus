import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import pos_tag
import matplotlib.pyplot as plt
from file_utils import write_file


nltk.download("punkt")
nltk.download("stopwords")
nltk.download("vader_lexicon")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
ps = PorterStemmer()
sia = SentimentIntensityAnalyzer()


def preprocess_review(review):
    processed_data = []
    for row in review:
        words = word_tokenize(row.lower())
        words = [
            ps.stem(word) for word in words if word.isalpha() and word not in stop_words
        ]
        processed_data.append((row, " ".join(words)))
    return processed_data


def get_sentiment(reviews):
    reviews = preprocess_review(reviews)
    sentiment_score = []
    for row in reviews:
        score = sia.polarity_scores(row[1])["compound"]
        tag = (
            "positive" if score > 0.05 else ("negative" if score < -0.05 else "neutral")
        )
        sentiment_score.append((*row, tag))
    return sentiment_score

def get_sentiment_sort(sentiment_tags):
    sentiment_sort = {"positive": [], "negative": [], "neutral": []}
    for i in sentiment_tags:
        sentiment_sort[i[2]].append(i[0])
    return sentiment_sort


def write_sentiment(sentiment_sort):
    for key in sentiment_sort:
        write_file(f"{key}.txt",sentiment_sort[key])


def plot_data(data):
    plt.bar(data.keys(), [len(val) for val in data.values()])
    plt.show()
