import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Data Analysis Dashboard')

# Sidebar for navigation
st.sidebar.title('Navigation')
options = st.sidebar.selectbox('Choose a section', ['Home', 'Upload Data', 'Data Overview', 'Visualizations', 'Data Filtering'])

# Home section
if options == 'Home':
    st.write('Welcome to the Data Analysis Dashboard!')
    st.write('Use the sidebar to navigate through different sections of the app.')

# File upload section
if options == 'Upload Data':
    st.subheader('Upload a CSV File')
    uploaded_file = st.file_uploader("Choose a file", type="csv")

    if uploaded_file is not None:
        # Read the data into a DataFrame
        df = pd.read_csv(uploaded_file)
        st.write(f'Dataframe shape: {df.shape}')
        st.dataframe(df.head())

        # Store data for later use in session state
        st.session_state['df'] = df

# Data Overview section
if options == 'Data Overview' and 'df' in st.session_state:
    st.subheader('Data Overview')

    df = st.session_state['df']
    st.write('Basic Statistics')
    st.write(df.describe())

    st.write('Columns Info')
    st.write(df.dtypes)

    st.write('Null Values in Data')
    st.write(df.isnull().sum())

# Visualizations section
if options == 'Visualizations' and 'df' in st.session_state:
    st.subheader('Data Visualizations')

    df = st.session_state['df']

    st.write('Correlation Heatmap')
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    st.pyplot(plt)

    st.write('Pairplot')
    sns.pairplot(df.dropna())
    st.pyplot(plt)

# Data Filtering section
if options == 'Data Filtering' and 'df' in st.session_state:
    st.subheader('Data Filtering')

    df = st.session_state['df']
    
    st.write('Filter by Column')
    column_to_filter = st.selectbox('Choose a column to filter by:', df.columns)
    
    if df[column_to_filter].dtype == 'object':
        unique_values = df[column_to_filter].unique()
        filter_value = st.selectbox('Choose a value:', unique_values)
        filtered_df = df[df[column_to_filter] == filter_value]
    else:
        min_value, max_value = int(df[column_to_filter].min()), int(df[column_to_filter].max())
        filter_value = st.slider(f'Select range for {column_to_filter}', min_value, max_value, (min_value, max_value))
        filtered_df = df[(df[column_to_filter] >= filter_value[0]) & (df[column_to_filter] <= filter_value[1])]

    st.write('Filtered Data')
    st.dataframe(filtered_df)

    st.write(f'Shape of filtered data: {filtered_df.shape}')

# If no data has been uploaded
if options != 'Home' and 'df' not in st.session_state:
    st.write('Please upload data to proceed!')
