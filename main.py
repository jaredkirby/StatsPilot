import streamlit as st
from langchain.chat_models import ChatOpenAI

import tools.exam_answer as exam_answer, tools.user_question as user_question, tools.explain as explain, tools.translate as translate
from utils.stream import StreamHandler

openai_api_key = st.secrets["OPENAI_API_KEY"]


PAGE_TITLE = "StatsPilot"
PAGE_ICON = "🥧"
LAYOUT = "centered"


def set_page_config():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)


def create_chat(temperature, model, stream_handler):
    chat = ChatOpenAI(
        temperature=temperature,
        model=model,
        openai_api_key=openai_api_key,
        request_timeout=250,
        streaming=True,
        callbacks=[stream_handler],
    )
    return chat


def main():
    set_page_config()
    st.markdown(
        f"<h1 style='text-align: center;'>{PAGE_TITLE} {PAGE_ICON} <br> Tools for statistics class survival!</h1>",
        unsafe_allow_html=True,
    )

    # Define the samples dictionary
    samples = {
        "Ask a Question": "What does it mean for a result to be statistically significant, and how is it determined?",
        "Explain a Concept or Term": "Probability",
        "Answer an Exam Question": """\
    A study compared the heights of two groups of individuals, Group A and Group B. 
    The heights (in centimeters) of the participants were recorded as follows:

    Group A: 160, 165, 170, 175, 180
    Group B: 165, 170, 175, 180, 185

    (a) Calculate the mean height for each group.

    (b) Determine whether there is a significant difference in the mean heights between the two groups.
            """,
        "Analyze Data": "What is the correlation between height and weight?",
        "Expression to English": "Probability Density Function (PDF): f(x) = (1 / σ√(2π)) * e^(-(x-μ)² / (2σ²))",
    }
    # Define skill levels and their corresponding integer values
    skill_levels = {
        "4th Grade": 4,
        "8th Grade": 8,
        "HS Senior": 12,
        "College": 16,
    }

    # Set up tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Explain a Concept or Term",
            "Answer an Exam Question",
            "Ask a Question",
            "Expression to English",
        ]
    )

    with tab1:
        handle_explain_tab(samples, skill_levels)
    with tab2:
        handle_exam_question_tab(samples)
    with tab3:
        handle_question_tab(samples, skill_levels)
    with tab4:
        handle_expression_tab(samples)
    # with tab5:
    #    handle_summarize_tab(samples)

    st.markdown(
        """
    ---
    Built by **Jared Kirby** :wave:

    [Twitter](https://twitter.com/Kirby_) | [GitHub](https://github.com/jaredkirby) | [LinkedIn](https://www.linkedin.com/in/jared-kirby/) | [Portfolio](https://www.jaredkirby.me)

        """
    )


def handle_exam_question_tab(samples):
    sample = samples.get("Answer an Exam Question", "")
    user_input = st.text_area(
        "Input Exam Question", sample, height=275, key="exam_question_input"
    )
    temperature = 0
    model = "gpt-4"
    exam_button = st.button("Generate Answer", key="exam_button")
    if exam_button:
        exam_chat_box = st.empty()
        exam_stream_handler = StreamHandler(exam_chat_box)
        exam_chat = create_chat(temperature, model, exam_stream_handler)
        exam_answer.get_exam_question_answer(exam_chat, user_input)


def handle_question_tab(samples, skill_levels):
    sample = samples.get("Ask a Question", "")
    user_input = st.text_area("Input Question", sample, key="question_input")
    skill_level = st.select_slider(
        "Select your skill level:",
        list(skill_levels.keys()),
        key="question_skill_level",
    )
    temperature = 1
    model = "gpt-4"
    question_button = st.button("Generate Answer", key="question_button")
    if question_button:
        question_chat_box = st.empty()
        question_stream_handler = StreamHandler(question_chat_box)
        question_chat = create_chat(temperature, model, question_stream_handler)
        user_question.get_user_question_answer(
            question_chat, user_input, skill_levels[skill_level]
        )


def handle_explain_tab(samples, skill_levels):
    sample = samples.get("Explain a Concept or Term", "")
    user_input = st.text_area("Input Concept or Term", sample, key="concept_input")
    skill_level = st.select_slider(
        "Select level of explanation:", list(skill_levels.keys()), key="skill_level"
    )
    temperature = 1
    model = "gpt-4"
    explain_button = st.button("Generate Explanation", key="explain_button")
    if explain_button:
        explain_chat_box = st.empty()
        explain_stream_handler = StreamHandler(explain_chat_box)
        explain_chat = create_chat(temperature, model, explain_stream_handler)
        explain.get_explanation(explain_chat, user_input, skill_levels[skill_level])


def handle_expression_tab(samples):
    sample = samples.get("Expression to English", "")
    user_input = st.text_area("Input Expression", sample, key="expression_input")
    context_input = st.text_input("Input Context", key="context_input")
    temperature = 0.75
    model = "gpt-4"
    expression_button = st.button(
        "Translate Expression to English", key="expression_button"
    )
    if expression_button:
        expression_chat_box = st.empty()
        expression_stream_handler = StreamHandler(expression_chat_box)
        expression_chat = create_chat(temperature, model, expression_stream_handler)
        translate.get_expression_to_english(expression_chat, user_input, context_input)


def handle_summarize_tab(samples):
    sample = samples.get("Answer an Exam Question", "")
    temperature = 1
    model = "gpt-4"
    user_input = st.text_area(
        "Input Research Paper", sample, height=275, key="paper_input"
    )
    summarize_button = st.button("Generate Summary", key="summarize_button")
    if summarize_button:
        summarize_chat_box = st.empty()
        summarize_stream_handler = StreamHandler(summarize_chat_box)
        summarize_chat = create_chat(temperature, model, summarize_stream_handler)
        # summarizer.main(summarize_chat, user_input)


if __name__ == "__main__":
    main()
