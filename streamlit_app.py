import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Webpage", page_icon='tada', layout='wide')

st.header("Pandas Website Test For CSV Files")
st.subheader("You will receive the red error until you input the exact file path to which you would like to use.")
st.write("It must be the exact file path as well as a csv, for example /Users/You/Dekstop/yourfile.csv")
st.write("For mac, visit here on how to get an exact file path : https://support.apple.com/guide/mac-help/get-file-folder-and-disk-information-on-mac-mchlp1774/mac")

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def answer_question(df, column_name, question):
    if column_name not in df.columns:
        return "Sorry, that column does not exist in the data."
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

file_path = st.text_input('Input EXACT file path here, and press enter.')
#file_path = "C:/Users/ethan/Cookies/Desktop/streamlit1.csv.csv"
df = read_csv(file_path)

@st.cache(allow_output_mutation=True)
def get_data():
    return []

question = st.text_input("What Function? (Type average, minimum, maximum, or standard deviation)").lower()
column_name = st.text_input("Column Name? (Use correct punctuation)")
answer = answer_question(df, column_name, question)
st.write(answer)
