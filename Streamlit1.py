import streamlit as st
import joblib
from PIL import Image
def main():
    
    html_temp="""
    <div style="background-color:lightgreen;padding:20px;border-radius:10px;border-left:5px solid red;border-right:5px solid red">
    <h2 style="color:black;text-align:center">Customer Segmentation Model</h2>
    </div>
    <br>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model=joblib.load('Customer Segmentation')
    
    p1=st.slider('Enter Your Annual Income In ($)',10,100)
    p2=st.slider('Enter Your Spending Score ',0,100)
    

    image = Image.open('https://ibb.co/rv9yFKm')
    st.image(image, caption='This is The Spending Habit. You can See Yours')
    
    if st.button('Predict'):
        pred=model.predict([[p1,p2]])
        st.success('You Lie In Cluster Or Group {}'.format(pred[0]))

if __name__=='__main__':
    main()
