import pandas as pd # type: ignore
from sklearn.svm import LinearSVC # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.pipeline import Pipeline # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix # type: ignore
import joblib # type: ignore
from stopwords import updated_stopwords, nlp


def custom_tokenizer(text):
    doc = nlp(text)
    tokens=[]
    for token in doc:

        if token not in updated_stopwords and not token.is_punct:
            # if token is a pronoun, spacy lemmatizes it to "-PRON-"
            if token.lemma_ != "-PRON-":
                temp = token.lemma_.lower().strip()
            else:
                temp = token.lower_
            tokens.append(temp)
    
    return tokens

def train_and_save_model():
    
    columns = ["Sentiment", "Title", "Review"]
    df = pd.read_csv("temp\\test.csv", header=None)
    df.columns = columns
    # -------------------------------------------------------------------------------------------------------------

    # vectorizer object
    tfidf = TfidfVectorizer(tokenizer=custom_tokenizer, ngram_range=(1,2))

    # classifier object
    svc = LinearSVC(random_state = 42)

    # pipeline
    sentiment_model = Pipeline([("tfidf", tfidf), ("svc", svc)])

    # train test split
    X = df["Review"]
    y = df["Sentiment"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # train model
    sentiment_model.fit(X_train, y_train)

    # evaluate test data
    y_pred = sentiment_model.predict(X_test)

    print("accuracy: ", accuracy_score(y_test, y_pred))

    # save model
    joblib.dump(sentiment_model, 'sv_sentiment_classifier.pkl')
    

if __name__=="__main__":
    train_and_save_model()