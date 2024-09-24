from create_model import custom_tokenizer
from stopwords import contradiction_tokens, negation_tokens
from nltk.sentiment.vader import SentimentIntensityAnalyzer # type: ignore
import os
from pathlib import Path
if "vader_lexicon.zip" not in os.listdir(os.path.join(Path.home(),r"AppData\Roaming\nltk_data\sentiment")):
    import nltk # type: ignore
    nltk.download("vader_lexicon")
import pandas as pd # type: ignore
    
    
sia = SentimentIntensityAnalyzer()
    
def get_stopwords(nlp):

    # load in spaCy stop words
    stopwords = nlp.Defaults.stop_words
    print(len(stopwords))

    # filter stop words
    updated_stopwords=[]
    for word in stopwords:
        if word not in negation_tokens and word not in contradiction_tokens:
            updated_stopwords.append(word)
    print(len(updated_stopwords))
    
    return updated_stopwords

# split document into sentences for individual sentiment analysis
# if sentence has a contradiction word - split the sentence in two and analyze both halves
def document_breakdown(text:str, nlp):
    doc = nlp(text)
    sentences=[]
    
    for sent in doc.sents:
        sent_left, sent_right, left, right = "", "", "", ""

        for index, token in enumerate(sent):
            if token.text in contradiction_tokens:
                sent_left, sent_right = sent[:index], sent[index+1:]
                left = sent_left.text
                right = sent_right.text
                
            decomposition = {"sentence":{
                    "span_full":sent,
                    "text_full":sent.text,
                    "span_left":sent_left,
                    "text_left":left,
                    "span_right":sent_right,
                    "text_right":left
                }}
                
        sentences.append(decomposition)
        
    subdocs = []
    if sentences:
        for doc in sentences:
            full = doc["sentence"]["span_full"]
            left = doc["sentence"]["span_left"]
            right = doc["sentence"]["span_right"] 
            if right and left:
                subdocs.append(left)
                subdocs.append(right)
            else:
                subdocs.append(full)

            
    return subdocs


def get_vader_score(sentence, sia):
    vader_score = sia.polarity_scores(sentence)["compound"]
    if vader_score > 0:
        return 2
    elif vader_score == 0:
        return "neutral"
    else:
        return 1


def pos_neg_split(sentences:list, model, pos=[], neg=[]):
    
    for s in sentences:
        if not isinstance(s, str):
            s = s.text
        # calculate scores
        vader_score = get_vader_score(s, sia)
        model_score = model.predict([s])[0]

        if vader_score == model_score:
            if model_score == 2:
                pos.append(s)
            elif model_score == 1:
                neg.append(s)
        
        # if vader is neutral, take model score
        elif vader_score=="neutral":
            if model_score == 2:
                pos.append(s)
            elif model_score == 1:
                neg.append(s)
        
        # else take the model score
        else:
            if model_score == 2:
                pos.append(s)
            if model_score == 1:
                neg.append(s)
                
    return pos, neg


def get_aspects(sent_list:list, nlp):
    aspects=[]
    for s in sent_list:
        if not isinstance(s, str):
            s = s.text
        doc = nlp(s)
        for token in doc:
            if token.pos_ in ["NOUN", "ADJ"] and token.text not in aspects:
                aspects.append(token.lemma_)
    return aspects

def get_input_data(path):
    df = pd.read_csv(path)
    reviews = df["Reviews"]
    product = df["Product"]
    return reviews, product
    