import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px

#titles
st.title("Supermarket Grocery sales")
st.sidebar.title('Slicers')

#filelocation
DATA_URL= 'Supermart Grocery Sales - Retail Analytics Dataset.csv'

df = pd.read_csv(DATA_URL)
city = df['City'].unique()

selected_states = st.sidebar.selectbox('Select City',options = city,key =1)

city_df = df[(df['City'] == selected_states)]

#CategoryWiseSales
city_sales = (city_df.groupby(['Category'], group_keys=True, axis=0, as_index=True)['Sales']
    .sum()
    .reset_index()
    .rename(columns={"Category":"Category","Sales": "Sales"})
    )


city_df['year'] = pd.DatetimeIndex(city_df['Order Date']).year
city_df['month'] = pd.DatetimeIndex(city_df['Order Date']).month


year_sales_df = city_sales

#visualization
select= st.sidebar.selectbox('Visualization',['Bar Graph','Pi Chart'], key=2)


st.markdown('### Sales by Category')
if select=='Bar Graph':
	fig=px.bar(city_sales, x='Category',y='Sales',color='Sales',height=500, text_auto = True)
	st.plotly_chart(fig)

else:
	fig=px.pie(city_sales, values='Sales', names='Category')
	st.plotly_chart(fig)

st.markdown('### Details')
st.dataframe(city_df)

