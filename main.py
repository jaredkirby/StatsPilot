import streamlit as st
from tools import exam_answer, user_question, explain, translate
from typing import Tuple

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
**StatsPilot** is a collection of tools designed to assist with statistics class survival. 
Whether you need help answering an exam question or understanding a statistics concept, 
StatsPilot has got you covered.
"""
)
st.sidebar.markdown(
    """
---
Built by **Jared Kirby** :wave:

[Twitter](https://twitter.com/Kirby_) | [GitHub](https://github.com/jaredkirby) | [LinkedIn](https://www.linkedin.com/in/jared-kirby/) | [Portfolio](https://www.jaredkirby.me)

    """
)

# Define tool types and their corresponding explanations
tool_types = {
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
    "Explain a Concept or Term": """
    ##### Explain a Concept Tool
    This tool helps explain a statistics concept through teaching.
    Ask your question in the input box and select your skill level, then click the "Generate" button.
    """,
    "Expression to English": """
    ##### Expression to English Tool
    This tool helps translate a mathematical expression into English.
    Copy the expression into the input box and click the "Generate" button.
    """,

}

# Define the samples dictionary
samples = {
    "Ask a Question": "What is the population of China?",
    "Explain a Concept or Term": "Probability",
    "Answer an Exam Question": '''\
A study compared the heights of two groups of individuals, Group A and Group B. 
The heights (in centimeters) of the participants were recorded as follows:

Group A: 160, 165, 170, 175, 180
Group B: 165, 170, 175, 180, 185

(a) Calculate the mean height for each group.

(b) Determine whether there is a significant difference in the mean heights between the two groups.
        ''',
    "Analyze Data": "What is the correlation between height and weight?",
    "Expression to English": "Probability Density Function (PDF): f(x) = (1 / σ√(2π)) * e^(-(x-μ)² / (2σ²))",
}

# Define tool functions
tool_functions = {
    "Answer an Exam Question": exam_answer.get_exam_question_answer,
    "Ask a Question": user_question.get_user_question_answer,
    "Explain a Concept or Term": explain.get_explenation,
    "Expression to English": translate.get_expression_to_english,
}

# Define skill levels and their corresponding integer values
skill_levels = {
    "Beginner's Playground": 2,
    "Inquisitive Explorer": 6,
    "Determined Challenger": 10,
    "Master Statistician": 14,
}

# Define UI elements
st.markdown("### Select a tool:")
tool_type = st.radio("Tool explanation below", list(tool_types.keys()))
with st.expander("Tool Explanation"):
    st.markdown(tool_types[tool_type])

# Call the appropriate tool function based on the selected tool type
if tool_type == "Ask a Question" or tool_type == "Explain a Concept or Term":
    skill_level = st.select_slider("Select your skill level:", list(skill_levels.keys()))
    tool_functions["Ask a Question"] = lambda x: user_question.get_user_question_answer(x, skill_levels[skill_level])
    tool_functions["Explain a Concept"] = lambda x: explain.get_explenation(x, skill_levels[skill_level])
elif tool_type == "Expression to English":
    tool_functions["Expression to English"] = lambda x, y: translate.get_expression_to_english(x, y)

# Define user_input and expression_context variables
user_input = None
expression_context = None

# Define get_text function
def get_text(tool_type: str) -> Tuple[str, str]:
    sample = samples.get(tool_type, "")
    user_input = st.text_area(
        "Input type will change depending on the tool selected.",
        sample,
        key="input",
    )
    expression_context = None
    if tool_type == "Expression to English":
        expression_context = st.text_input("Enter the context of the expression:", "Create example context")
    return user_input, expression_context

# Get user input before button is clicked
user_input, expression_context = get_text(tool_type)

# Only generate output if the user has entered text and clicked the "Generate" button
button = st.button("Generate")
if button:
    with st.spinner("Generating response..."):
        if tool_type == "Expression to English":
            output = tool_functions[tool_type](user_input, expression_context)
        else:
            output = tool_functions[tool_type](user_input)
        st.markdown("### StatPilot:")
    st.markdown(
        f'''
        {output}
        '''
    )