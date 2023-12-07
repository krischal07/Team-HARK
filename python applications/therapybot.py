import streamlit as st

st.title("Mental Health Support Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize context dictionary
if "context" not in st.session_state:
    st.session_state.context = {}

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
    if "depressed" in prompt.lower() or "anxious" in prompt.lower():
        response = "I'm sorry to hear that you're feeling this way. It's important to acknowledge and express your feelings. If you're comfortable, consider talking to someone you trust about what you're going through. Additionally, engaging in activities you enjoy, maintaining a regular sleep schedule, and incorporating exercise into your routine can have positive effects on mood. However, it's crucial to reach out to a mental health professional for personalized support and guidance. They can provide valuable insights and help you develop coping strategies tailored to your specific situation. Remember that seeking help is a sign of strength, and you don't have to face this alone. If you're in crisis, please reach out to a helpline or emergency services in your country."
        # Update context to reflect the user's emotional state
        st.session_state.context["emotion"] = "depressed"
    elif "stress" in prompt.lower() or "overwhelmed" in prompt.lower():
        response = "I'm sorry to hear that you're feeling overwhelmed. It's completely normal to feel this way at times, and it's important to acknowledge and explore those feelings. Can you tell me more about what might be contributing to your sense of overwhelm? Are there specific situations, responsibilities, or thoughts that are particularly challenging for you right now?It's essential to take breaks. How about trying a relaxation exercise?"
        # Update context to reflect the user's emotional state
        st.session_state.context["emotion"] = "stressed"
    elif "lonely" in prompt.lower() or "isolated" in prompt.lower():
        response = "I'm sorry to hear that you're feeling isolated. It's common for people to experience loneliness, and it's important to address these feelings. Can you share a bit more about what might be contributing to your sense of isolation? Are there specific factors, such as changes in relationships or circumstances, that you find challenging? Additionally, have you considered reaching out to friends, family, or others for support or companionship?"
        # Update context to reflect the user's emotional state
        st.session_state.context["emotion"] = "lonely"
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