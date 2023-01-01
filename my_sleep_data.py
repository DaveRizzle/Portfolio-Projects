import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('cleaned_sleep_data_all.csv')

# Reset the index to the Date column. 
df['date'] = pd.to_datetime(df['date'],format='%Y/%m/%d')
df.reset_index(drop=True,inplace=True)
df.set_index('date',inplace=True)

st.set_page_config(page_title='Dave\'s Sleep Data', 
page_icon='', layout="wide")

# Add social media tags and links to the web page.
"""
[![Star](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@david-robertson67/)
[![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/david-robertson11/)

# Deep Sleep Continuity

"""

# Add a sidebar to the web page. 
st.markdown('---')
# Sidebar Configuration
st.sidebar.image('https://lh3.googleusercontent.com/a/AEdFTp6VbOY8XKfxjAV2eTxdjHCYQQB_5wb8WonEI1RsgA=s576-p-rw-no', width=200)
st.sidebar.markdown('# My Sleep Dashboard')
st.sidebar.markdown('Measuring Deep Sleep Continuity Across Time')
st.sidebar.markdown('Sleep Data: 2020 - 2022')
st.sidebar.markdown('Assessing Trends and Patterns over a given time span.') 

st.sidebar.markdown('---')
st.sidebar.write('Developed by Dave Robertson')
st.sidebar.write('Contact at david.robertson67@gmail.com')

# Display the Data in the App.
st.subheader('Looking at the Data')
st.dataframe(df.head())
# Display statistical information on the dataset.
st.subheader('Statistical Info about the Data')
st.write(df.describe())

# Selection for a specific time frame.
st.subheader('Select a Date Range')
df_select = df 

col1, col2 = st.columns(2)

with col1:
    st.write('Select a Start Date')
    start_date = st.date_input('Start Date',min_value= datetime.date(2020,7,12),max_value=datetime.date(2022,10,20),value=datetime.date(2020,7,12))

with col2:    
    st.write('Select an End Date')
    end_date = st.date_input('End Date',min_value=datetime.date(2020,7,12),max_value=datetime.date(2022,10,20),value=datetime.date(2022,10,20))

if(start_date != None or end_date != None):
    if(start_date < end_date):
        df_select = df[start_date:end_date]
    else:
        st.warning("Invalid Date Range - Re-enter Dates")

# Deep vs Light Sleep 
st.subheader("Light and Deep Sleep Comparison")
st.markdown("\n\n")
st.line_chart(df_select[['light_sleep_perc','deep_sleep_perc']])


# REM vs Light Sleep 
st.subheader("REM and Light Sleep Comparison")
st.markdown("\n\n")
st.line_chart(df_select[['rem_sleep_perc','light_sleep_perc']])

st.subheader("Total Times Woke Up")
st.markdown("\n\n")
st.line_chart(df_select[['times_woke_up']])

# Moving average from 50 days to 730 days.
st.subheader("Moving Average of Times Woke Up")
movevavg_len = st.slider('Select the number of days for Moving Averages',min_value=0,max_value=6,value=730)
moveavg_oc = df_select[['deep_sleep_perc','light_sleep_perc', 'rem_sleep_perc', 'times_woke_up_perc']].rolling(50).mean()
st.line_chart(moveavg_oc)
