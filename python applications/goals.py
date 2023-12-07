import streamlit as st
import random

def generate_daily_goals():
    goals = [
        "Exercise for 30 minutes",
        "Read a chapter of a book",
        "Learn something new for 15 minutes",
        "Write in a journal for 10 minutes",
        "Practice mindfulness for 10 minutes",
        "Wake up at a specific time.",
        "Practice mindfulness or meditation for 10 minutes."
        "Read a chapter of a book.",
        "Wake up at a specific time.",
        "Practice mindfulness or meditation for 10 minutes.",
        "Read a chapter of a book.",
        "Write down three things you're grateful for.",
        "Take a 30-minute walk or exercise.",
        "Drink at least 8 glasses of water.",
        "Limit social media usage to 30 minutes.",
        "Learn a new word and use it throughout the day.",
        "Eat a healthy breakfast, lunch, and dinner.",
        "Complete a short workout routine.",
        "Call or message a friend or family member.",
        "Learn a new skill for 20 minutes.",
        "Clean and organize a specific area of your home.",
        "Avoid caffeine or sugary drinks.",
        "Write in a journal for 15 minutes.",
        "Plan and prepare a nutritious snack.",
        "Set aside time for a hobby you enjoy.",
        "Review and update your to-do list.",
        "Express kindness to someone.",
        "Limit screen time before bedtime.",
        "Learn a new recipe and cook it.",
        "Take breaks every hour to stretch and move.",
        "Practice deep breathing exercises.",
        "Listen to a podcast or audiobook.",
        "Create a budget or track your expenses.",
        "Send a thank-you note or message.",
        "Learn a new fact about a topic you're interested in.",
        "Limit multitasking and focus on one task at a time.",
        "Do something creative, like drawing or writing.",
        "Volunteer your time or help someone in need.",
        "Disconnect from technology for an hour.",
        "Review and reflect on your goals.",
        "Plan a small act of kindness for someone else.",
        "Practice a language you're learning for 15 minutes.",
        "Watch a documentary or educational video.",
        "Create a playlist of motivating or relaxing music.",
        "Plan and organize tasks for the next day.",
        "Research a topic you're curious about.",
        "Take a photo of something that makes you happy.",
        "Write a letter to your future self.",
        "Spend quality time with loved ones.",
        "Learn a new yoga pose or stretch routine.",
        "Try a new type of tea or coffee.",
        "Set specific work or study goals.",
        "Unsubscribe from unnecessary emails.",
        "Create a vision board for your future.",
        "Learn about a different culture or tradition.",
        "Practice gratitude by thanking someone.",
        "Limit negative self-talk and focus on positivity.",
        "Review and celebrate your achievements for the day."
    ]
    return random.sample(goals, 5)

def main():
    st.title("Daily Goals Generator")

    # Button to generate more goals at the top right
    if st.button("Generate More Goals", key="generate_button"):
        if all(st.session_state.completed_goals.values()):
            st.session_state.daily_goals = generate_daily_goals()
            st.session_state.completed_goals = {f"goal_{i}": False for i in range(1, 6)}
            st.session_state.affirmation = ""
        else:
            st.warning("Please complete all goals before generating more.")

    # Retrieve or generate daily goals
    if 'daily_goals' not in st.session_state:
        st.session_state.daily_goals = generate_daily_goals()

    # Initialize session state to store checkbox states and affirmation
    if 'completed_goals' not in st.session_state:
        st.session_state.completed_goals = {f"goal_{i}": False for i in range(1, 6)}

    if 'affirmation' not in st.session_state:
        st.session_state.affirmation = ""

    # Display daily goals with checkboxes
    st.markdown("## Your Daily Goals:")
    for i, goal in enumerate(st.session_state.daily_goals, start=1):
        key = f"goal_{i}"
        checkbox_state = st.checkbox(f"Goal {i}: {goal}", key=key, value=st.session_state.completed_goals[key])
        st.session_state.completed_goals[key] = checkbox_state

    # Display a random affirmation for completed goals with styling
  
    affirmations = [
        "Well done! You're making progress.",
        "Great job! Keep it up.",
        "Fantastic! Celebrate your achievements.",
        "Amazing work! Consistency is key.",
        "You're on fire! Keep that momentum going."
        "I am deserving of all the good things in my life.",
        "You are deserving of all the happiness in the world.",
        "Your potential is limitless, and you have the power to achieve your dreams.",
        "You radiate positivity, and good things are drawn to you.",
        "Your presence brings joy and warmth to those around you.",
        "You have the strength and resilience to overcome any challenge.",
        "Your kindness and compassion make a positive impact on others.",
        "You are surrounded by love and support from those who care about you.",
        "Your unique qualities and talents make you truly special.",
        "You are constantly evolving and growing into the best version of yourself.",
        "Your decisions are guided by wisdom, and you trust in your ability to choose wisely.",
        "You have a beautiful soul that shines through in everything you do.",
        "Your life is filled with purpose, and you contribute meaningfully to the world.",
        "You are a source of inspiration for those who know you.",
        "Your positive attitude is contagious, uplifting those around you.",
        "You are worthy of all the success and happiness life has to offer.",
        "Your confidence in your abilities is admirable.",
        "You create a life filled with passion and purpose.",   
        "You are open to new opportunities and embrace change with grace.",
        "Your authenticity and alignment with your true self are admirable.",
        "You are a beacon of light, bringing positivity wherever you go."

    ]

    completed_goals_keys = [key for key, value in st.session_state.completed_goals.items() if value]
    if completed_goals_keys:
        key = random.choice(completed_goals_keys)
        affirmation_text = random.choice(affirmations)
        styled_affirmation = (
            f'<div style="background-color: lightgreen; border: 1px solid #c3e6cb; border-radius: 5px; padding: 10px;">'
            f'<p style="font-weight: bold; color: #155724;">{affirmation_text}</p>'
            f'</div>'
        )
        st.markdown(styled_affirmation, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
