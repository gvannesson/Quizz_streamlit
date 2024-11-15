import streamlit as st
import json


with open('quiz_data.json', 'r') as file:
    data = json.load(file)

if not "etape"in st.session_state:
    st.session_state.etape = 0
    st.session_state.score=0
    st.session_state.index_bonne_reponse = 0
if st.session_state.etape == len(data):
    st.title("fin de questionnaire")
    st.write(f"Score final: {st.session_state.score} / {len(data)}")
    if st.button("Recommencer le quizz"):
        st.session_state.etape = 0
        st.session_state.score=0

elif st.session_state.etape != len(data):
    selected_answer = None
    st.title(data[st.session_state.etape]["Question :"])
    for i, answer in enumerate(data[st.session_state.etape]["Answers :"]):
        if st.button(answer):
            selected_answer = i+1
            st.session_state.index_bonne_reponse = selected_answer # Stocker l'index de la réponse sélectionnée


    if st.button("Next question"):
        if str(st.session_state.index_bonne_reponse) == data[st.session_state.etape]["good_answer :"]:
            st.session_state.score+=1
        st.session_state.etape +=1
        st.rerun()