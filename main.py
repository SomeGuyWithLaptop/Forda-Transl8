import streamlit as st 
from googletrans import Translator, LANGUAGES
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def main(): 
    st.title("Forda Transl8 Yarn")
    st.caption("A Netspeak Translator with Sentiment Analysis :)")
    activities=["Translator", "Sentimental Analysis"]
    choice=st.sidebar.selectbox("Select Activities", activities)

    #Translator Part
    if choice == "Translator": 
        st.write("\n")
        st.write("\n")
        st.write("Translator")
        from_text = st.text_input("Enter Source Text: ")
        from_code = st.text_input("Enter the Language: ")
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
        st.write("Sentiment Analyzer")
        from_sent = st.text_input("Enter a Sentence: ")
        if st.button("Check Sentiment"): 
            try:
                obj = SentimentIntensityAnalyzer()
                sentiment_dict = obj.polarity_scores(from_sent)

                st.write(sentiment_dict) 
                st.write("Sentence is rated as ", sentiment_dict['neg']*100, "% Negative")
                st.write("Sentence is rated as ", sentiment_dict['neu']*100, "% Neutral")
                st.write("Sentence is rated as ", sentiment_dict['pos']*100, "% Positive")

                st.write("\n" )
                st.write("\n" )

                st.write("Sentence gives a: " )

                #Dito yung part kung good or bad yung statement
                if sentiment_dict['compound'] >= 0.05 : 
                    st.success("Positive Statement")
                elif sentiment_dict['compound'] <= -0.05: 
                    st.success("Negative Statement")
                else: 
                    st.success("Neutral Statement")

            except Exception as e: 
                obj1 = os.system("ping www.google.com")
                if obj1==1: 
                    st.write("Please Check Your Internet Connection.")
                else: 
                    st.write("Analysis Error. Try Again")

if __name__=="__main__": 
    main()
