import streamlit as st
from tools import exam_answer, user_question

PAGE_TITLE = "StatsPilot"
PAGE_ICON = "🥧"
LAYOUT = "centered"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)

st.markdown(
    f"<h1 style='text-align: center;'>{PAGE_TITLE} {PAGE_ICON} <br> Tools for statistics class survival!</h1>",
    unsafe_allow_html=True,
)

st.sidebar.title("About")
st.sidebar.markdown(
    """
**StatsPilot** provides a selection of prompt refinement tools that help you generate the
better prompts for ChatGPT.
"""
)

# Add a dropdown menu to select the prompt tool type
st.markdown("### Select a tool:")
tool_type = st.radio(
    "Tool explanation below",
    [
        "Answer an Exam Question",
        "Ask a Question",
    ],
)

tool_explanation = {
    "Answer an Exam Question": """
    ##### Answer an Exam Question Tool
    This tool helps you generate an answer to an exam question.
    Copy the question into the input box and click the "Generate" button.
    """,
    "Ask a Question": """
    ##### Ask a Question Tool
    This tool helps answer a statistics question through teaching.
    Ask your question in the input box and select your skill level, then click the "Generate" button.
    """,
}

with st.expander("Tool Explanation"):
    st.markdown(tool_explanation[tool_type])

# Create a dictionary mapping tool types to their corresponding functions
tool_functions = {
    "Answer an Exam Question": exam_answer.get_question_answer,
    "Ask a Question": user_question.get_question_answer,
}

if tool_type == "Ask a Question":
    skill_level = st.select_slider(
        "Select your skill level:",
        [
            "Beginner's Playground",
            "Inquisitive Explorer",
            "Determined Challenger",
            "Master Statistician"
        ],
    )

    # Map the skill level to an integer value
    skill_level_map = {
        "Beginner's Playground": 2,
        "Inquisitive Explorer": 6,
        "Determined Challenger": 10,
        "Master Statistician": 14,
    }

    # Pass the appropriate integer value to the get_question_answer function
    tool_functions["Ask a Question"] = lambda x: user_question.get_question_answer(x, skill_level_map[skill_level])

st.sidebar.markdown(
    """
---
Built by **Jared Kirby** :wave:

[Twitter](https://twitter.com/Kirby_) | [GitHub](https://github.com/jaredkirby) | [LinkedIn](https://www.linkedin.com/in/jared-kirby/) | [Portfolio](https://www.jaredkirby.me)

    """
)

st.markdown("### Enter your input below:")


def get_text() -> str:
    user_input = st.text_area(
        "Input type will change depending on the tool selected.",
        "What is the difference between population and sample in statistics?",
        key="input",
    )
    return user_input


user_input = get_text()

button = st.button("Generate")

if user_input and button:
    with st.spinner("Generating response..."):
        # Use the tool_type selected by the user to call the corresponding function
        output = tool_functions[tool_type](user_input)
    st.markdown(
        f'''
        StatsPilot:
        {output}
        '''
    )