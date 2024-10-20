from file_utils import open_file
from utils import get_sentiment,get_sentiment_sort,write_sentiment,plot_data
from summarizer import summarize_review

if "__main__" == __name__:
    reviews = open_file("starbucks_reviews.tsv")
    sentiments = get_sentiment(reviews)
    for i in sentiments:
        print(i[0],i[2])
    sort_sentiment = get_sentiment_sort(sentiments)
    # write_sentiment(sort_sentiment)
    # plot_data(sort_sentiment)
    summarize_review(sort_sentiment)