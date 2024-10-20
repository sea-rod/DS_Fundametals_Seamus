import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import  WordNetLemmatizer
from nltk import pos_tag


nltk.download("averaged_perceptron_tagger_eng")

def preprocess(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    words = [
        word
        for word in words
        if word not in stop_words and word not in ",.!;:''\"\"" and word.isalpha()
    ]
    return sentences, words


def word_frequency(words):
    freq = dict()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def score_sentences(sentences, freq):
    sentence_scores = dict()
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                sentence_scores[sentence] = (
                    sentence_scores.get(sentence, 0) + freq[word]
                )
    return sentence_scores


def get_wordnet_pos(tag):
    """Convert POS tag to a format compatible with WordNetLemmatizer"""
    if tag.startswith("V"):
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
                if base_word.endswith("e"):
                    past_sentence.append(base_word + "d")
                else:
                    past_sentence.append(base_word + "ed")
        else:
            past_sentence.append(word)
    return " ".join(past_sentence)


def summarize(text, n=3):
    sentences, words = preprocess(text)
    freq = word_frequency(words)
    sentence_scores = score_sentences(sentences, freq)
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[
        :n
    ]
    past_tense_summary = [to_past_tense(sentence) for sentence in summary_sentences]
    return past_tense_summary


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

irregular_verbs = {
    "is": "was",
    "am": "was",
    "are": "were",
    "eat": "ate",
    "go": "went",
    "do": "did",
    "have": "had",
    "take": "took",
    "get": "got",
    "make": "made",
    "see": "saw",
    "come": "came",
    "buy": "bought",
    "bring": "brought",
    "think": "thought",
}

def summarize_review(sentiment_sort):
    for key in sentiment_sort:
        combined_reviews = " ".join(sentiment_sort[key])
        summary = summarize(combined_reviews, n=3)
        print(f"Summary of {key} Reviews:")
        for sentence in summary:
            print("-", sentence)
