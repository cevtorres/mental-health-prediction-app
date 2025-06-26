import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open('model.pkl', 'rb'))

gender_encoder = LabelEncoder()
location_type_encoder = LabelEncoder()
wellness_apps_encoder = LabelEncoder()
eats_healthy_encoder = LabelEncoder()

st.title("Mental Health Prediction App")
st.subheader("Enter the details below to predict mental health status")
age = st.slider("How old are you?", 0, 100, 25)
gender = st.selectbox(
    "What is your gender?",
    ("Female", "Male", "Other"),
)
daily_screen_time_hours= st.slider("How many hours do you spend on screens daily?", 0, 24, 0)
phone_usage_hours= st.slider("How many hours do you spend on your phone daily?", 0, 24, 0)
laptop_usage_hours= st.slider("How many hours do you spend on your laptop daily?", 0, 24, 0)
tablet_usage_hours= st.slider("How many hours do you spend on your tablet daily?", 0, 24, 0)
tv_usage_hours = st.slider("How many hours do you spend watching TV daily?", 0, 24, 0)
social_media_hours = st.slider("How many hours do you spend on social media daily?", 0, 24, 0)
work_related_hours = st.slider("How many hours do you spend on work-related tasks daily?", 0, 24, 0)
entertainment_hours = st.slider("How many hours do you spend on entertainment daily?", 0, 24, 0)
gaming_hours = st.slider("How many hours do you spend gaming daily?", 0, 24, 0)
sleep_duration_hours = st.slider("How many hours do you sleep daily?", 0, 24, 0)
sleep_quality = st.slider("Rate your sleep quality from 1 to 10", 1, 10, 5)
mood_rating = st.slider("Rate your mood from 1 to 10", 1, 10, 5)
stress_level = st.slider("Rate your stress level from 1 to 10", 1, 10, 5)
physical_activity_hours_per_week = st.slider("How many hours do you exercise per week?", 0, 20, 0)
location_type = st.selectbox(
    "Where do you live?",
    ("Rural", "Suburban", "Urban"),
)
uses_wellness_apps = st.selectbox(
    "Do you use wellness apps?",
    ("No", "Yes"),
)
eats_healthy = st.selectbox(
    "Do you eat healthy?",
    ("No", "Yes"),
)
caffeine_intake_mg_per_day = st.slider("How much caffeine do you consume daily (in mg)?", 0, 1000, 0)
weekly_anxiety_score = st.slider("Rate your weekly anxiety from 1 to 20", 1, 20, 5)
weekly_depression_score = st.slider("Rate your weekly depression from 1 to 20", 1, 20, 5)
mindfulness_minutes_per_day = st.slider("How many minutes do you practice mindfulness daily?", 0, 40, 0)

gender_encoded = gender_encoder.fit_transform([gender])[0]
location_type_encoded = location_type_encoder.fit_transform([location_type])[0]
wellness_apps_encoded = wellness_apps_encoder.fit_transform([uses_wellness_apps])[0]
eats_healthy_encoded = eats_healthy_encoder.fit_transform([eats_healthy])[0]

if 'is_submitted' not in st.session_state:  
    st.session_state.is_submitted = False

if st.button("Submit"): 
    st.session_state.is_submitted = True
    array = np.array([age, gender_encoded, daily_screen_time_hours, phone_usage_hours, laptop_usage_hours, tablet_usage_hours, tv_usage_hours, social_media_hours, work_related_hours, entertainment_hours, gaming_hours, sleep_duration_hours, sleep_quality, mood_rating, stress_level, physical_activity_hours_per_week, location_type_encoded, wellness_apps_encoded, eats_healthy_encoded, caffeine_intake_mg_per_day, weekly_anxiety_score, weekly_depression_score, mindfulness_minutes_per_day])
    array = array.reshape(1, -1)
    prediction = model.predict(array)
    st.session_state.prediction_value = int(prediction[0])
    print("Prediction:", st.session_state.prediction_value)
    if st.session_state.prediction_value >= 40:
        st.success(f"Your mental health score is: {st.session_state.prediction_value}. You are likely to have a healthy mental state.")
    else:
        st.error(f"Your mental health score is: {st.session_state.prediction_value}. You may be at risk of mental health issues. Please consider seeking professional help.")

if st.session_state.is_submitted:
    if st.button("Print"):
        summary = f"""User Input Summary:
        Age: {age}
        Gender: {gender}
        Daily Screen Time: {daily_screen_time_hours} hours
        Phone Usage: {phone_usage_hours} hours
        Laptop Usage: {laptop_usage_hours} hours
        Tablet Usage: {tablet_usage_hours} hours
        TV Usage: {tv_usage_hours} hours
        Social Media Usage: {social_media_hours} hours
        Work-related Hours: {work_related_hours} hours
        Entertainment Hours: {entertainment_hours} hours
        Gaming Hours: {gaming_hours} hours
        Sleep Duration: {sleep_duration_hours} hours
        Sleep Quality: {sleep_quality}
        Mood Rating: {mood_rating}
        Stress Level: {stress_level}
        Physical Activity (per week): {physical_activity_hours_per_week} hours
        Location: {location_type}
        Uses Wellness Apps: {uses_wellness_apps}
        Eats Healthy: {eats_healthy}
        Caffeine Intake: {caffeine_intake_mg_per_day} mg
        Weekly Anxiety Score: {weekly_anxiety_score}
        Weekly Depression Score: {weekly_depression_score}
        Mindfulness Minutes: {mindfulness_minutes_per_day} minutes

    Mental Health Score: {st.session_state.prediction_value}
        """
        st.text_area("Summary: ", summary, height=400)

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="mental_health_summary.txt",
            mime="text/plain"
        )



