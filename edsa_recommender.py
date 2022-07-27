"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see
    
	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
from distutils.log import info
from nbformat import write
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    st.set_page_config(page_title="DEVIANTS", page_icon=":trident:")
    title_logo, title = st.columns((1,4))

    with title_logo:
        st.image("resources/images/GM1_logo.png")

    with title:
        st.title("""DEVIANTS MOVIE RECOMMENDER""")

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","About Us", "Information", "Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.radio("Choose Option", page_options)

    if page_selection == "Recommender System":
        # Header contents
        # st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.snow()
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "About Us":

        st.markdown("<h2 style='text-align: left; color: white;'>About The Team</h2>", unsafe_allow_html=True)


        team_img, team_info = st.columns((2,3))

        with team_img:
            st.image('resources/images/team.jpeg')
        with team_info:
            st.write(
                """
                Deviants: We are a team of Data Scientists that pride themselve in creating valuable insights 
                using data. After collecting data we take it through several Data Science techniques that enable us
                use to build and train Machine Learning models. We use these Models to provide valuable insights which is what is presented on this Movie
                Recommendation platform. 
                """
            )	

        st.markdown("<h2 style='text-align: center; color: orange;'>About The Platform</h2>", unsafe_allow_html=True)
        st.image('resources/images/recommender_bot.jpg')
        st.markdown("<p style='text-align: left; color: white;'>In today’s technology driven world, recommender systems are socially and economically critical to ensure that individuals can make optimised choices surrounding the content they engage with on a daily basis. One application where this is especially true is movie recommendations; where intelligent algorithms can help viewers find great titles from tens of thousands of options.</p>", unsafe_allow_html=True)
        st.write(
                """
                Our platform recommends ten movies depending on three movies a user chooses. These movies chosen either 
                based on the pool of similar movies(Content filtering) or data from other users with similar interests (Collaborative filtering).   
                """
            )
        
    if page_selection == "Information":


        st.markdown("<h2 style='text-align: centre; color: white;'>Data Processing</h2>", unsafe_allow_html=True)
        collection_text, collection_img = st.columns((2,1))
        with collection_text:
            st.write(
                    """
                    Data was collected from a very reliable Data Science platform named Kaggle. 
                    """
                )


            st.markdown("<p style='text-align: centre; color: white;'>This dataset consists of several million 5-star ratings obtained from users of the online MovieLens movierecommendation service. The MovieLens dataset has long been used by industry and academic researchers toimprove the performance of explicitly-based recommender systems. </p>", unsafe_allow_html=True)

            st.write( 
                    """   
                    The data for the MovieLens dataset is maintained by the GroupLens research group in the Department of
                    Computer Science and Engineering at the University of Minnesota. Additional movie content data was legally
                    scraped from IMDB.

                    """
                )

        with collection_img:
            st.image('resources/images/kaggle1.jpg')
            st.image('resources/images/imdb.jpg')


        st.markdown("<h2 style='text-align: center; color: white;'>Recommender Engines</h2>", unsafe_allow_html=True)

        st.write(
                """
                recommendation engine is essentially a solution that allows marketers to offer their customers relevant product
                recommendations in real-time.
                """
            )

        data_clean1, data_clean2 = st.columns((1, 1))
        with data_clean1:
            st.image('resources/images/recommend.jfif')
        with data_clean2:
            st.markdown("<h2 style='text-align: center; orange: white;'>Filtering tools</h2>", unsafe_allow_html=True)


            st.markdown("<p style='text-align: center; color: white;'>CONTENT-BASED filtering is a type of recommender system that attempts to guess what a user may like based onthat user's activity. Content-based filtering makes recommendations by using keywords and attributes assignedto objects in a database.</p>", unsafe_allow_html=True)
         

        filter0, filter1, filter2 = st.columns((1,4,2))

        with filter0:
                st.empty()        
        with filter1:
                st.write(
                        """
                        COLLABORATIVE filtering is a technique that can filter out items that a user might like on the basis of
                        reactions by similar users.
                        
                        It works by searching a large group of people and finding a smaller set
                        of users with tastes similar to a particular user.   
                        """
                )
        with filter2:
                st.image('resources/images/filtering.jpg')    

        st.markdown("<p style='color: white'> These powerful data filtering tools, recommendation systems use algorithms and data analysis techniques to recommend the most relevant product/items to a particular user. </p>", unsafe_allow_html=True)        

        st.markdown("<h2 style='text-align: center; color: orange;'>Uses and Benefits</h2>", unsafe_allow_html=True) 
        st.markdown("<p style='color: white'> Our platform can be used to  filter or predict the users' movie preferences based on their past choices or users with similar interests. This is beneficial since it ensures that users have the most relevant content suggested to them.</p>", unsafe_allow_html=True)              	    			

        st.markdown("<h3 style='text-align: left; color: orange;'>Other uses for recommenders</h3>", unsafe_allow_html=True) 
        st.image('resources/images/e-commerce.jpg')
      

        st.markdown("<h5 style='text-align: left; color: orange;'>Drive Traffic</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: right; color: white;'>Through personalized email messages and targeted blasts, a recommendation engine can encourage elevated amounts of traffic to your site, thus increasing the opportunity to scoop up more data to further enrich a customer profile.</p>", unsafe_allow_html=True)        
        
        st.markdown("<h5 style='text-align: center; color: orange;'>Increase Number of Items per Order</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; color: orange;'>In addition to the average order value rising, the number of items per order also typically rises when an engine is employed. When the customer is shown options that meet his or her interest, they are far more likely to add items to to their active purchase cart.</p>", unsafe_allow_html=True)        

        st.markdown("<h5 style='text-align: center; color: white;'>Offer Advice and Direction</h5>", unsafe_allow_html=True)
        other1, other2 = st.columns((1, 3))
        with other1:
            st.image('resources/images/bot.gif')
        with other2:
            st.markdown("<p style='text-align: center; color: white;'>An experienced recommendation provider like Kibo can offer advice on how to use the data collected from your recommendation engine. Acting as a partner and a consultant, the provider should have the industry know-how needed to help guide you and your ecommerce site to a prosperous future.</p>", unsafe_allow_html=True)        


        st.markdown("<h2 style='text-align: left; color: orange;'>For more information</h2>", unsafe_allow_html=True)

        info1, info2 = st.columns((4, 2)) 

        with info1:
            st.write("[Working and Advantages of a Recommendation Engine - Explained](https://medium.com/geekculture/explained-working-and-advantages-of-a-recommendation-engine-16cbff7796c)")
            st.write("[Benefits of Recommendation Systems](https://kibocommerce.com/blog/recommendation-engine-benefits-aov/)")
            st.write("[Streamlit](https://streamlit.io/)")
            st.write("[Amazon Webservices hosting](https://aws.amazon.com/)")
        with info2:    
            st.image('resources/images/plug1.gif')

    if page_selection == "Contact Us":

        st.markdown("<h2 style='text-align: left; color: white;'>Get in touch!</h2>", unsafe_allow_html=True)
        st.write("For feedback and improvement recommendations")

        contact_form ="""
			<form action="https://formsubmit.co/deviants42@gmail.com" method="POST">
    			 <input type="text" name="Message" placeholder="Your Message" required>
        		<input type="email" name="email" placeholder="Your email" required>
     			<button type="submit">Send</button>
				</form>
			"""

        local_css()
        st.markdown(contact_form, unsafe_allow_html=True)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


def local_css():
    with open('styles.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
