from secret import OPENAI_API_KEY
from langchain.chat_models import ChatOpenAI

openai_api_key = OPENAI_API_KEY
chat_35_07 = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
chat_35_0 = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)
chat_35_05 = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

chat_4_1 = ChatOpenAI(
    model="gpt-4", 
    temperature=1, 
    openai_api_key=openai_api_key, 
    request_timeout=250
    )
chat_4_07 = ChatOpenAI(
    model="gpt-4", 
    temperature=0.7, 
    openai_api_key=openai_api_key, 
    request_timeout=250
    )
chat_4_05 = ChatOpenAI(
    model="gpt-4", 
    temperature=0.5, 
    openai_api_key=openai_api_key, 
    request_timeout=250
    )
chat_4_0 = ChatOpenAI(
    model="gpt-4", 
    temperature=0, 
    openai_api_key=openai_api_key, 
    request_timeout=250
    )