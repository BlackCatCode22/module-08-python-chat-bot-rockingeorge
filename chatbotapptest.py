import openai
import streamlit as st
import streamlit.components.v1 as components
import os

# User-defined function go here, before the main() function (is a Python coding convention)
def generate_response(user_input, chat_history):
    messages = [{"role": "system", "content": "Assume the role of a Python teacher. Your name is Skippy Py."}] + chat_history
    messages.append({"role": "user", "content": user_input})

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response_text = completion['choices'][0]['message']['content']
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": response_text})
        return response_text, chat_history
    except Exception as e:
        st.error("Error generating response: " + str(e))
        return "I'm sorry, I couldn't generate a response.", chat_history

# HTML
def render_html():
    html_temp = """
    <style>
    .reportview-container {
        background: #808080;
        color: #FFFFFF;
    }
    .stTextInput > label, .stButton > button {
        color: #04f404;
    }
    </style>
    """
    components.html(html_temp, height=0)

# Function
def main():
    # Set API key securely
    openai.api_key = os.getenv("sk-proj-guLxIoP58Fek41PNtmwwT3BlbkFJwn0GcscgeDOwlC3BDASN")
    
    render_html()

    st.title('Python Study Bot')
    st.write("Welcome to the Python Study Bot! Type your questions below:")

    # Maintain chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Python student question:", "")
    if user_input:
        response, st.session_state.chat_history = generate_response(user_input, st.session_state.chat_history)
        st.text_area("Python Study Bot:", value=response, height=200)

if __name__ == "__main__":
    main()
