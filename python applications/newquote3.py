import json
import requests
import streamlit as st
import random


# List of amazing quotes
amazing_quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt"
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill"
]

def get_random_quote():
    return random.choice(amazing_quotes)

def main():
    st.title("DAILY QUOTES FOR YOUR MOOD")
    st.write("Click the button below to get a new amazing quote!")
    
    if st.button("Generate Quote"):
        quote = get_random_quote()
        st.write(quote)

if __name__ == "__main__":
    main()
