import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
import plotly.express as px

#set page wide
st.set_page_config(page_title="Retail Shopping", page_icon="img/icon.png")
#st.set_page_config(page_title="Retail Shopping", page_icon="img/icon.png")

menu = ['Introduction', 'Classfication Model']
choice = st.sidebar.selectbox("Menu", menu)

if choice == menu[0]:

    st.header("Customer Segmentation with RFM")
    st.image('img/68747470733a2f2f6269742e6c792f33617443617046.jfif', width=600)

    st.markdown("### Context")
    st.write('At here applied customer segmentation base on RFM. The data was collected from an online retail shop '
             'The data has bend collected for one years from 2010-2011, about all the invoices that the store had '
             'posted.')

    st.write("Here is what the data looks like. Because it's huge about (0.5M records) so I only show a small pieces "
             "of it.")
    data = pd.read_csv('OnlineRetail.csv', encoding='unicode_escape').head(100)
    st.write(data)

    st.markdown("")
    st.markdown("")
    report = pd.read_csv('data/ReportCustomerLabels.csv')
    st.markdown(
        "##### After applied algorithm, customers in data divided in five groups as the table shows bellow.")
    st.write(report)
    st.markdown(
        "##### The bellow graph will show clearer about how algorithm cut data into segments")

    fig = px.scatter(report, x="Recency Mean", size="Monetary Mean", y="Frequency Mean", color="labels",
                     hover_name="labels", size_max=150, height=650, log_x=True, width=900)

    st.plotly_chart(fig)


elif choice == menu[1]:
    
    
    # Init labels cluster
    labels = {
        2: 'GONE',
        4: 'LIKELY GONE',
        3: 'HOT',
        1: 'PROSPECTIVE',
        0: 'NEW'
    }
    # Load strategy
    strategy = pd.read_csv('data/strategy.csv')
    report = pd.read_csv('data/ReportCustomerLabels.csv')

    # Load model
    model = pickle.load(open('model/classification_pipeline.pkl', 'rb'))

    # Init layout for user to predict
    st.sidebar.markdown("#### Input data")
   
    
    
    
    recency_input = st.sidebar.number_input("Recency", min_value=0, max_value=450, value=10)
    st.sidebar.markdown("###### Recency: Total day has passed since customer bought something")
    frequency_input = st.sidebar.number_input("Frequency", min_value=1, max_value=1000, step=1, value=1)
    st.sidebar.markdown("###### Frequency: The number of time that customer bought something")
    monetary_input = st.sidebar.number_input("Monetary", min_value=50, max_value=500000, step=100, value=500)
    st.sidebar.markdown("###### Monetary: Total money that customer has spent ($)")

    
    # Get input into a data frame and print it out
    data_input = pd.DataFrame([[recency_input, frequency_input, monetary_input]],
                              columns=['recency', 'frequency', 'monetary'])
    
    #Divided layout
    new_cols = st.columns([4])
    
    
    #Print input data
    new_cols[0].write("Customer input data")
    new_cols[0].dataframe(data_input)

    # Predict customer label and print it out
    pred_label = model.predict(data_input)[0]
    
    new_cols[0].write("Predict label")
    new_cols[0].write(report.loc[report['labels'] == labels[pred_label], ['labels','Recency Mean', 'Frequency Mean', 'Monetary Mean']])
    
    #Print out recommendation along with labels
    new_cols[0].write("Recommendation action")
    new_cols[0].write(str(strategy.loc[strategy['labels'] == labels[pred_label], 'Recomendation Action'].values[0]))

    # # Print out graph for easier compare
    fig = px.scatter(report, x="Recency Mean", size="Monetary Mean", y="Frequency Mean", color="labels",
                     hover_name="labels", size_max=150, height=650, log_x=True, width=900, title="Customer Segmentation Map")

    new_cols[0].plotly_chart(fig)
