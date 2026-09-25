from fastapi import FastAPI
app = FastAPI()

# @app.get("/add/{a}/{b}")
# def addnumbers(a:int, b: int):
#     return("your sum is ....",a+b)


# this is for get and post practice in fastapi
# notes = []

# @app.get("/notes")
# def get_notes():
#     return{"notes", notes}

# @app.post("/notes/{note}")
# def add_note(note: str):
#     notes.append(note)
#     return{"Congratulations" : "Note added" , "notes" : notes}

# This is for sentiment analysis project

@app.get("/sentiment_analysis/{text}")
def check_sentiment(text: str):

    positive_words = ["good", "great", "excellent", "love", "amazing", "best"]
    negative_words = ["bad", "worst", "hate", "terrible", "poor"]

    text_lower = text.lower()

    if any(word in text_lower for word in negative_words) and any (word in text_lower for word in positive_words):
        return {"text": text, "sentiment": "neutral"}
    if any(word in text_lower for word in positive_words):
        return {"text": text, "sentiment": "Positive"}
    elif any(word in text_lower for word in negative_words):
        return {"text": text, "sentiment": "Negative"}
    else:
        return {"text": text, "sentiment": "Neutral"}

print("thanks for having good time  hurrah.......")    