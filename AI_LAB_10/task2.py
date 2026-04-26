import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

data = {
    'text': [
        "Hey, are we still meeting for lunch at 12?",        
        "Don't forget to send me that report by Friday.",    
        "CONGRATULATIONS! You've won a $1000 Walmart gift card! Click here!",
        "URGENT: Your account has been compromised. Verify now.", 
        "Can you pick up some milk on your way home?",       
        "WINNER! Claim your prize money before it's gone!",  
        "Let's catch up over coffee this weekend."           
    ],
    'label': [0, 0, 1, 1, 0, 1, 0] 
}

df = pd.DataFrame(data)

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['text'])
y = df['label']

svm = SVC(kernel='linear')
svm.fit(X, y)

test_emails = [
    "Are you free for a call?", 
    "WIN a million dollars today!!!"
]
test_vectors = tfidf.transform(test_emails)
predictions = svm.predict(test_vectors)

for email, pred in zip(test_emails, predictions):
    category = "SPAM" if pred == 1 else "HAM"
    print(f"Email: '{email}' -> Result: {category}")
