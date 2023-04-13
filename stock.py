import pandas as pd
import numpy as np
import streamlit as st
#import datetime as dt
import time as t

#setting icon and name for the webpage.
st.set_page_config (page_title='Stock App',page_icon='st.ico',layout="wide",initial_sidebar_state="expanded")

#data in csv file
A_data=pd.read_csv('Amazon.csv',index_col=0)
N_data=pd.read_csv('NFLX.csv',index_col=0)
T_data=pd.read_csv('tesla.csv',index_col=0)

#creating dataframe for the taken csv files
df1=pd.DataFrame(A_data)
df2=pd.DataFrame(N_data)
df3=pd.DataFrame(T_data)



st.markdown('''
# Stock Price App

###### This is a simple normal stock price app which is made with `streamlit`and`pandas`

- Easy to understand stocks

Data collected from the [kaggle](https://www.kaggle.com/datasets)

1.Amazon stock price

2.Netflix stock price

3.Tesla stock price
''')

'---'




#creating the sidebar for stocks
st.sidebar.markdown('''# :violet[**SIDE BAR**]''')
opt=st.sidebar.selectbox('**Companies**',options=('AMZON','NFLX','TESLA'))
if opt=='AMZON':
    with st.spinner('Loading'):
       t.sleep(0.3)
    st.balloons()
    st.image('mazon.png')
    st.markdown(opt)
    st.info('''All time Stock price of Amazon(1197-2022)''',icon='👉')
    st.experimental_data_editor(df1,num_rows='dynamic')
    st.line_chart(df1)
    st.success('Success!')

elif opt=="NFLX":
    with st.spinner('Loading'):
       t.sleep(0.3)
    st.image('netflix.png')
    st.write(opt)
    st.info('''Netflix stock price between (2015-2019)''',icon='👉')
    st.experimental_data_editor(df2,num_rows='dynamic')
    st.line_chart(df2)
    st.success('Success!')

elif opt=='TESLA':
    with st.spinner('Loading'):
       t.sleep(0.3)
    st.image('tesla.png')
    st.write(opt)
    st.info('''Tesla stock price between(2010-2017)''',icon='👉')
    st.experimental_data_editor(df3,num_rows='dynamic')
    st.line_chart(df3)
    st.success('Success!')

else:
    pass
