import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Webpage", page_icon='tada', layout='wide')

st.header("Pandas Website Test For CSV Files")
st.subheader("Upload a file that you would like to get information from.")





def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df




fileupload = st.file_uploader(label=" ")

def answer_question(df, column_name, question):
    if column_name not in df.columns:
        return "Sorry, that column does not exist in the data. Please check punctuation and ensure that you pressed enter."
    else:
        if question == "average":
            return df[column_name].mean()
        elif question == "minimum":
            return df[column_name].min()
        elif question == "maximum":
            return df[column_name].max()
        elif question == "standard deviation":
            return df[column_name].std()
        else:
            return "Sorry, I don't understand your question."



#file_path = st.text_input('Input EXACT file path here, and press enter.')
#file_path = "C:/Users/ethan/Cookies/Desktop/streamlit1.csv.csv"



@st.cache(allow_output_mutation=True)
def get_data():
    return []
if fileupload:
    df = read_csv(fileupload)
    question = st.text_input("What Function? (Type average, minimum, maximum, or standard deviation)").lower()
    column_name = st.text_input("Column Name? (Use correct punctuation)").lower
    answer = answer_question(df, column_name, question)
    st.write(answer)
#st.write(answer)
