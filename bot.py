import streamlit as st
import pandas as pd

def app():

    # Load data and dictionaries
    #training = pd.read_csv('Training.csv')
    description_df = pd.read_csv('symptom_Description.csv')
    precaution_df = pd.read_csv('symptom_precaution.csv')

    # Convert disease names in the dataset to lowercase for case-insensitive matching
    description_df['Disease'] = description_df['Disease'].str.lower()

    # Create dictionaries for description and precautions
    description_dict = dict(zip(description_df['Disease'], description_df['Description']))
    precaution_dict = {
        row['Disease'].lower(): [row['Precaution_1'], row['Precaution_2'], row['Precaution_3'], row['Precaution_4']]
        for _, row in precaution_df.iterrows()
    }

    # Streamlit UI
    st.title("Precautionary Recommendations")
    name = st.text_input("Your Name")

    if name:
        st.write(f"Hello, {name}")

        disease_name = st.text_input("Enter the disease name:")

        if disease_name:
            # Convert user input to lowercase for case-insensitive matching
            disease_name_lower = disease_name.lower()

            # Check if the disease name exists in description_dict (case-insensitive)
            if disease_name_lower in description_dict:
                actual_disease_name = description_df.loc[
                    description_df['Disease'] == disease_name_lower, 'Disease'].iloc[0]
            else:
                actual_disease_name = None

            if actual_disease_name:
                st.subheader(f"Description of {actual_disease_name.capitalize()}:")
                st.write(description_dict[actual_disease_name])

                # Check if the disease name exists in precaution_dict (case-insensitive)
                precautions = precaution_dict.get(actual_disease_name, [])

                if precautions:
                    st.subheader(f"Precautions for {actual_disease_name.capitalize()}:")
                    for i, precaution in enumerate(precautions, start=1):
                        st.write(f"{i}. {precaution}")
                else:
                    st.warning("Precautions not found for this disease.")
            else:
                st.error("Disease not found in the database. Please enter a valid disease name.")

  
