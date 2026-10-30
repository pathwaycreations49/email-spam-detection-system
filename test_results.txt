# Email Spam Detection System

## Project Description

The Email Spam Detection System is a machine learning-based application developed to identify and classify email messages as either spam or legitimate.

The system uses natural language processing techniques to convert email text into numerical features using Term Frequency-Inverse Document Frequency (TF-IDF). Three machine learning algorithms were evaluated: Multinomial Naive Bayes, Logistic Regression, and Linear Support Vector Machine (SVM).

The Linear SVM achieved the best overall performance and was selected for integration into the application.

## Dataset

The system was developed using the Enron spam email dataset.

Total emails: 33,716

- Spam: 17,171
- Legitimate (Ham): 16,545

## Machine Learning Models

The following models were evaluated:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Linear Support Vector Machine (SVM)

### Model Performance

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Naive Bayes | 98.81% | 98.36% | 99.33% | 98.84% |
| Logistic Regression | 99.02% | 98.39% | 99.71% | 99.05% |
| Linear SVM | 99.26% | 98.90% | 99.65% | 99.27% |

Linear SVM was selected as the final model based on its strongest overall performance.

## Application

The application was developed using Streamlit. Users can enter an email subject and message, after which the system classifies the email as either:

- SPAM EMAIL
- LEGITIMATE EMAIL

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Linear SVM
- Joblib
- Streamlit
- Matplotlib
- Seaborn
- NLTK