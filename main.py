import pandas as pd # type: ignore
import functions
import joblib # type: ignore
from nltk.sentiment.vader import SentimentIntensityAnalyzer # type: ignore
from stopwords import nlp
from datetime import datetime
import shutil
from create_model import custom_tokenizer

def main(nlp, data_path, **comment):
    today = datetime.now().strftime("%d-%m-%y")
    
    # load spacy vocab
    print("Loaded spacy model.")

    # load model    
    model = joblib.load(r"C:\Users\bmurraysmith\OneDrive - SharkNinja\Documents\ML\Sentiment model\sv_sentiment_classifier.pkl")
    print("Loaded SVC model.")

    # load VADER analyser
    sia = SentimentIntensityAnalyzer()
    print("Initialized VADER.")

    
    reviews, product = functions.get_input_data(data_path)


    # empty dataframe
    analysis = pd.DataFrame(columns=["Date", "Product", "Review", "Sentiment", "Positive Aspects", "Positive Comments", "Negative Aspects", "Negative Comments"])

    
    print("Processing reviews...")
    for review in reviews:
        prediction = model.predict([review])[0]
        if prediction==2:
            prediction="Positive"
        else:
            prediction="Negative"
        
        # break review into sentences
        subdocs = functions.document_breakdown(review, nlp)
        
        # split on positive/negative
        pos, neg = functions.pos_neg_split(subdocs, model, pos=[], neg=[])
        
        # pull aspects of sentiment
        if pos:
            pos_aspects = functions.get_aspects(pos, nlp=nlp)
        else:
            pos, pos_aspects="", ""
            
        if neg:
            neg_aspects = functions.get_aspects(neg, nlp=nlp)
        else:
            neg, neg_aspects="", ""
                
        today_data={
            "Date":today,
            "Product":product[0],
            "Review":review,
            "Sentiment":prediction,
            "Positive Aspects":pos_aspects,
            "Positive Comments":pos,
            "Negative Aspects":neg_aspects,
            "Negative Comments":neg,
        }
        
        new_row = pd.DataFrame([today_data])
        analysis = pd.concat([analysis, new_row], ignore_index=True)
        
        
    analysis.to_csv("sentiment_analysis.csv", index=False)
    shutil.move("sentiment_analysis.csv", rf"sentiment {today}.csv")
    print("Success.")


if __name__=="__main__":
    path=r"C:\Users\bmurraysmith\OneDrive - SharkNinja\Documents\ML\data files\Air Fryer review scrape.csv"
    main(nlp=nlp, data_path=path)
    