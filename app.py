import streamlit as st
import joblib

# Load the trained model and TF-IDF vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.set_page_config(
    page_title="Email Spam Detection System",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Spam Detection System")
st.write(
    "Enter an email subject and message below to determine whether the email "
    "is spam or legitimate."
)
st.info(
    "This system uses a machine learning model trained on email text to "
    "classify messages as either SPAM or LEGITIMATE."
)
subject = st.text_input("Email Subject")

message = st.text_area(
    "Email Message",
    height=250,
    placeholder="Paste or type the email message here..."
)

check_email = st.button("Check Email")
if st.button("Clear"):
    st.rerun()
if check_email:
    email_text = subject + " " + message

    if email_text.strip():
        email_tfidf = vectorizer.transform([email_text])
        prediction = model.predict(email_tfidf)[0]

        if prediction == 1:
            st.error("⚠️ SPAM EMAIL")
            st.write(
                "This email has been classified as spam by the machine learning model."
            )
        else:
            st.success("✅ LEGITIMATE EMAIL")
            st.write(
                "This email has been classified as legitimate by the machine learning model."
            )
    else:
        st.warning("Please enter an email subject or message.")
