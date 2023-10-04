import streamlit as st
def app():
    with open('style.css') as op:   
        st.markdown(f'<style>{op.read()}</style>',unsafe_allow_html=True )

    st.markdown('''
    <div class="text">
    <h1>Welcome to MediVerse - Your Healthcare Companion</h1>
    <hr>
    </div>
    <div class="about">
    <div class="main-about">
        <div class="inner-about">
            <div class="about-content">
                <h2>About us</h2>
                <p>At MediVerse, we believe that everyone deserves access to personalized healthcare information and support at their fingertips.
                Our mission is to empower individuals to take control of their health, make informed decisions, and lead healthier lives.</p>
            </div>
        </div>
        <div class="inner-about">
            <div class="inner-about-image">
                <img src="images/doctor,jpg" alt="">
            </div>
        </div>
    </div>
</div>''',unsafe_allow_html=True)

    image_path = "images/doctor.jpg"  # Replace with the correct path to your image
    st.image(image_path, use_column_width=True)

    st.markdown ( '''
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bree+Serif&family=Bungee+Spice&family=PT+Serif:ital@1&display=swap" rel="stylesheet">
</head>
    <div class="our-services">
    <div class="service-content">
        <div class="left-service-content">
            <h2>Our Services</h2>
            <p>Discover the comprehensive healthcare services and features offered by MediVerse that empower you to take control of your health and well-being:</p>
        </div>   
    </div>
    <div class="main-services">
        <div class="inner-services-content">
         <div class="service-icon">
         <br>
            <h3><i class="fas fa-stethoscope"></i> Predict Disease</h3>
        </div>
            <p>Worried about your health? MediVerse is here to help you stay ahead of any potential health issues.
            Our advanced AI-powered disease prediction feature analyzes your symptoms to provide you with personalized insightsand predictions.
            Take control of your health with early detection and prevention</p>
        </div>
        <div class="inner-services-content">
        <br>
            <h3><i class="fas fa-shield-virus"></i>  Take Preacutions</h3>
            <p>Prevention is better than cure.
            MediVerse offers information on precautions for various diseases and health conditions. 
            Stay informed about the steps you can take to protect yourself and your loved ones. 
            Knowledge is your first line of defense!</p>
        </div>
        <div class="inner-services-content">
        <br>
            <h3><i class="fas fa-user-md"></i>   Find Doctors</h3>
            <p>Need expert medical advice? Finding the right healthcare professional is now easier than ever. 
            MediVerse extensive database of certified doctors, specialists, and healthcare providers allows you to search for the best-suited
             healthcare professionals in your area.</p>
        </div>
        <div class="inner-services-content">
        <br>
            <h3><i class="fas fa-ambulance"></i> Find an Ambulance</h3>
            <p>During emergencies, every second counts. 
            MediVerse ambulance locator feature helps you quickly find the nearest ambulance service to your location. 
            Your safety is our Priority.</p>
        </div>
    </div>
    <div class = "end">
        <div class="end1">
        <hr>
        <h3> Why Choose MediVerse?</h3>
        <ol>
        <li>User-Friendly: Our app is designed with simplicity in mind, making it accessible to users of all ages.</li>
        <li>Accuracy: We use state-of-the-art AI algorithms for disease prediction, ensuring reliable results.</li>
        <li>Comprehensive Information: Access a wealth of healthcare knowledge, from symptoms to treatment options.</li>
        </ol>
        <hr>
        </div>
        <div class="disclaimer">
        <p>Disclaimer: MediVerse is not a substitute for professional medical advice. 
        Consult a healthcare provider for accurate diagnosis and treatment.</p>
        </div>
    </div>

''' , unsafe_allow_html=True)
    
        

