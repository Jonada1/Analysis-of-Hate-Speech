from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


def sentiment_analyser(comments):
	sentiment_intensity_analyzer = SentimentIntensityAnalyzer()
	comment_as_whole = ""
	for comment in comments:
		comment_as_whole += " " + comment.body
	total_sentiment = sentiment_intensity_analyzer.polarity_scores(comment.body)
	return total_sentiment


def sentiment_polarity_printer(polarity_dictionary):
	total_sentiment = ""
	for polarity_score_key in sorted(polarity_dictionary):
		sentiment = '{0}: {1}, '.format(polarity_score_key, polarity_dictionary[polarity_score_key])
		total_sentiment += sentiment
	return total_sentiment
