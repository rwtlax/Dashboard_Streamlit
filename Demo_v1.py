from operator import truediv
import streamlit as st
import pandas as pd
import plotly.graph_objects as plt
import plotly.express as px

st.title("Supermaket Grocery sales")
url = 'Supermart Grocery Sales - Retail Analytics Dataset.csv'

df = pd.read_csv(url)
city = df['City'].unique()
selected_states = st.sidebar.selectbox('Select City',
                                       options = city)

city_df = df[(df['City'] == selected_states)]

city_sales = (city_df.groupby(['Category'], group_keys=True, axis=0, as_index=True)['Sales']
    .sum()
    .reset_index()
    .rename(columns={"Category":"Category","Sales": "Sales"})
    )

year_sales_df = city_sales

##year_sales_df['Year'] = pd.DatetimeIndex(year_sales_df['Order Date']).year

##fig = plt.Figure()

fig1 = plt.Figure(data=[plt.Table(
    header=dict(values=list(city_sales.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[city_sales.Category, city_sales.Sales],
               fill_color='lavender',
               align='left'))
])

st.plotly_chart(fig1, use_container_width =  True)

fig = px.bar(city_sales, x = 'Category', y ='Sales' , text_auto = True)

st.plotly_chart(fig, use_container_width =  True)


