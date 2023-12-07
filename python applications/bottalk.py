import streamlit as st
import random

st.title("Mental Health Support Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize context dictionary
if "context" not in st.session_state:
    st.session_state.context = {}

# Define responses for each keyword
responses = {
    "depressed": [
        "I'm sorry to hear that you're feeling this way. It's truly difficult when depression takes hold. Remember that you don't have to go through this alone. Reach out to friends, family, or a mental health professional who can offer support and understanding. Taking small steps each day, like engaging in activities you enjoy or talking to someone you trust, can be important in the journey toward healing. Be gentle with yourself, and know that it's okay to ask for help.",
        "It's important to acknowledge and express your feelings, especially when facing depression. Give yourself the space to understand and accept your emotions without judgment. Whether through journaling, talking to a friend, or seeking professional support, expressing what you're going through can be a crucial step in the healing process. Remember that your feelings are valid, and taking the time to explore them is a sign of strength. As you navigate this journey, be patient with yourself and recognize that healing is a gradual process.",
        "Remember that seeking help is a sign of strength. It takes courage to recognize when you need support and to take steps toward healing. Whether it's reaching out to friends, family, or a mental health professional, you're making a proactive choice to prioritize your well-being. By seeking help, you're demonstrating resilience and a commitment to your own growth. Embrace the support that is available to you, and know that you're not alone on this journey. It's okay to ask for help, and it's a powerful step toward creating positive change in your life."
    ],
    "stress": [
        "I'm sorry to hear that you're feeling overwhelmed. It's completely understandable that life's challenges can sometimes become too much to bear. In times like these, it might be helpful to break things down into smaller, more manageable tasks. Prioritize self-care and consider reaching out to a supportive friend, family member, or a mental health professional. Remember, it's okay to ask for help, and taking small steps can lead to a sense of accomplishment. You don't have to navigate this overwhelm alone, and support is available to help you through it.",
        "I'm sorry to hear that you're feeling stressed. It's completely normal to experience stress, and I'm here to help you navigate through it. Let's explore together what might be contributing to your stress and work on strategies to manage and alleviate these feelings. Remember, you don't have to face this alone, and we can collaborate to develop coping mechanisms tailored to your unique situation. What specific aspects of your life or situations are currently causing you the most stress?"
    ],
    "lonely": [
        "I'm sorry to hear that you're feeling isolated. It's a challenging and often overwhelming experience. It's important to recognize that you don't have to navigate this sense of isolation alone. In our sessions, we can explore the factors contributing to these feelings and work together to develop strategies to connect with others and build a supportive network. Additionally, consider reaching out to friends, family, or engaging in activities that bring you a sense of connection. Remember, your feelings are valid, and it's okay to seek support. Let's explore ways to strengthen your connections and foster a sense of belonging.",
        "Have you considered reaching out to friends, family, or others for support or companionship? Connecting with people who care about you can be a powerful way to alleviate feelings of isolation. Sharing your thoughts and emotions with someone you trust can provide comfort and understanding. If reaching out feels challenging, we can explore together what might be holding you back and work on strategies to make those connections. Remember, you deserve support, and there are people who care about you. Let's discuss how we can create a plan to strengthen your social connections and enhance your sense of well-being."
    ],
    "sad": [
        "I'm sorry to hear that you're feeling sad. It's important to recognize and acknowledge your emotions. In our therapeutic journey, we can explore the depth of these feelings, understanding when they arise and any specific triggers that may contribute. By delving into the nuances of your emotional landscape, we can gain insights that guide our work together.",
        "It's perfectly natural to feel a range of emotions, and sadness is a valid and human response to various life experiences. Your willingness to share this with me is a testament to your courage and self-awareness. Let's work collaboratively, drawing upon your strengths, to navigate through this emotional space."
        
    ],
    "what is my purpose": [
        "I'm truly sorry to hear that you're feeling this way. It's not uncommon for people to experience moments when life feels overwhelming or devoid of meaning. I want you to know that your feelings are valid, and it's essential for us to explore them together. In our sessions, we can delve into the factors contributing to this sense of meaninglessness, examining aspects of your life, relationships, and personal goals.",
        "It's important to remember that emotions can be transient, and working through these feelings is a process. While I'm here to support you, it might also be beneficial to involve additional resources, such as friends, family, or support groups. They can offer different perspectives and forms of support."

    ],
    "relationship": [
        "I hear that you're feeling lonely and expressing a desire for a romantic relationship. Loneliness can be a challenging emotion, and it's completely valid to seek connection with others. It's important to acknowledge that relationships, including romantic ones, can be complex and don't define your worth."
    ],
    "live": [
        "I'm truly sorry to hear that you're feeling like this. It's crucial to prioritize your safety. Reach out to a mental health professional, a trusted person in your life, or a helpline. You don't have to face this alone, and there are people who want to support you. If you're in immediate danger, please call emergency services in your country. It's okay to ask for help, and taking that step can make a significant difference in your well-being. Your life is valuable, and there are resources available to support you through difficult times."
    ],
    "carrer": [
        "I hear that you're feeling frustrated about your career path. Remember, it's never too late to reassess and make changes. Let's explore your goals, strengths, and interests to create a plan that aligns with your aspirations. Each setback is an opportunity for growth, and your journey is unique. Together, we can work towards a fulfilling and rewarding career that reflects your true potential. Your path may have detours, but it doesn't define your destination. Embrace the possibilities, and let's navigate this journey together."
    ],
    "died": [
        "I'm deeply sorry for your loss. Grieving is a unique and challenging journey. Your loved one's impact lives on in the memories and love shared. In time, may you find solace in the cherished moments, honoring their legacy. It's okay to feel the pain, and I'm here to support you as you navigate through this difficult time. Remember, healing is a gradual process, and your emotions are valid. Allow yourself the space for grief, and in time, may you find moments of peace and resilience. Your loved one's spirit lives on in the love they gave, and they will always hold a special place in your heart."
    ],
    "heal": [
        "I'm glad to hear that you're on a healing journey. Recognize the strength within you. Each step, no matter how small, is progress. Embrace the process, and know that healing is a continuous journey. Celebrate your resilience and the positive changes you're making. It's okay to have moments of difficulty; they are a natural part of the healing process. Trust yourself, and continue moving forward at your own pace. Your commitment to healing is a powerful testament to your courage and inner strength. As you navigate this path, may you find increasing peace, understanding, and a renewed sense of well-being."
    ]
}

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Process user input and provide mental health support
    for keyword, keyword_responses in responses.items():
        if keyword in prompt.lower():
            response = random.choice(keyword_responses)
            # Update context to reflect the user's emotional state
            st.session_state.context["emotion"] = keyword
            break
    else:
        # Check context for emotional state
        if "emotion" in st.session_state.context:
            emotion = st.session_state.context["emotion"]
            response = f"I'm here to support you. How can I assist you further? You mentioned feeling {emotion}."
        else:
            response = "I'm here to support you. How can I assist you further?"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
