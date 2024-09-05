import streamlit as st
import numpy as np
import joblib

# Load the pre-trained decision tree model
model = joblib.load('decision_tree_model.joblib')

# Title of the dashboard
st.title("Student Performance Predictor")

st.write("Decision Tree Classifier Dashboard")

# Create the input fields
input_data = []

field_names = ['Class','Age','Gender','Years in the School','Approx. Distance from your Hse. To Sch.(Km)','mode of transportation','Who do you stay with?','Average score Last term','Assignment Completion','Study Hours','Study Resources',  'How helpful are your teachers? ' ,'Do you attend extra classes' ,'What Helps you do better in School? ','Challenges in School']
#fields
class_ = st.number_input("Class", min_value=1, max_value=12, step=1)
input_data.append(class_)

age = st.number_input("Age", min_value=0, max_value=20, step=1)
input_data.append(age)

# Gender field (using selectbox to show 'Male' and 'Female')
gender = st.selectbox("Gender", options=["Male", "Female"])
gender_value = 1 if gender == "Male" else 0
input_data.append(gender_value)


years_in_school = st.number_input("Years in School", min_value=0, max_value=10, step=1)
input_data.append(years_in_school)

distance = st.number_input("Approx. Distance from your Hse. To Sch.(Km)", min_value=0.0, max_value=15.0, step=0.1)
input_data.append(distance)

# Another gender-like input (just an example)
transportation_mode = st.selectbox("Mode of Transportation", options=["Walking", "Public Transport", "School Bus", "Private Car"])
# Encode the options as integers
transportation_value = {
    "Walking": 1,
    "Public Transport": 2,
    "School Bus": 3,
    "Private Car": 4
}[transportation_mode]
input_data.append(transportation_value)

gurdian = st.selectbox("Who do you stay with?", options=["Mother", "Father", "Both Parents", "Siblings"])
# Encode the options as integers
gurdian_value = {
    "Mother": 1,
    "Father": 2,
    "Both Parents": 3,
    "Siblings": 4
}[gurdian]
input_data.append(gurdian_value)

average_score = st.number_input("Average score Last term", min_value=0, max_value=100, step=1)
input_data.append(average_score)

assignment_complete = st.selectbox("Do you complete your assignments/.", options=["Always", "Most at Times", "Somtimes", "Rarely"])
# Encode the options as integers
assignment_complete_value = {
    "Always": 1,
    "Most at times": 2,
    "Sometimes": 3,
    "Rarely": 4
}[assignment_complete]
input_data.append(assignment_complete_value)


hours_of_study = st.selectbox("Study Hours", options=["Less than 2 hours", "2 - 3 hours", "Above 3 hours"])
# Encode the options as integers
hours_of_study_value = {
    "Less than 2 hours": 1,
    "2 - 3 hours": 2,
    "Above 3 hours": 3
}[hours_of_study]
input_data.append(hours_of_study_value)


study_resources = st.selectbox("Which Resource do you use to study", options=["Computer", "Mobile Phone"])
# Encode the options as integers
study_resources_value = {
    "Computer": 1,
    "Mobile Phone": 2,
}[study_resources]
input_data.append(study_resources_value)

helpful_teachers = st.selectbox("How supportive are your teachers?", options=["Very Supportive", "Okay"])
# Encode the options as integers
helpful_teachers_value = {
    "Very Supportive": 1,
    "Okay": 2,
}[helpful_teachers]
input_data.append(helpful_teachers_value)


extra_classes = st.selectbox("Do you attend extra classes?", options=["Yes", "No"])
# Encode the options as integers
extra_classes_value = {
    "Yes": 1,
    "No": 2,
}[extra_classes]
input_data.append(extra_classes_value)

performance = st.selectbox("What Helps you do better in School?", options=["Paying attention in class", "Doing homework on time", 'Staying organized with notes assignments', 'Practicing tough subjects often', 'Setting personal Goals for improvement', 'Studying regularly, not just before exams'])
# Encode the options as integers
performance_value = {
    "Paying attention in class": 1,
    "Doing homework on time": 2,
    "Staying organized with notes assignments": 3,
    "Practicing tough subjects often": 4,
    "Setting personal Goals for improvement": 5,
    "Studying regularly, not just before exams": 6,
}[performance]
input_data.append(performance_value)

challenges = st.selectbox("What are your challenges in School?", options=["Yes", "No"])
# Encode the options as integers
challenges_value = {
    "Yes": 1,
    "No": 2,
}[challenges]
input_data.append(challenges_value)


# Convert the input data to a numpy array
input_data = np.array(input_data).reshape(1, -1)

class_names = [
    'Excellent',
    'Very Good',
    'Good',
    'Below average'
]

# Classify the input data when the button is clicked
if st.button("Classify"):
    prediction = model.predict(input_data)
    st.write(f"The predicted class is: {prediction[0]}")
    st.write(f"The predicted class is: {class_names[prediction[0]]}")

