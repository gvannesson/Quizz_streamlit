import streamlit as st
import json
import os
from pydantic import BaseModel, field_validator, model_validator, ValidationError
from typing import List

number_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth"]

st.markdown("# Création d'un quiz🎉")
st.sidebar.markdown("# Créer un quiz 🎉")

if "list_answer" not in st.session_state:
    st.session_state.list_answer = []

if "flag" not in st.session_state:
    st.session_state.flag = False

if "submit" not in st.session_state:
    st.session_state.submit = False

if "flag_boucle" not in st.session_state:
    st.session_state.flag_boucle = False

# if "answer_0" in st.session_state:
#     st.session_state.answer_0 = st.write("réponse 0")

# if "answer_1" in st.session_state:
#     st.session_state.answer_1 = st.write("réponse 1")

if 'reset' not in st.session_state:
    st.session_state.reset = False

# if 'answer_number' not in st.session_state:
#     st.session_state.answer_number = 0

# Clear input fields by checking the reset flag
if st.session_state.reset:
    st.session_state["question"] = ''
    for i in range(int(st.session_state.answer_number)):
        st.session_state[f"answer_{i}"] = ""
    st.session_state.answer_number =''
    st.session_state["good_answer"] = ''
    # Set the reset flag back to False
    st.session_state.reset = False
    st.session_state.submit = False
    st.session_state.flag = False
    st.session_state.flag_boucle = False
    st.session_state.list_answer = []


class Quiz(BaseModel):
    question: str
    answers: List[str]
    good_answer: int

    # Validations des champs individuels
    @field_validator('question')
    def validate_question(cls, value):
        if not value:
            raise ValueError("La question ne peut pas être vide.")
        return value

    # @field_validator('answers')
    # def validate_answers(cls, value):
    #     if len(value) != 4:
    #         raise ValueError("Il faut exactement 4 réponses possibles.")
    #     if any(not answer for answer in value):
    #         raise ValueError("Toutes les réponses doivent être renseignées.")
    #     return value

    @field_validator('good_answer')
    def validate_good_answer(cls, value):
        if value not in [1, 2, 3, 4]:
            raise ValueError("La réponse correcte doit être un chiffre entre 1 et 4.")
        return value

    # Validation globale du modèle
    @model_validator(mode="before")
    def check_all_fields(cls, values):
        if not values.get('question'):
            raise ValueError("La question ne peut pas être vide.")
        if len(values['answers']) != int(st.session_state.answer_number):
            raise ValueError(f"Il faut exactement 4  {len(values['answers'])} réponses possibles.")
        if values["good_answer"] not in [str(i) for i in range(int(st.session_state.answer_number))]:
            raise ValueError("La réponse correcte doit être un nombre entre 1 et 4.")
        return values


question = st.text_input('Type a question', key="question")
st.text_input('Type a number of possible answers', key="answer_number")


if not st.session_state.flag:
    if st.button("Valider le nombre de réponses à entrer"):
        st.session_state.flag = True
        st.rerun()

if st.session_state.flag:
    if not st.session_state.flag_boucle:
        with st.form("form"):
            for i in range(int(st.session_state.answer_number)):
            #st.session_state.list_answer.append(st.text_input(f'Type the {number_list[i]} possible answer', key=f"answer_{i}"))
                st.text_input(f'Type the {number_list[i]} possible answer', key=f"answer_{i}")
            print(st.session_state)
            good_answer = st.text_input('Type the number of the good answer', key="good_answer")
            st.session_state.submit = st.form_submit_button("bouton de submit")
        if st.session_state.submit:
            # if st.button('Save your question'):
# with open('quiz_data.json', 'w') as file:
#     json.dump({"Question :" : question, "Answers :" : [answer_1,answer_2,answer_3,answer_4], "good_answer :" : good_answer}, file)
                # st.session_state.reset = True

                # st.rerun()

            try:
                # Valider l'objet Quiz avec les données saisies
                quiz_data = Quiz(
                    question=question,
                    answers=[st.session_state[f"answer_{i}"] for i in range(int(st.session_state.answer_number))],
                    good_answer=good_answer
                )
                if os.path.exists('quiz_data.json'):
                # Open the file and load the existing data
                    with open('quiz_data.json', 'r') as file:
                        data = json.load(file)
                    
                    # Add the new question to the data (assuming it's a list of questions)
                    data.append({"Question :" : question, "Answers :" : [st.session_state[f"answer_{i}"] for i in range(int(st.session_state.answer_number))], "good_answer :" : good_answer})
                else:
                    # If the file doesn't exist, start with an empty list
                    data = [{"Question :" : question, "Answers :" : [st.session_state[f"answer_{i}"] for i in range(int(st.session_state.answer_number))], "good_answer :" : good_answer}]

                # Write the updated data back to the JSON file
                with open('quiz_data.json', 'w') as file:
                    json.dump(data, file, indent=4)
                
                st.session_state.reset = True

                st.rerun()

            except ValidationError as e:
                # Afficher les erreurs de validation
                st.error(f"Erreur de validation : {e}")
                st.session_state.flag_boucle=True



