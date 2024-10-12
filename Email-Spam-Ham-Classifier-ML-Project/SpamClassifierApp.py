import streamlit as st
import pickle
import string
import nltk
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


# Load the models and vectorizer
tfidf = pickle.load(open('email_spam_vectorizer.pkl','rb'))
models = {
    # 'SVC': pickle.load(open('svc_email_spam_model.pkl', 'rb')),
    'MultinomialNB': pickle.load(open('mnb_email_spam_model.pkl', 'rb')),
    'KNeighborsClassifier': pickle.load(open('knc_email_spam_model.pkl', 'rb')),
    # 'GaussianNB': pickle.load(open('gnb_email_spam_model.pkl', 'rb')),
    'BernoulliNB': pickle.load(open('bnb_email_spam_model.pkl', 'rb')),
    'DecisionTreeClassifier': pickle.load(open('dtc_email_spam_model.pkl', 'rb')),
    'LogisticRegression': pickle.load(open('lrc_email_spam_model.pkl', 'rb')),
    'RandomForestClassifier': pickle.load(open('rfc_email_spam_model.pkl', 'rb')),
    'AdaBoostClassifier': pickle.load(open('abc_email_spam_model.pkl', 'rb')),
    'BaggingClassifier': pickle.load(open('bc_email_spam_model.pkl', 'rb')),
    'ExtraTreesClassifier': pickle.load(open('etc_email_spam_model.pkl', 'rb')),
    'GradientBoostingClassifier': pickle.load(open('gbdt_email_spam_model.pkl', 'rb')),
    'XGBClassifier': pickle.load(open('xgb_email_spam_model.pkl', 'rb')),
    # 'VotingClassifier': pickle.load(open('voting_email_spam_model.pkl', 'rb')),
    # 'StackingClassifier': pickle.load(open('stacking_email_spam_model.pkl', 'rb')),
}

lemmatizer = WordNetLemmatizer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(lemmatizer.lemmatize(i, wordnet.VERB))
    
    return " ".join(y)

st.title("Email Spam And Ham Classifier")

# Add a sidebar to select the model
selected_model = st.sidebar.selectbox("Select Model", list(models.keys()))

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = models[selected_model].predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
        result=0
    else:
        st.header("Ham")


link1 = '[©Developed by Muhammad Talha]()'
link2 = '[LinkedIn](https://www.linkedin.com/in/muhammad-talha-806126234/)'
link3='[GitHub: ](https://github.com/LearnCode801)'
st.sidebar.markdown(link1, unsafe_allow_html=True)
st.sidebar.markdown(link2, unsafe_allow_html=True)    

st.sidebar.markdown(link3, unsafe_allow_html=True) 