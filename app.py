import streamlit as st

from streamlit_option_menu import option_menu
from PIL import Image
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Prediction','Settings','About Us'],
        icons=['house','book','gear','envelope'],
        styles={
            "container":{"background-color":"#FFB5DA"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#facf7d",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#fedc57"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:#1693a7;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE PARKINSONS DISEASE PREDICTION SYSTEM </p>',unsafe_allow_html=True)
    file_=open("parkinsons3.png","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="700" image-align="center"  alt="Heart gif">',
        unsafe_allow_html=True, )

    st.markdown("""
    <style>
    . paragraph {
        font-size:20px !important;
        text-align: justify;
        }
    </style>
        """, unsafe_allow_html=True)

    st.markdown(' <p class="paragraph"> Parkinsons disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement. </p>',
    unsafe_allow_html=True)



if selected=='Prediction':
    image=Image.open('parkinsons.png')
    
    st.image(image,width=200,use_column_width=True)

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('model.pkl','rb'))

    def parkinson_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
            return 'Person Dont Have Parkinson Disease'
        else:
            return 'Person Have Parkinson Disease'
    def main(): 

    # giving title 
        #st.title('PARKINSONS DISEASE PREDICTION SYSTEM')
        st.markdown("<h1 style='text-align: center; color: #1693a7;'>PARKINSONS DISEASE PREDICTION SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,col3,col4=st.columns(4)


        with co1:
            PPE= st.number_input('Enter PPE Value',min_value=0.00000,step=0.01)
            MDVP_APQ=st.number_input('Enter MDVP_APQ Value',min_value=0.00000)
            spread2=st.number_input('Enter Spread2 Value:',min_value=0.00000) 
        with col2:
            
            MDVP_Fhi_Hz=st.number_input('Enter MDVP Fhi in Hz Value:',min_value=0.00000)
            MDVP_Fo_Hz=st.number_input('Enter MDVP Fo in Hz Value:',min_value=0.00000)
            Shimmer_APQ_5=st.number_input('Enter Shimmer APQ 5 Value:',min_value=0.00000)
        with col3:
            Jitter_DDP=st.number_input('Enter Jitter DDP Value:',min_value=0.00000)
            RPDE=st.number_input('Enter RPDE Value:',min_value=0.00000)
    
        #code for the prediction 
    
        prediction=''
    
    
        #creating a button for prediction 
        if st.button('Prediction Result'):
            prediction = parkinson_prediction([PPE,MDVP_APQ,spread2,MDVP_Fhi_Hz,MDVP_Fo_Hz,Shimmer_APQ_5,Jitter_DDP,RPDE])
            st.success(prediction)
    

    
    if __name__ =='__main__':
        main()

if selected=='Settings':
    st.subheader('To Run This Project you need the Streamlit Environment and Required Libraries')
    st.subheader('Open Streamlit CMD and Type Command "streamlit run app.py"')
    st.subheader('A web application will get open in the default browser')

if selected=='About Us':


    st.markdown("""
<div style="text-align: justify;">
Parkinson's disease prediction using machine learning involves analyzing medical data to identify patterns indicative of the disease, enabling early and accurate diagnosis. Key features include motor and non-motor symptoms, with data sourced from voice recordings, handwriting samples, and clinical assessments. Machine learning algorithms like Support Vector Machines, Random Forests, and Neural Networks are employed, with feature selection techniques enhancing model performance. The models are evaluated using metrics such as accuracy, precision, recall, and AUC-ROC. Early detection facilitated by these models can lead to timely interventions and personalized treatment plans, improving patient outcomes. Challenges include ensuring data quality, model generalization, and addressing ethical considerations like patient privacy and data security.
</div>
""", unsafe_allow_html=True)
