from textblob import TextBlob
from newspaper import Article

# for newspaper article
#url = "https://www.indiatoday.in/india/story/renukaswamy-murder-case-actor-darshan-karnataka-police-pavithra-gowda-2553403-2024-06-15"
# article = Article(url)

# article.download()  # Downloads the link’s HTML content
# article.parse()  # Parse the article
# article.nlp()  # Keyword extraction wrapper

user = input("Enter text (should be a long one):")
text = user  # Get the article’s text

# Print the article’s text
print(text)


blob = TextBlob(text)  # Create a TextBlob object

sentiment = blob.sentiment.polarity  # Get the sentiment of the article

print("The sentiment analysis of provided text is : ",sentiment," -1 is negative , 0 is neutral, 1 is positive")
