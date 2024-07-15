import streamlit as st
from dotenv import load_dotenv

from utils.llm_utils import initialize_llm
from questions import QUESTIONS


load_dotenv()

def ask_question(question):
    question_type = question["type"]
    field_funcs = { # func, kwargs
        "radio": (st.radio, {"label": question["question"], "key": question["key"], "options": question["options"], "index": None}),
        "selectbox": (st.selectbox, {"label": question["question"], "key": question["key"], "options": question["options"], "index": None}),
        "text": (st.text_input, {"label": question["question"], "key": question["key"]}),
        "number": (st.number_input, {"label": question["question"], "key": question["key"]}),
    }
    if question_type in field_funcs:
        func = field_funcs[question_type][0]
        selection = func(**field_funcs[question_type][1])
        if question_type in ["radio", "selectbox"]:
            if isinstance(selection, str):
                if selection.lower() == "other":
                    selection = st.text_input(f"Enter your other option for '{question['question']}'", key=f"{question['key']}_other")
        return selection

def check_dependencies(question: dict, answers: dict) -> bool:
    if "depends_on" not in question:
        return True
    dependencies = question["depends_on"]
    dependency_type = question.get("dependency_type", "AND").upper()
    dependency_func = {"AND": all, "OR": any}[dependency_type]
    def check_dependency(dependency):
        dependency_key, dependency_value = dependency
        answer = answers.get(dependency_key, {}).get("answer")
        if dependency_value == "Any":
            return answer is not None
        elif isinstance(dependency_value, (list, tuple)):
            return answer in dependency_value
        else:
            return answer == dependency_value
    return dependency_func(check_dependency(dep) for dep in dependencies)

def run():
    st.title("New Jersey Program Eligibility")
    for key in ["started", "submit_clicked", "submitted"]:
        if key not in st.session_state:
            st.session_state[key] = False
    if st.session_state["submitted"]:
        st.write("Analysis:")
        answers = {qa["question"]: qa["answer"] for key, qa in st.session_state["answers"].items()}
        llm = initialize_llm(
            model_name="gpt-3.5-turbo",
            use_context=True,
            query_limit=1
        )
        analysis = llm.query(f"The following Q&A describes a proposed project:\n\n{answers}")
        st.write(analysis)
    else:
        answers = {}
        for question in QUESTIONS:
            if check_dependencies(question, answers):
                answer = ask_question(question)
                if st.session_state["submit_clicked"]:
                    if question["key"] in st.session_state["missing_questions"]:
                        st.warning("This question requires an answer")
                if answer:
                    st.session_state["started"] = True
                answers[question["key"]] = {
                    "question": question["question"],
                    "answer": answer,
                    "required": question.get("required", True),
                }

        if st.session_state["started"] and st.button("Submit"):
            st.session_state["submit_clicked"] = True
            st.session_state["missing_questions"] = [
                q for q in answers if answers[q]["required"] and answers[q]["answer"] is None
            ]
            if len(st.session_state["missing_questions"]) == 0:
                st.session_state["submitted"] = True
                st.session_state["answers"] = answers
            st.experimental_rerun()


if __name__ == "__main__":
    run()
