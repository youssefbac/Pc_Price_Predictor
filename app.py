import streamlit as st
import pickle
import  numpy as np


pipe=pickle.load(open('pipe.pkl','rb'))
df= pickle.load(open('df.pkl','rb'))



st.title("PC Price Predictor ")
company= st.selectbox('Brand',df['Company'].unique())

type= st.selectbox('Type',df['TypeName'].unique())

Ram= st.selectbox('Ram',[2,4,6,8,12,16,24,32,64])

Weight= st.number_input('Laptop weight ')

touchscreen=st.selectbox('Touchscreen',['yes','no'])

#ips (in plane switching) type of screen
ips=st.selectbox('IPS',['yes','no'])

screen_size=st.number_input('Screen size')

screen_resolution=st.selectbox('screen Resolution',['1920x1080','1366x768'
'1600x900','3840x2160','3200x1800','2800x1800','2560x1600','2560x1440',
    '2304x1440'])

cpu= st.selectbox('CPU Brand',df['Cpu brand'].unique())

hdd= st.selectbox('HDD (GB)',[0,8,128,256,512,1024])
ssd= st.selectbox('SDD (GB)',[0,8,128,256,512,1024])
gpu= st.selectbox('GPU',df['Gpu Brand'].unique())

os= st.selectbox('Operating system',df['OS'].unique())


if st.button('Predict Price'):
    if touchscreen == 'yes':
        touchscreen =1
    else:
        touchscreen=0
    #ips
    if ips =='yes':
        ips=1
    else:
        ips=0
    X_res= int(screen_resolution.split('x')[0])
    Y_res= int(screen_resolution.split('x')[1])

    ## ppi (pixel per inches)
    ppi= (X_res**2) + (Y_res**2)**0.5/screen_size
    query=np.array([company,type,Ram,Weight,touchscreen,ips,ppi,cpu,hdd,ssd
                    ,gpu,os])
    #reshape query to 1 row and 12 columns
    query=query.reshape(1,12)
    st.title("The predicted price is of this PC configuration : "+str(int(np.exp(pipe.predict(query)[0]))))
