import streamlit as st
import random

def mood_finder(answers):
    # Calculate mood based on answers
    score = sum(answers.values())
    
    if score < 30:
        mood = "Sad"
    elif score < 60:
        mood = "Neutral"
    else:
        mood = "Happy"
    
    return mood

def generate_manual_joke():
    # Define a list of jokes
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What do you call fake spaghetti? An impasta!",
        "Did you hear about the math teacher who’s afraid of negative numbers? He will stop at nothing to avoid them.", 
        "I only know 25 letters of the alphabet. I don't know y.",
        "Why did the bicycle fall over? Because it was two-tired!", 
        "I used to play piano by ear, but now I use my hands and fingers.",
        "How does a penguin build its house? Igloos it together!",
        "What do you call fake cheese? Gouda imposter!",
        "I told my computer I needed a break, and now it won’t stop sending me vacation ads. It’s on a scroll-down menu."
        #
    ]

    
    return random.choice(jokes)

def main():
    st.title("Mood Magic Finder App")
    st.write("DISCLAIMER: These questions have been sourced from the materials available on verywellmind.com, and they will be utilized to assess your mood.")
   
    st.write("(Rate your mood from 1 - Not at all, 5 - Very much)")
    # Dictionary to store user answers
    answers = {}

   
    question = "How do you feel?"
    answer = st.slider(question, 1, 10)
    answers["Q1"] = answer

    question = "How calm do you feel at the moment?"
    answer = st.slider(question, 1, 10)
    answers["Q2"] = answer

    question = "How energized do you feel right now?"
    answer = st.slider(question, 1, 10)
    answers["Q3"] = answer

    question = "Rate your level of motivation currently."
    answer = st.slider(question, 1, 10)
    answers["Q4"] = answer

    question = "How would you describe your level of relaxation?"
    answer = st.slider(question, 1, 10)
    answers["Q5"] = answer

    question = "How satisfied are you with your current situation?"
    answer = st.slider(question, 1, 10)
    answers["Q6"] = answer

    question = "How optimistic are you about the future?"
    answer = st.slider(question, 1, 10)
    answers["Q7"] = answer

    question = "How would you rate your level of focus right now?"
    answer = st.slider(question, 1, 10)
    answers["Q8"] = answer

    question = "How social do you feel today?"
    answer = st.slider(question, 1, 10)
    answers["Q9"] = answer

    question = "How would you rate your overall mood?"
    answer = st.slider(question, 1, 10)
    answers["Q10"] = answer

    # Button to calculate mood
    if st.button("Find My Mood"):
        mood = mood_finder(answers)

        # Customize display based on mood
        if mood == "Happy":
            st.success(f"Your mood seems to be {mood}!")
            st.balloons()  # Optional: Add balloons for extra celebration
            st.markdown(
                """<style>div.stButton > button:first-child {background-color: #4CAF50;}</style>""",
                unsafe_allow_html=True,
            )
        elif mood == "Sad":
            st.error(f"Your mood seems to be {mood}!")
            st.markdown(
                """<style>div.stButton > button:first-child {background-color: #FF5733;}</style>""",
                unsafe_allow_html=True,
            )

            # Generate and display a random joke to cheer up the user
            joke = generate_manual_joke()
            st.write("Cheer up with a joke:")
            st.write(joke)
        else:
            st.info(f"Your mood seems to be {mood}.")

if __name__ == "__main__":
    main()
