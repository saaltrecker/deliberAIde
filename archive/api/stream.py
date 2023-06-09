import streamlit as st
import requests
#run this file with streamlit run api.stream.py

st.markdown('''# DeliberAIde''')


st.markdown('''## Welcome to DeliberAIde!''')

inp= st.text_input('Enter your prompt here')

select= st.radio('Select your option', ('Topics', 'viewpoints', 'tree'))
but= st.button('deliberAIde')
if inp!='':
    if select=='Topics' and but==True:
        st.markdown(f'here is your prompt: {inp}')
        url= 'http://127.0.0.1:8000/topics'
        response= requests.get(url).json()
        st.markdown(f'here are the topics: {response}')


    elif select=='viewpoints'and but==True:
        st.markdown(f'here is your prompt: {inp}')
        url= 'http://127.0.0.1:8000/viewpoints'
        params= {'prompt': 'hello there'}

        response= requests.get(url).json()
        st.markdown(f'here is viewpoints: {response}')

    elif select=='tree' and but==True:
        st.markdown(f'here is your prompt: {inp}')
        url= 'http://127.0.0.1:8000/tree'
        response= requests.get(url).json()
        st.markdown(f'here is Tree: {response}')

    elif but==True:
        st.markdown(f'here is your prompt: {inp}')
        url= 'http://127.0.0.1:8000/deiber'
        response= requests.get(url).json()
        st.markdown(f'here is Overall deliber: {response}')
if inp=='' and but==True:
    st.markdown("<p style='color: red;'>Please enter your prompt and select your option</p>", unsafe_allow_html=True)
