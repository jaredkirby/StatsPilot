from utils import chat_4_0

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)

def get_exam_question_answer(user_input: str):
    sys_template = "You are a Statistics and data expert taking a statistics exam."
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Exam question:
    {user_input}
    Please respond by walking through your thought process and calculations step by step then make your final answer very clear.
    Format your response in markdown.
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
    llm = chat_4_0
    result = llm(formatted_answer_prompt)
    print("Bot Response:", result.content)
    return result.content

