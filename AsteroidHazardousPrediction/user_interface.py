import joblib
import pandas as pd
import streamlit as st

st.title("Asteroid Hazardous Prediction")

AbsoluteMagnitude = st.number_input("Enter Absolute Magnitude:")
RelativeVelocitykmperhr = st.number_input("Enter Relative Velocity km per hr:")
OrbitUncertainity = st.number_input("Enter Orbit Uncertainity:")
MinimumOrbitIntersection = st.number_input("Enter your Minimum Orbit Intersection:")
PerihelionDistance = st.number_input("Enter Perihelion Distance:")

user_input = pd.DataFrame([[AbsoluteMagnitude, RelativeVelocitykmperhr, OrbitUncertainity, MinimumOrbitIntersection, PerihelionDistance]], columns=['Absolute Magnitude', 'Relative Velocity km per hr', 'Orbit Uncertainity', 'Minimum Orbit Intersection', 'Perihelion Distance'])
model = joblib.load('hmodel.pkl')

prediction = model.predict(user_input)

if st.button("Predict"):
    if prediction[0]==0:
        st.write("The asteroid is Not Hazardous")
    else:
        st.write("The asteroid is Hazardous")

pd.show_versions()
