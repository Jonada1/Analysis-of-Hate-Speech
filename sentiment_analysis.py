from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


def sentiment_analyser(comments):
	sentiment_intensity_analyzer = SentimentIntensityAnalyzer()
	polarity_dictionaries = []
	for comment in comments:
		polarity_dictionary = sentiment_intensity_analyzer.polarity_scores(comment.body)
	polarity_dictionaries.append(polarity_dictionary)
	return polarity_dictionaries


def sentiment_polarity_printer(polarity_dictionaries):
	total_sentiment = ""
	for polarity_dictionary in polarity_dictionaries:
		for polarity_score_key in sorted(polarity_dictionary):
			sentiment = '{0}: {1}, '.format(polarity_score_key, polarity_dictionary[polarity_score_key])
			total_sentiment += sentiment
	return total_sentiment
