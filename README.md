# Sentiment Analysis API

- Creates a FastAPI endpoint `/sentiment_analysis/{text}` that takes the text from the URL.
- Converts the text to lowercase and checks it against predefined lists of positive and negative words.
- Returns **Neutral** if the text contains both positive and negative words.
- Returns **Positive** or **Negative** if only one type of word is found.
- Returns **Neutral** if no keywords match, and sends the result as JSON: `{"text": "...", "sentiment": "..."}`.
