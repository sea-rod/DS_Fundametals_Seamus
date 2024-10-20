import matplotlib.pyplot as plt

def open_file(path):
    with open(path, "r") as file:
        review_data = []
        review = file.readline().strip('\n').split("\t").index("Review")
        for i in file.readlines():
            review_data.append(i.strip('\n').split("\t")[review])
    return review_data

reviews = open_file("starbucks_reviews.tsv")


import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords,wordnet
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import pos_tag

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_review(review):
    processed_data = []
    for row in review:
        words = word_tokenize(row.lower())
        words = [ps.stem(word) for word in words if word.isalpha() and word not in stop_words]
        processed_data.append((row,' '.join(words)))
    return processed_data

processed_review = preprocess_review(reviews)

sia = SentimentIntensityAnalyzer()

def get_sentiment(reviews) :
    sentiment_score = []
    for row in reviews:
        score = sia.polarity_scores(row[1])['compound']
        tag = 'positive' if score > 0.05 else ('negative' if score < -0.05 else 'neutral')
        sentiment_score.append((*row,tag))
    return sentiment_score

sentiment_tags = get_sentiment(processed_review)

sentiment_sort = {'positive':[],"negative":[],"neutral":[] }
for i in sentiment_tags:
    sentiment_sort[i[2]].append(i[0])

def write_file(path,data):
    with open(path,"w") as file:
        for i in data:
            file.write(i+"\n")

for key in sentiment_sort:
    write_file(f"{key}.txt",sentiment_sort[key])

def plot_data(data):
   plt.bar(data.keys(),[len(val) for val in data.values()])
   plt.show()

plot_data(sentiment_sort)

def preprocess(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    words = [word for word in words if word not in stop_words and word not in ",.!;:''\"\"" and word.isalpha()]
    return sentences, words

def word_frequency(words):
    freq = dict()
    for word in words:
        freq[word] = freq.get(word,0)+1
    return freq

def score_sentences(sentences, freq):
    sentence_scores = dict()
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence,0) + freq[word]
    return sentence_scores

lemmatizer = WordNetLemmatizer()

irregular_verbs = {
    "is": "was", "am": "was", "are": "were", "eat": "ate", "go": "went", "do": "did",
    "have": "had", "take": "took", "get": "got", "make": "made", "see": "saw",
    "come": "came", "buy": "bought", "bring": "brought", "think": "thought"
}

def get_wordnet_pos(tag):
    """Convert POS tag to a format compatible with WordNetLemmatizer"""
    if tag.startswith('V'):
        return wordnet.VERB
    return None

def to_past_tense(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    past_sentence = []

    for word, tag in tagged_words:
        pos = get_wordnet_pos(tag)
        if pos == wordnet.VERB:
            if word in irregular_verbs:
                past_sentence.append(irregular_verbs[word])
            else:
                base_word = lemmatizer.lemmatize(word, pos=wordnet.VERB)
                if base_word.endswith('e'):
                    past_sentence.append(base_word + 'd')
                else:
                    past_sentence.append(base_word + 'ed')
        else:
            past_sentence.append(word)
    return ' '.join(past_sentence)

def summarize(text, n=3):
    sentences, words = preprocess(text)
    freq = word_frequency(words)
    sentence_scores = score_sentences(sentences, freq)
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
    past_tense_summary = [to_past_tense(sentence) for sentence in summary_sentences]
    return past_tense_summary

for key in sentiment_sort:
    combined_reviews = " ".join(sentiment_sort[key])
    summary = summarize(combined_reviews, n=3)
    print(f"Summary of {key} Reviews:")
    for sentence in summary:
        print("-", sentence)