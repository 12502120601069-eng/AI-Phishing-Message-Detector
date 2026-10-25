```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample messages for training
messages = [
    "You won a free prize click here",
    "Verify your bank account immediately",
    "Claim your reward now",
    "Send your password to receive money",
    "Click this link to win a lottery",
    "Your account will be blocked verify now",
    "Hello how are you",
    "Your class starts at 10 am",
    "Please send me your notes",
    "Your order has been delivered",
    "We will meet tomorrow",
    "Thank you for your help"
]

# Labels for each message
labels = [
    "Phishing",
    "Phishing",
    "Phishing",
    "Phishing",
    "Phishing",
    "Phishing",
    "Legitimate",
    "Legitimate",
    "Legitimate",
    "Legitimate",
    "Legitimate",
    "Legitimate"
]

# Convert messages into numbers
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(messages)

# Train the machine learning model
model = MultinomialNB()
model.fit(x, labels)

print("AI Phishing Message Detector")
print("----------------------------")

while True:
    text = input("\nEnter a message (or type exit): ")

    if text.lower() == "exit":
        print("Program closed.")
        break

    if text.strip() == "":
        print("Please enter a message.")
        continue

    # Convert user message into numbers
    new_message = vectorizer.transform([text])

    # Predict the result
    result = model.predict(new_message)

    print("Prediction:", result[0])

    if result[0] == "Phishing":
        print("Warning: This message may be suspicious.")
    else:
        print("This message appears legitimate to the model.")
```
