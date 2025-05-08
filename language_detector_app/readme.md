#                                                         Language Detection Web App using Flask and Machine Learning


## 📌 1. Introduction

Language detection is a fundamental task in Natural Language Processing (NLP) which involves determining the language in which a given piece of text is written. This project demonstrates a language detection system built using Python, machine learning (Naive Bayes), and Flask for deployment through a web interface. The primary objective is to allow users to input any sentence or phrase and receive an instant prediction of its language.

---

## 🎯 2. Objectives

Build a machine learning model to detect language from a sentence.

Design a clean and interactive web interface using Flask and HTML/CSS.

Allow real-time predictions via user input.

Deploy the system locally for demonstration purposes.

---

## 📁 3. Dataset

- Source: A custom CSV file (language.csv) is used.
- Features:
   Text: Input sentence or phrase.
   Language: Target output (language label).
- Sample Data:
   mathematica
   Copy
   Edit
   Text,Language
   Bonjour, French
   Hello, English
   Hola, Spanish
  
## 🧠 4. Machine Learning Model

- 4.1 Data Preprocessing
   Convert textual data into numerical vectors using CountVectorizer.
   Split dataset into training and testing sets using train_test_split.

- 4.2 Model Selection
   Model Used: Multinomial Naive Bayes
   Reason: Performs well on text classification tasks involving word frequency counts.

- 4.3 Model Training
   cv = CountVectorizer()
   X = cv.fit_transform(x)
   x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
   model = MultinomialNB()
   model.fit(x_train, y_train)
  
## 4.4 Model Accuracy
    Evaluated using .score() method.
    Accuracy typically exceeds 95% depending on dataset size and diversity.

--- 

## 🌐 5. Web Application (Flask)

- 5.1 Overview
   A Flask-based web application provides a graphical user interface (GUI) for users to interact with the language detection system.

- 5.2 Features
   Text input field for user sentence.
   "Detect Language" button to submit input.
    Real-time prediction display.

- 5.3 Flask Backend (app.py)
   Handles:
   Model loading and prediction logic.
   Routes for rendering HTML templates and processing form data.

- 5.4 HTML Template (index.html)
   Provides:
   Simple and clean UI using HTML and styled with CSS.
  Responsive layout for better user experience.

5.5 CSS Styling (style.css)
Implements:
Modern layout with card-based design.
Styled form, buttons, and result box for better readability.

---

## 💡 6. Key Technologies Used

- Technology	Purpose
- Python	Core programming language
- Flask	Web framework for deployment
- Scikit-learn	Machine learning toolkit
- HTML/CSS	Frontend user interface
- CountVectorizer	Text feature extraction
- Naive Bayes	Classification algorithm

## ✅ 7. Results

The model can successfully predict languages such as English, Spanish, French, etc., from text inputs.

Web interface is responsive and performs real-time inference.

High accuracy on the test data (~95%).

---

## 🚀 8. Conclusion

This project demonstrates the integration of machine learning and web technologies to build a simple yet effective language detection system. It shows how natural language processing models can be deployed in real-world applications using Flask.

---

## 🔭 9. Future Enhancements

Add more languages and dataset entries for better generalization.

Implement language detection using more advanced models like LSTM or transformers.

Deploy the application to cloud platforms like Heroku, AWS, or Streamlit.

Include auto-detection of language from speech using speech-to-text APIs.

---

## 📎 10. References

Scikit-learn Documentation

Flask Documentation

Natural Language Toolkit (NLTK)

Dataset Sources (Kaggle, UCI)
