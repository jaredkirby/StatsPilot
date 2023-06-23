'''
Statistical Language Translator: A tool to convert mathematical expressions of statistical concepts into plain English and vice versa. This would help students with understanding complex mathematical notation and expressing their understanding in mathematical terms.
'''
'''
"Hello, I'm trying to understand the mathematical expression for conditional probability, which is P(A|B) = P(A ∩ B) / P(B). In this context, let's say A represents 'it will rain tomorrow', and B is 'it is cloudy today'. Can you please translate this mathematical expression into plain English? I'd also appreciate it if you could provide a real-world example to clarify its usage. After your explanation, I'll attempt to translate my understanding back into statistical terms, and I'd like you to verify its correctness. Thank you for your help."


Sure, here are two separate templates that cover each direction of translation:

Template 1 - Converting Mathematical Expressions to Plain English:

"Hello, I'm working with the mathematical expression: [insert mathematical expression here]. If we assume that [insert any specifics or contextual details about the variables or terms involved], could you please translate this expression into plain English? It would be helpful if you could provide an example related to [insert general context or situation here] to illustrate its usage. I look forward to understanding this better. Thank you in advance for your assistance."

Template 2 - Converting Plain English to Mathematical Expressions:

"Hello, I'm trying to express the following statistical concept in mathematical terms: [insert statistical concept in plain English here]. The context is [insert any specifics or contextual details about the situation or variables involved]. Could you please translate my understanding into a proper mathematical expression or statistical notation? Once you've provided the expression, I'll try to explain it back in plain English to ensure my understanding is correct. I appreciate your help."
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

