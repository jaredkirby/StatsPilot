from samples.test_paper import paper
from tqdm import tqdm

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)
from secret import OPENAI_API_KEY
from langchain.chat_models import ChatOpenAI
import asyncio

ai_key = OPENAI_API_KEY
chat_35_0 = ChatOpenAI( 
    openai_api_key=ai_key,
    temperature=0,
    verbose=True)

chat_4_0 = ChatOpenAI(
    model="gpt-4",
    openai_api_key=ai_key,
    temperature=0,
    verbose=True)

paper = paper

# get abstract
async def get_abstract(paper: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract only the abstract from a research paper, responding with only the abstract text, word for word.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Review the following research paper:
    {paper}
    Respond with only the abstract text, word for word.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Abstract:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    abstract = llm(formatted_answer_prompt)
    #print("Bot Response:", abstract.content)
    return abstract.content

# get abstract summary
async def get_abstract_summary(abstract: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract the key points and summarize the following Abstract from a research paper. 
    Respond with only the key points list followed by the summary text.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Abstract:
    {paper}
    Respond with only the key points list followed by the summary text.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Abstract:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    abstract_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", abstract_summary.content)
    return abstract_summary.content

# get intro
async def get_intro(paper: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract only the introduction from a research paper, responding with only the introduction text, word for word.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Review the following research paper:
    {paper}
    Respond with only the introduction text, word for word.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Introduction:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    intro = llm(formatted_answer_prompt)
    #print("Bot Response:", intro.content)
    return intro.content

# get intro summary
async def get_intro_summary(intro: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract the key points and summarize the following Introduction from a research paper. 
    Respond with only the key points list followed by the summary text.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Introduction:
    {paper}
    Respond with only the key points list followed by the summary text.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Introduction:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    intro_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", intro_summary.content)
    return intro_summary.content

# methodology
async def get_methodology(paper: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract only the methodology from a research paper, responding with only the methodology text, word for word.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Review the following research paper:
    {paper}
    Respond with only the methodology text, word for word.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Methodology:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    methodology = llm(formatted_answer_prompt)
    #print("Bot Response:", methodology.content)
    return methodology.content

# methodology summary
async def get_methodology_summary(methodology: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract the key points and summarize the following Methodology from a research paper. 
    Respond with only the key points list followed by the summary text.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Methodology:
    {paper}
    Respond with only the key points list followed by the summary text.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Methodology:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    methodology_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", methodology_summary.content)
    return methodology_summary.content

# results
async def get_results(paper: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract only the results from a research paper, responding with only the results text, word for word.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Review the following research paper:
    {paper}
    Respond with only the results text, word for word.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Results:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    results = llm(formatted_answer_prompt)
    #print("Bot Response:", results.content)
    return results.content

# results summary
async def get_results_summary(results: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract the key points and summarize the following Results from a research paper. 
    Respond with only the key points list followed by the summary text.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Results:
    {paper}
    Respond with only the key points list followed by the summary text.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Results:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    results_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", results_summary.content)
    return results_summary.content

# conclusion
async def get_conclusion(paper: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract only the conclusion from a research paper, responding with only the conclusion text, word for word.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Review the following research paper:
    {paper}
    Respond with only the conclusion text, word for word.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Conclusion:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    conclusion = llm(formatted_answer_prompt)
    #print("Bot Response:", conclusion.content)
    return conclusion.content

# conclusion summary
async def get_conclusion_summary(conclusion: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract the key points and summarize the following Conclusion from a research paper. 
    Respond with only the key points list followed by the summary text.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Conclusion:
    {paper}
    Respond with only the key points list followed by the summary text.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Conclusion:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    conclusion_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", conclusion_summary.content)
    return conclusion_summary.content

# future work
async def get_future_work(paper: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract only the future work from a research paper, responding with only the future work text, word for word.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Review the following research paper:
    {paper}
    Respond with only the future work text, word for word.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Future Work:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    future_work = llm(formatted_answer_prompt)
    #print("Bot Response:", future_work.content)
    return future_work.content

# future work summary
async def get_future_work_summary(future_work: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract the key points and summarize the following Future Work from a research paper. 
    Respond with only the key points list followed by the summary text.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Future Work:
    {paper}
    Respond with only the key points list followed by the summary text.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Future Work:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    future_work_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", future_work_summary.content)
    return future_work_summary.content

# limitations
async def get_limitations(paper: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract only the limitations from a research paper, responding with only the limitations text, word for word.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Review the following research paper:
    {paper}
    Respond with only the limitations text, word for word.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Limitations:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    limitations = llm(formatted_answer_prompt)
    #print("Bot Response:", limitations.content)
    return limitations.content

# limitations summary
async def get_limitations_summary(limitations: str):
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to extract the key points and summarize the following Limitations from a research paper. 
    Respond with only the key points list followed by the summary text.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Limitations:
    {paper}
    Respond with only the key points list followed by the summary text.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Limitations:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_35_0
    limitations_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", limitations_summary.content)
    return limitations_summary.content

async def get_summary_from_all_summaries(all_summaries: list):
    all_summaries_str = '\n'.join(all_summaries)
    sys_template = '''\
    You are a Computer Science student who specializes in Natural Language Processing and Machine Learning.
    You're task is to analyze and organize the following research paper section key points and summaries.
    '''
    sys_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    question_template=f'''\
    Summaries:
    {all_summaries_str}
    Respond with a well written summary of the paper in 2 sections:
    1. The main key points of the paper
    2. An overall summary of the paper
    Your response should be appropriate for a college level student learning about the topic for the first time.
    '''
    question_message_prompt = HumanMessagePromptTemplate.from_template(question_template)
    response_template = "Summary:"
    response_message_prompt = AIMessagePromptTemplate.from_template(response_template)
    answer_prompt = ChatPromptTemplate.from_messages(
        [
            sys_message_prompt, 
            question_message_prompt, 
            response_message_prompt,
        ]
    )
    formatted_answer_prompt = answer_prompt.format_prompt(paper=paper).to_messages()
    llm = chat_4_0
    main_summary = llm(formatted_answer_prompt)
    #print("Bot Response:", summary.content)
    return main_summary.content

# Define the function to get all summaries
async def get_all_summaries(paper: str):
    # List of functions to get each section of the paper
    section_funcs = [get_abstract, get_intro, get_methodology, get_results, get_conclusion, get_future_work, get_limitations]
    
    # List of functions to summarize each section of the paper
    summary_funcs = [get_abstract_summary, get_intro_summary, get_methodology_summary, get_results_summary, 
                     get_conclusion_summary, get_future_work_summary, get_limitations_summary]

    # Dictionary to store sections and their summaries
    sections_and_summaries = {}

    # For each pair of section and summary functions
    for section_func, summary_func in zip(section_funcs, summary_funcs):
        # Get the section and store it in the dictionary
        section = await section_func(paper)
        sections_and_summaries[section_func.__name__.replace('get_', '')] = section

        # Get the summary of the section and store it in the dictionary
        summary = await summary_func(section)
        sections_and_summaries[summary_func.__name__.replace('get_', '')] = summary

    return sections_and_summaries

# Define the main function
async def main(paper):
    # Get all summaries
    sections_and_summaries = await get_all_summaries(paper)
    
    # Get the main summary and add it to the dictionary
    sections_and_summaries['main_summary'] = await get_summary_from_all_summaries(sections_and_summaries.values())

    return sections_and_summaries

