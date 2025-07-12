# ✉️ Spam Classifier App

This project is a simple yet effective web application that helps identify whether a text message is **spam** or **not spam**. It combines natural language processing (NLP) with machine learning to make accurate predictions, all wrapped in an easy-to-use Streamlit interface.

---

## 🌟 What This App Does

- Takes in any text message you provide
- Processes it using smart NLP techniques like tokenization, stopword removal, and stemming
- Converts the text into numerical features using TF-IDF
- Feeds the features into a trained model to predict if it's spam
- Shows the result instantly on the web interface

---

## 📊 Model Performance

The model used in this project is a **Multinomial Naive Bayes classifier**, trained on a labeled dataset of spam and ham (non-spam) messages.

**Evaluation Results:**
- **Accuracy**: 97.09%
- **Precision**: 1.00
- **Confusion Matrix**:
       [889   0]
       [ 30 115]

  
**Interpretation:**
- 889 legitimate messages correctly classified
- 115 spam messages correctly identified
- 30 spam messages were missed (false negatives)
- 0 legitimate messages were incorrectly flagged as spam (false positives)

These results reflect a high-precision model, with zero false alarms and strong overall accuracy, making it particularly suitable for applications where avoiding false positives is critical.

---

## 🧰 Built With

- **Python 3.9+** for core logic
- **Streamlit** for the web interface
- **scikit-learn** for training the classification model
- **spaCy** and **NLTK** for text preprocessing
- **pickle** for saving and loading the model and vectorizer

---

## 🎯 Why This Project?

This project is a hands-on demonstration of how machine learning and NLP can come together to solve real-world problems like spam detection. It's also a great way to explore deploying ML models in a clean, responsive app.
