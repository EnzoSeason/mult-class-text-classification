import pickle
import os
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


# python 3

# Loading classifier
classifier_file = open("tweetClassifier.pickle", "rb")
classifier = pickle.load(classifier_file)
classifier_file.close()

#Loading CountVector and TfidfTransformer
count_file = open("count_vect.pickle", 'rb')
count_vect = pickle.load(count_file)
count_file.close()

tfidf_file = open("tfidf_transformer.pickle", 'rb')
tfidf_transformer = pickle.load(tfidf_file)
tfidf_file.close()

# get tweet
tweet = "Norvège : le mois de mai le plus chaud en 71 ans dans le sud-est du pays"

#prediction
res = classifier.predict(tfidf_transformer.fit_transform(count_vect.transform([tweet])))

if res == 0:
	print("Trump")
if res == 1:
	print("Politique")
if res == 2:
	print("Economie")
if res == 3:
	print("Monde")
if res == 4:
	print("Région")
if res == 5:
	print("Santé")
if res == 6:
	print("Culture")
if res == 7:
	print("Tech")
if res == 8:
	print("Sport")
if res == 9:
	print("Société")
if res == 10:
	print("Afrique")
if res == 11:
	print("Planète")
if res == 12:
	print("Moyen-orient")


