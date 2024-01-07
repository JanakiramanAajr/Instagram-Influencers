import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide", page_icon=Image.open(r"D:\Insta Influence\Insta_Influence.jpeg"),
                   page_title="Instagram Influencers Analysis")
selected = option_menu(None, ["Home", "Visualization", "About"], icons=["house", "pencil-square ",
                                                                                            "gear"],default_index=0,
styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"}})
# Selecting Home Menu
if selected == 'Home':
    # Open the image
    image = Image.open(r"D:\Insta Influence\Insta_Influence.jpeg")

    # Resize the image to the desired dimensions
    new_width = 300  # Set your desired width
    new_height = 200  # Set your desired height
    resized_image = image.resize((new_width, new_height))
    # Display the resized image
    st.image(resized_image, caption="Instagram Influences Analysis")
if selected == 'Visualization':
    tabi, tabii, tabiii, tabiv, tabv = st.tabs(['Correlation','Frequency distribution for Influence Score',"Influences Distribution",'Top 10 Influences','Relationship Analysis'])
    with open(r"D:\Insta Influence\data.pkl", 'rb') as file:
        loaded_data = pickle.load(file)
    df = pd.DataFrame(loaded_data)

    with tabi:
        st.subheader('Correlation Matrices\nEnter the Correlation Button')
        correlation_matrix = df.corr()
        # Create Matplotlib figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))
        # Plot heatmap
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5, ax=ax)
        # Display the Matplotlib figure in Streamlit
        st.pyplot(fig)
    with tabii:
        tab1, tab2, tab3 = st.tabs(['Influence Score','Followers','Posts'])
        with tab1:
            col1,col2,col3 = st.columns(3)
            with col1:
                # Frequency distribution for Influence Score
                plt.figure(figsize=(5, 3))
                plt.hist(df['Influence Score'], bins=20, color='blue', edgecolor='black')
                plt.title('Influence Score Frequency Distribution')
                plt.xlabel('Influence Score')
                plt.ylabel('Frequency')
                # a = plt.show()
                st.pyplot(plt)
        with tab2:
            col1, col2, col3 = st.columns(3)
            with col2:
                # Frequency distribution for Followers
                plt.figure(figsize=(5, 3))
                plt.hist(df['Followers'], bins=20, color='green', edgecolor='black')
                plt.title('Followers Frequency Distribution')
                plt.xlabel('Followers')
                plt.ylabel('Frequency')
                st.pyplot(plt)
        with tab3:
            col1, col2, col3 = st.columns(3)
            with col3:
                # Frequency distribution for Posts
                plt.figure(figsize=(5, 3))
                plt.hist(df['Posts'], bins=20, color='orange', edgecolor='black')
                plt.title('Posts Frequency Distribution')
                plt.xlabel('Number of Posts')
                plt.ylabel('Frequency')
                st.pyplot(plt)
    with tabiii:
        st.subheader('Number of Instagram Influencers in Different Countries')
        country_counts = df['Country Or Region'].value_counts()

        plt.figure(figsize=(5, 5))
        bar_plot = sns.barplot(y=country_counts.index, x=country_counts.values)
        # plt.yticks(rotation=0)
        plt.title('Number of Instagram Influencers in Different Countries')
        plt.ylabel('Country')
        plt.xlabel('Count')
        for index, value in enumerate(country_counts.values):
            bar_plot.text(value, index, str(value), ha='center', va='center')
        col1, col2, col3 = st.columns(3)
        with col2:
            st.pyplot(plt)
    with tabiv:
        tab1, tab2, tab3 = st.tabs(['Followers', 'Avg. Likes','Total Likes'])
        top_followers = df.nlargest(10, 'Followers')
        top_avg_likes = df.nlargest(10, 'Avg. Likes')
        top_total_likes = df.nlargest(10, 'Total Likes')

        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                # Plotting the results using bar charts
                fig, axes = plt.subplots(figsize=(5, 3))
                # Bar chart for top influencers based on Followers
                sns.barplot(x='Followers', y='Channel Info', data=top_followers, ax=axes)
                axes.set_title('Top 10 Influencers based on Followers')
                plt.tight_layout()
                st.pyplot(plt)
        with tab2:
            col1, col2, col3 = st.columns(3)
            with col2:
                # Plotting the results using bar charts
                fig, axes = plt.subplots(figsize=(5, 3))
                # Bar chart for top influencers based on Average Likes
                sns.barplot(x='Avg. Likes', y='Channel Info', data=top_avg_likes, ax=axes)
                axes.set_title('Top 10 Influencers based on Average Likes')
                plt.tight_layout()
                st.pyplot(plt)
        with tab3:
            col1, col2, col3 = st.columns(3)
            with col3:
                # Plotting the results using bar charts
                fig, axes = plt.subplots(figsize=(5, 3))
                # Bar chart for top influencers based on Total Likes
                sns.barplot(x='Total Likes', y='Channel Info', data=top_total_likes, ax=axes)
                axes.set_title('Top 10 Influencers based on Total Likes')
                st.pyplot(plt)
    with tabv:
        tab1, tab2, tab3,tab4 = st.tabs(['Followers vs Total Likes',
                                         'Followers vs Influence Score', 'Post vs Avg. Likes', 'Posts vs Average Likes'])
        with tab1:
            col1, col2, col3,col4 = st.columns(4)
            with col1:
                # Scatter plot for Followers and Total Likes
                plt.figure(figsize=(10, 6))
                plt.scatter(df['Followers'], df['Total Likes'], color='blue', alpha=0.5)
                plt.title('Followers vs Total Likes')
                plt.xlabel('Followers')
                plt.ylabel('Total Likes')
                st.pyplot(plt)
        with tab2:
            col1, col2, col3, col4 = st.columns(4)
            with col2:
                # Scatter plot for Followers and Influence Score
                plt.figure(figsize=(10, 6))
                plt.scatter(df['Followers'], df['Influence Score'], color='green', alpha=0.5)
                plt.title('Followers vs Influence Score')
                plt.xlabel('Followers')
                plt.ylabel('Influence Score')
                st.pyplot(plt)
        with tab3:
            col1, col2, col3, col4 = st.columns(4)
            with col3:
                # Scatter plot for Posts and Average Likes
                plt.figure(figsize=(10, 6))
                plt.scatter(df['Posts'], df['Avg. Likes'], color='orange', alpha=0.5)
                plt.title('Posts vs Average Likes')
                plt.xlabel('Number of Posts')
                plt.ylabel('Average Likes')
                st.pyplot(plt)
        with tab4:
            col1, col2, col3, col4 = st.columns(4)
            with col4:
                # Scatter plot for Posts and Influence Score
                plt.figure(figsize=(10, 6))
                plt.scatter(df['Posts'], df['Influence Score'], color='red', alpha=0.5)
                plt.title('Posts vs Influence Score')
                plt.xlabel('Number of Posts')
                plt.ylabel('Influence Score')
                st.pyplot(plt)









