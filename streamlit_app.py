import openai
import streamlit as st

openai.api_key = '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'

st.title('Chatbot')

# Let the user set the behavior of the assistant
system_msg = st.text_input("What type of assistant would you like to create?")

user_input = st.text_input("Input your question here")

if st.button('Send question'):
    # Start the conversation with the user defined system message
    conversation = [{"role": "system", "content": system_msg}]

    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation,
    )

    reply = response["choices"][0]["message"]["content"]
    conversation.append({"role": "assistant", "content": reply})

    st.write(reply)
