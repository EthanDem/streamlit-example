import openai
import streamlit as st

openai.api_key = 'your-openai-api-key'

# Start a conversation
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

st.title('Chatbot')

user_input = st.text_input("Input question here")

if st.button('Send question'):
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation,
    )

    reply = response["choices"][0]["message"]["content"]
    conversation.append({"role": "assistant", "content": reply})
    
    st.write(reply)
