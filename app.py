import streamlit as st
import numpy as np
import pickle


#Importing our pickle file
model = pickle.load(open('model1.pkl', 'rb'))

#Title of app
st.title('Predicted price of car')

#Range of paramenters
#Price	Kilometer	Fuel Type	Transmission	Owners Before	Engine	Fuel Tank Capacity	Age
Kilometer = st.slider("Kilometer",7.500000e+01,2.000000e+06)
Fuel_Type = st.slider("Fuel Type",0.000000,1.000000)
Transmission = st.slider("Transmission",0.000000,1.000000)
Owners = st.slider("Owners Before",0.000000,4.000000)
Engine = st.slider("Engine",624.000000,6592.000000)
Fuel = st.slider("Fuel Tank Capacity",15.000000,105.000000)
Age = st.slider("Age",1.000000,35.000000)

#Pridiction function
def predict():
    float_features = [float(x) for x in [Kilometer,Fuel_Type,Transmission,Owners,Engine,Fuel,Age]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)

#Printing the output 
    st.success('The car price is : ' + str(label) + ' :thumbsup:')
trigger = st.button('Predict', on_click=predict)

