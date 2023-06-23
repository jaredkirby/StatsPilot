'''
Automated Research Paper Summarizer: 
This tool would condense lengthy academic papers into a brief summary, highlighting key statistical methods, findings, and limitations. This would help students to quickly understand and critique statistical methods used in research.

I'd like to request your assistance in creating a summary for a research paper. The aim is to provide students studying statistics with a condensed version of the paper that highlights the key statistical methods, findings, and limitations.

Here are the steps you should follow to achieve this:

Read the entire research paper to understand the overall objective, the methods used, the results obtained, and the conclusions drawn.

Identify and highlight the sections of the paper which include the abstract, introduction, methodology, results, and conclusion/discussion. These sections usually carry the most vital information.

Write a brief summary of each section. Ensure you note the main statistical methods used in the methodology section, highlight the important findings in the results, and summarize the implications and limitations in the conclusion section.

Combine your summaries into one concise overview of the paper. This should provide a clear snapshot of the paper's purpose, methods, findings, and implications.

Use language that is clear and easy to understand. Avoid technical jargon whenever possible, so the summary is accessible to statistics students.

Finally, review your summary for completeness and accuracy. Make sure it captures the essence of the research without any unnecessary details.
'''
'''
BEGIN
  SET paper = research paper to be summarized
  SET sections = ["abstract", "introduction", "methodology", "results", "conclusion"]
  SET summary = empty dictionary or map data structure
  
  FOR EACH section IN sections:
    READ section from paper
    HIGHLIGHT key points in section
    WRITE a summary for section
    ADD the summary of section to the 'summary' dictionary with the key as section's name

  COMBINE the summaries in 'summary' dictionary into a coherent overview
  ENSURE the overview is clear, non-technical and comprehensive
  REVIEW the overview for accuracy
  IF any inaccuracies found, then REVISE the overview

RETURN overview
END

'''


from utils import chat_35_0

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)

def get_question_answer(user_input: str):
    sys_template = "You are a Statistics and data expert taking a statistics exam."
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Exam question:
    {user_input}
    Please format your response by walking through your thought process and calculations step by step then make your final answer very clear.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Sure! Let's think step by step:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(user_input=user_input).to_messages()
    llm = chat_35_0
    result = llm(formatted_answer_prompt)
    print("Bot Response:", result.content)
    return result.content

