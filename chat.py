from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class AgentState(TypedDict):
    messages:List[HumanMessage]


llm = ChatOpenAI(model = "gpt-3.5-turbo")

def process(state:AgentState):
    response = llm.invoke(state['messages'])
    print(response)
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

User_input = input("Enter: ")
agent.invoke({"messages":[HumanMessage(content=User_input)]})
