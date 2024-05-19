from pathlib import Path
import sys
PARENT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(PARENT_DIR))
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from llm import LlmRepo
import os

class Conversation:
    def __init__(self):
        pass
    def start_conversation(self):

        # st.title("FinThrivin")
        llmrepo = LlmRepo()
        basic_user_details = []
        context = ""

        # Define initial question
        question = ""

        # Define dictionary of questions based on user responses
        question_mapping = {
                "hello": "I would like to as you some security questions to identify who you are and better assist you. Can you please give me your first Name?",
                "first name": ["what is your last name?"],
                "last name":['what is your date of birth?,please provide date of birth in mm/dd/yyyy format'],
                "date of birth":['Looks like you are existing user'],
                "new user": ["Welcome. To give you better advice and insights, it is important to get some financial information from you. This will take about 10 minutes. If you don't have 10 minutes, you can also do this in parts. Do some right now and come back and finish later. Are you ready to start?"],
                "existing user": ['can you provide your more details about your financial details'],
                "ready to start": ["What's your profession?"],
                "profession": ["Enter your profession-specific question here."],
                "collect other questions": ["Enter other relevant questions here."],
            }
        template = """INSTRUCTIONS:

                    Context: {context}

                    As a financial analyst, your task is to ask the appropriate question based on the current context.

                    Ask the following question by understanding the current context:
                    {question}

                    The available questions for each context are defined as follows:
                    {question_mapping}

                    Provide a response based on the user_text and the context.

                    Do not add any extra information other than the question picked up from question_mapping

                    Response:
                    """
        colored_header(label='', description='', color_name='blue-30')
        welcome_msg = 'Hi my name Robert. Welcome to FinThrivin.'

        if "conversation" not in st.session_state:
            st.session_state.conversation = [{'type': 'llm', 'text': welcome_msg}]

        user_input_container = st.sidebar.container()
        

        for item in st.session_state.conversation:
            if item['type'] == 'user':
                # message(item['text'], is_user=True)
                st.sidebar.write("User Response:", item['text'])
            else:
                # message(item['text'])
                st.sidebar.write("LLM Response:", item['text'])

        with user_input_container:
            st.title('User profile chatbot')
            user_input = st.sidebar.chat_input("type your answer here")

            if user_input:
                
                with st.spinner('Processing..'):
                    st.session_state.conversation.append({'type': 'user', 'text': user_input})
                    response = llmrepo.llm_chatbot_inference(template=template,
                                                            question=question,
                                                            question_mapping=question_mapping,
                                                            user_input=user_input,
                                                            context=context)

                    # st.session_state.asked_questions.append(response)
                    st.session_state.conversation.append({'type': 'llm', 'text': response})
                    st.sidebar.write("LLM Response:", response)




    
           
   
    