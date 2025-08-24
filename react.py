from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num:float)->float:
    '''

    :param num: a number to triple
    :return:the triple of the input parameter
    '''

    return float(num)*3

tools=[TavilySearch(max_result=1),triple]
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0).bind_tools(tools)
    