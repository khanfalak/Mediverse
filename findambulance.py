import streamlit as st
import requests

class FindAmbulanceApp:
    def __init__(self):
        st.title("Find an Ambulance")
        
        self.search_term = st.text_input("Search for Ambulance in Your Area:")
        self.search_button = st.button("Search")
        
       # self.result_label = st.empty()

        if self.search_button:
            self.search_doctors()

    def search_doctors(self):
        # Use Google Places API to search for doctors
        # Replace 'YOUR_API_KEY' with your actual Google Places API key
        api_key = 'AIzaSyBt1I4b_0y8RphfTIBSlXl6MlPlf4DpEDQ'
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=ambulance service+{self.search_term}&key={api_key}"
        
        response = requests.get(url)
        data = response.json()

        doctors = data.get('results', [])
        self.display_results(doctors)
        #st.write(doctors)
        
        

    def display_results(self, doctors):
        result=[]
        #self.result_label.markdown("### Doctors in Your Area:")
        
        for doctor in doctors:
                 name = doctor['name']
                 address = doctor['formatted_address']
                 rating = doctor.get('rating', 'N/A')
                 openhr= doctor.get('opening_hours')
                 geometry=doctor.get('geometry')
                 result_text = f"Name: {name} Address: {address} Rating: {rating}"
                 result.append(result_text)
        for i in range (len(result)):
            #st.markdown(result[i])
            st.markdown(
            f'<div style="border: 1px solid red; padding: 10px; margin: 10px; background-color: #f0f0f0; color:black;font-weight:bold">{result[i]}</div>',
            unsafe_allow_html=True
        )
        map_url="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d8765.300009601822!2d72.86216055910711!3d19.280045608202837!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sin!4v1694445144998!5m2!1sen!2sin"
       # map_url = "https://www.google.com/maps/dir/{geometry}"
        st.components.v1.iframe(src=map_url, width=800, height=600)
        
        
if __name__ == "__main__":
    app = FindAmbulanceApp()
