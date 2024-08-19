### Diabetes Prediction Using Logistic Regression

This project involves the development of a machine learning model to predict whether a person has diabetes based on certain medical features. The model is built using Logistic Regression, a popular algorithm for binary classification tasks.

#### Steps Involved:

1. **Data Preparation:**
   - Collected and preprocessed a dataset containing medical attributes related to diabetes (e.g., glucose levels, BMI, age, etc.) from Kaggle.
   - Split the dataset into training and testing sets to evaluate the model's performance.

2. **Model Development:**
   - Implemented a Logistic Regression model using `scikit-learn`.
   - Trained the model on the training data to learn the relationship between the features and the target variable (whether the person has diabetes or not).

3. **Model Serialization:**
   - After training, the model was saved (serialized) using Python's `pickle` module. This allows the trained model to be easily reused without retraining.

4. **Streamlit Application:**
   - Developed an interactive web application using `Streamlit`.
   - The app allows users to input medical details (such as glucose levels, BMI, etc.) and, upon pressing a button, predicts whether the individual is likely to have diabetes.
   - The prediction is made by loading the pickled Logistic Regression model and applying it to the input data.

5. **How to Run the Application:**
   - To run the Streamlit application, clone this repository and ensure all dependencies are installed (you can use `requirements.txt`).
   - Use the command `streamlit run main.py` to start the application. This will open the app in your web browser, where you can interact with the model and get predictions.
