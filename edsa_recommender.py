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

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
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
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "About Us":

        st.markdown("<h2 style='text-align: left; color: white;'>About The Team</h2>", unsafe_allow_html=True)


        team_img, team_info = st.columns((1,3))

        with team_img:
            st.image('resources/images/team.jpeg')
        with team_info:
            st.write(
                """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                et dolore magna aliqua. 
                
                
                Proin nibh nisl condimentum id venenatis a condimentum. Eu nisl nunc mi
                ipsum. Pellentesque habitant morbi tristique senectus et. Vitae tortor condimentum lacinia quis
                vel eros donec. Tristique nulla aliquet enim 
                """
            )	


        st.markdown("<h2 style='text-align: center; color: orange;'>About The Platform</h2>", unsafe_allow_html=True)

        # st.write("##")

        project_info, project_img = st.columns((2,1))

        with project_info:
            st.write(
                """

                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt


                ut labore et dolore magna aliqua. Proin nibh nisl condimentum id venenatis a condimentum.
                Eu nisl nunc mi ipsum. Pellentesque habitant morbi tristique senectus et. Vitae tortor condimentum 
                 


                quis vel eros donec ac odio. Pretium lectus quam id leo in vitae. Egestas maecenas pharetra convallis
                posuere. Tempor id eu nisl nunc mi. Vel turpis nunc eget lorem dolor sed viverra ipsum nunc. Nunc mi
                ipsum faucibus vitae aliquet. Porttitor lacus luctus accumsan tortor posuere ac. Interdum
                consectetur libero id faucibus nisl tincidunt. Lacinia quis vel eros donec ac odio.

                Libero volutpat sed cras ornare arcu dui vivamus. Erat velit scelerisque in dictum non.
                Mattis molestie a iaculis at erat pellentesque adipiscing commodo. Quis imperdiet massa
                tincidunt nunc pulvinar sapien et ligula. Tellus rutrum tellus pellentesque eu tincidunt
                tortor aliquam nulla. Interdum posuere lorem ipsum dolor sit amet consectetur adipiscing
                elit. At elementum eu facilisis sed odio morbi. Vitae purus faucibus ornare suspendisse
                sed nisi lacus sed. Ut sem nulla pharetra diam sit amet nisl.

                """
            )		

        with project_img:
            st.image('resources/images/GM1_img.png')
            st.image('resources/images/GM1_img.png')

    if page_selection == "Information":


        st.markdown("<h1 style='text-align: centre; color: orange;'>Data Collection</h1>", unsafe_allow_html=True)
        collection_text, collection_img = st.columns((2,1))
        with collection_text:
            st.write(
                """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                dolore magna aliqua. Eu turpis egestas pretium aenean pharetra magna ac placerat vestibulum. Ut ornare
                lectus sit amet est placerat in egestas erat. Ultrices gravida dictum fusce ut placerat orci
                nulla pellentesque. Non sodales neque sodales ut etiam sit. 
                Pellentesque elit eget gravida cum

                
                """
            )
        with collection_img:
            st.image('resources/images/kaggle1.jpg')
        st.markdown("<h1 style='text-align: right; color: white;'>Recommender Engines</h1>", unsafe_allow_html=True)

        st.write(
                """
                 lectus sit amet est placerat in egestas erat. Ultrices gravida dictum fusce ut placerat orci
                nulla pellentesque.
                """
            )

        data_clean1, data_clean2 = st.columns((1, 1))
        with data_clean1:
            st.image('resources/images/recommend.jfif')
        with data_clean2:
            st.markdown("<h2 style='text-align: center; color: black;'>Recommender types</h2>", unsafe_allow_html=True)
            st.write("""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                dolore magna aliqua. Eu turpis egestas pretium aenean pharetra magna ac placerat vestibulum. Ut ornare
                lectus sit amet est placerat in egestas erat. Ultrices gravida dictum fusce ut placerat orci
                """)

        st.markdown("<h2 style='text-align: center; color: orange;'>Uses and Benefits</h2>", unsafe_allow_html=True) 

        st.markdown("<p style='color: white'> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore etdolore magna aliqua. Eu turpis egestas pretium aenean pharetra magna ac placerat vestibulum. Ut ornarelectus sit a</p>", unsafe_allow_html=True)              	    			

        st.write("""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                dolore magna aliqua. Eu turpis egestas pretium aenean pharetra magna ac placerat vestibulum. Ut ornare
                lectus sit amet est placerat in egestas erat. Ultrices gravida dictum fusce ut placerat orci
                """) 

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
