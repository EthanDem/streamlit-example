import openai
import streamlit as st
openai.api_key = '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'

messages = []

system_msg = st.text_input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content":system_msg})

x = st.text_input("Input question here")
button_pressed = st.button("Send question")

if button_pressed:
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    st.write("\n" + reply + "/n")
