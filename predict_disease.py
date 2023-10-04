#predict disease
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def app():

    random_seed = 42

  
    df = pd.read_csv("C:\\Users\\mkash\\Desktop\\streamlit\\Training.csv")
    df.drop('Unnamed: 133', axis=1, inplace=True)
    

    x = df.drop('prognosis', axis=1)
    y = df['prognosis']

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=random_seed)


    # Random Forest Classifier
    random_forest = RandomForestClassifier(random_state=random_seed)
    random_forest.fit(x_train.values, y_train)
    random_forest_pred = random_forest.predict(x_test.values)

    # Calculate accuracy score
    accuracy = accuracy_score(y_test, random_forest_pred)

    # Streamlit app
    st.title("Disease Predictor System")

    st.write(f"Accuracy Score (Random Forest): {accuracy}")
    # Sidebar
    st.header("Select Symptoms")
    symptoms = []
    for i in range(5):
        symptom = st.selectbox(f"Symptom {i+1}", [''] + sorted(x.columns))
        if symptom:
            symptoms.append(symptom)

    # Analyze Button
    if st.button("Predict"):
        selected_symptoms = ", ".join(symptoms)
        st.write(f"Selected Symptoms: {selected_symptoms}")

        l2 = [1 if symptom in symptoms else 0 for symptom in x.columns]
        inputtest = [l2]

        # Predictions 
        predicted_disease_random_forest = random_forest.predict(inputtest)[0]
        st.write(f"Predicted Disease: {predicted_disease_random_forest}")
   