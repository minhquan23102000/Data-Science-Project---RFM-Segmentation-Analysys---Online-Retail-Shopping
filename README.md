# Data-Science-Project---RFM-Segmentation-Analysys---Online-Retail-Shopping

In this project, I apply RFM Segmentation Clustering on customers in a online retail shopping to 5 type of customer. After i also build a classfication model, to predict customer is in which type of customer.

Reading notebook at the link below, to view full notebook's content:
https://nbviewer.org/github/minhquan23102000/Data-Science-Project---RFM-Segmentation-Analysys---Online-Retail-Shopping/blob/master/notebooks/RFM_ClusteringAnalysis.ipynb


## Deployment
Application made with streamlit is available on heroku via this link: https://segmentation-retail-store.herokuapp.com/


#### -- Project Status: [Completed]

## Project Intro/Objective
Company X specially sell their products as a present of the customer in holiday. Many customer of the company are wholesalers.
Now, company X wants to make more profit in their business and has more customers. In order to do that, they want to know each type of customers and the strategy to approach them.
Apply a clustiner algorithm to identify customer in the company. Base one that recommend action for each of them.


### Methods Used
* Inferential, Descriptive Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
* Big data preprocessing
* RFM analysys
* Web development framework (Streamlit)
* Web deploy

### Technologies
* Spark
* Pandas, numpy
* Matplotlib, seaborns, plotly
* Scikit-learn
* Streamlit


## Project Description
The data is put in a file name OnlineRetail.csv with total 541.909 records, from 01/12/2010 to 09/12/2011, as online retail invoices.

1. InvoiceNo:  Number of the Invoice, max length is 6, if has "C" in the series, that mean the invoice is cancelled
2. StockCode:  Id of the product
3. Description: Description of the product
4. Quantity: Number of items bought
5. InvoiceDate: The date of the invoice is created.
6. UnitPrice: Price of the product
7. CustomerID: Customer id
8. Country: Customer's country.

Because the data is a litle big, so I applied spark (big data preprocessing) to cleaning the data. You can view the script at the link bellow:
 <a href="https://github.com/minhquan23102000/Data-Science-Project---RFM-Segmentation-Analysys---Online-Retail-Shopping/blob/master/notebooks/PreprocessingData.ipynb"> Preprocessing script </a>

After the preprocessing step, we have the clean data at 'RFM_OnlineRetail.csv'

In deep of data exploration, i realize some insight the behaviour of customers, like they usually spend their lunch time to buy things, they bought mostly in November or on Friday. Also i have clustering them into group of customer base on their behaivours (volume, rencency, frequency).



## Contact
* My email: minhquan23102000@gmail.com
