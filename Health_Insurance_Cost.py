# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:16:19 2023

@author: sohan
"""

import streamlit as st
import numpy as np
import joblib

def main():
    html_temp = """
  <div style="background-color:lightblue;padding:16px">
  <h2 style="color:black";text-align:center> Health Insurance Cost Prediction Using ML</h2>
  </div>
  
  """
    st.markdown(html_temp,unsafe_allow_html=True)
    model=joblib.load('insurance_model')
   
    p1=st.slider('Enter your Age',18,100)
   
    s1=st.selectbox('Sex',('Male','Female'))
    if s1=='Male':
       p2=1
    else:
       p2=0
       
    p3=st.number_input('Enter your BMI value')

    p4=st.slider('Enter number of children',0,4)
   
    s2=st.selectbox('Smoker',('Yes','No'))
    if s2=='Yes':
       p5=1
    else:
       p5=0
   
     
    p6=st.slider('Enter your region',0,3)
   
    if st.button('Predict'):
       pred=model.predict([[p1,p2,p3,p4,p5,p6]])
       
       st.balloons()
       
       st.success('Your insurance cost is{}'.format(round(pred[0],2)))
          

if __name__=='__main__':
    main()
           