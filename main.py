import streamlit as st 
from googletrans import Translator, LANGUAGES
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import matplotlib.pyplot as plt
import os


def main(): 
    st.title("App")
    st.subheader("Switch between translation and sentimental analysis on the drop-down on the left\n")
    st.caption("Google Translate with Sentiment Analysis")
    activities=["Translator", "Sentimental Analysis"]
    choice=st.sidebar.selectbox("Select Activities", activities)

    #Translator Part
    if choice == "Translator": 
        list_text = list(LANGUAGES.values())
        st.write("\n")
        st.subheader("Translator")
        from_text = st.text_input("Enter Source Text: ")
        from_code = st.selectbox("Enter the Language: ", list_text)
       
        if st.button("Translate"):
            translator=Translator() 
            try:
                a=(translator.translate(from_text, dest=from_code).text)
                st.success(a)
            except Exception as e: 
                a1=os.system("ping www.google.com") 
                if a1==1: 
                    st.write("Please Check Your Internet Connection.")
                else: 
                    st.write("Language Input not Recognized.")
    
    #Sentimental Analysis Part
    elif choice == "Sentimental Analysis": 
        st.write("\n")
        st.write("\n")
        st.subheader("Sentiment Analyzer")

        from_sent = st.text_input("Enter a Sentence: ")
        if st.button("Check Sentiment"): 
            try:
                obj = SentimentIntensityAnalyzer()
                sentiment_dict = obj.polarity_scores(from_sent)

                labels = ['Negative', 'Neutral', 'Positive']
                sizes  = [sentiment_dict['neg'], sentiment_dict['neu'], sentiment_dict['pos']]
                explode = (0.1, 0, 0.1)
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90) # autopct='%1.1f%%' gives you percentages printed in every slice.
                ax.axis('equal')  # Ensures that pie is drawn as a circle.
                st.pyplot(fig)

                st.write(sentiment_dict) 
                st.write("Sentence is rated as ", sentiment_dict['neg']*100, "% Negative")
                st.write("Sentence is rated as ", sentiment_dict['neu']*100, "% Neutral")
                st.write("Sentence is rated as ", sentiment_dict['pos']*100, "% Positive")

                st.write("\n" )
                st.write("\n" )

                st.write("Sentence gives a: " )

                #Shows if sentiment is good, bad, or neutral
                if sentiment_dict['compound'] >= 0.05 : 
                    st.success("Positive Statement")
                    st.info("A **''sentiment''** is an attitude or emotion towards something, and can be determined if the statement has a positive meaning or not", icon="ℹ️")
                elif sentiment_dict['compound'] <= -0.05: 
                    st.success("Negative Statement")
                    st.info("A **''sentiment''** is an attitude or emotion towards something, and can be determined if the statement has a positive meaning or not", icon="ℹ️")
                else: 
                    st.success("Neutral Statement")
                    st.info("A **''sentiment''** is an attitude or emotion towards something, and can be determined if the statement has a positive meaning or not", icon="ℹ️")

            except Exception as e: 
                obj1 = os.system("ping www.google.com")
                if obj1==1: 
                    st.write("Please Check Your Internet Connection.")
                else: 
                    st.write("Analysis Error. Try Again")

if __name__=="__main__": 
    main()
