import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score

# Set Random seed
# np.random.seed(500)

# Add the Train Data using pandas
Corpus = pd.read_csv(r"C:\Users\Agolli\Downloads\Text-Classification-master\Text-Classification"
                     r"-master\train.csv", encoding='latin-1')

# Add the Test Data using pandas
CorpusTest = pd.read_csv(r"C:\Users\Agolli\Downloads\Text-Classification-master\Text"
                         r"-Classification-master\test.csv", encoding='latin-1')

# Step - 1: Data Pre-processing - This will help in getting better results through the
# classification algorithms

# Remove blank rows if any.
Corpus['text'].dropna(inplace=True)
CorpusTest['text'].dropna(inplace=True)

# Change all the text to lower case. "news" and "NEWS" and
Corpus['text'] = [entry.lower() for entry in Corpus['text']]
CorpusTest['text'] = [entry.lower() for entry in CorpusTest['text']]

# Tokenization : In this each entry in the corpus will be broken into set of words
Corpus['text'] = [word_tokenize(entry) for entry in Corpus['text']]
CorpusTest['text'] = [word_tokenize(entry) for entry in CorpusTest['text']]


# Remove Stop words, Non-Numeric and perform Word Stemming/Lemmenting.

# WordNetLemmatizer requires Pos tags to understand if the word is noun or verb or adjective
# etc. By default it is set to Noun
tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

# Train Lemmatizer
for index, entry in enumerate(Corpus['text']):
    # Declaring Empty List to store the words that follow the rules for this step
    Final_words = []
    # Initializing WordNetLemmatizer()
    word_Lemmatized = WordNetLemmatizer()
    # pos_tag function below will provide the 'tag' if the word is Noun(N) or Verb(V) or smth else
    for word, tag in pos_tag(entry):
        # Below condition is to check for Stop words and consider only alphabets
        if word not in stopwords.words('english') and word.isalpha():
            word_Final = word_Lemmatized.lemmatize(word, tag_map[tag[0]])
            Final_words.append(word_Final)
    # The final processed set of words for each iteration will be stored in 'text_final'
    Corpus.loc[index, 'text_final'] = str(Final_words)

# Test Lemmatizer
for index, entry in enumerate(CorpusTest['text']):
    # Declaring Empty List to store the words that follow the rules for this step
    Final_words = []
    # Initializing WordNetLemmatizer()
    word_Lemmatized = WordNetLemmatizer()
    # pos_tag function below will provide the 'tag' if the word is Noun(N) or Verb(V) or smth else
    for word, tag in pos_tag(entry):
        # Below condition is to check for Stop words and consider only alphabets
        if word not in stopwords.words('english') and word.isalpha():
            word_Final = word_Lemmatized.lemmatize(word, tag_map[tag[0]])
            Final_words.append(word_Final)
    # The final processed set of words for each iteration will be stored in 'text_final'
    CorpusTest.loc[index, 'text_final'] = str(Final_words)

# print(Corpus['text_final'])


# Step - 2: Split the model into Train and Test Data set
# Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus['text_final'],
#                                                                     Corpus['label'], test_size=0.3)

Train_X = Corpus['text_final']
Train_Y = Corpus['label']
# print("train")
# print(Train_X)
# print(Train_Y)

Test_X = CorpusTest['text_final']
Test_Y = CorpusTest['label']
# print("test")
# print(Test_X)
# print(Test_Y)
# Step - 3: Label encode the target variable

Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(Train_Y)
Test_Y = Encoder.fit_transform(Test_Y)

# Step - 4: Vectorize the words by using TF-IDF Vectorizer - This is done to find how important
# a word in document is in comaprison to the corpus
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(Corpus['text_final'])

Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)

# Step - 5: Now we can run different algorithms to classify out data check for accuracy

# Classifier - Naive Bayes

# fit the training dataset on the classifier
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf, Train_Y)

# predict the labels on validation dataset
predictions_NB = Naive.predict(Test_X_Tfidf)

# Use accuracy_score function to get the accuracy
print("Naive Bayes Accuracy Score -> ", accuracy_score(predictions_NB, Test_Y) * 100)

# Classifier - SVM
# fit the training dataset on the classifier
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf, Train_Y)

# predict the labels on validation dataset
predictions_SVM = SVM.predict(Test_X_Tfidf)

# Use accuracy_score function to get the accuracy
print("SVM Accuracy Score -> ", accuracy_score(predictions_SVM, Test_Y) * 100)

# Accuracy score

# Dataset - fake_or_real_news.csv
# Naive Bayes Accuracy Score ->  89.00578642819569
# SVM Accuracy Score ->  92.47764334560758

# Dataset - train.csv and test.csv
# Naive Bayes Accuracy Score ->  59.662877303018426
# SVM Accuracy Score ->  60.99568796550372
