from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def add(a:int, b:int):
    """addition function adds two numbers together"""
    return a+b

tools = [add]
model = ChatOpenAI(model = "gpt-3.5-turbo").bind_tools(tools)

def model_call(state:AgentState):
    system_prompt = SystemMessage(content = "You're AI system, please answer my query")
    response = model.invoke([system_prompt]+state['messages'])
    return {'messages':[response]}

def should_contnue(state:AgentState):
    messages = state['messages']
    last_message = messages[-1]
    if not last_message.tool_calls:
        return 'end'
    else:
        return 'continue'
    

graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)

tool_node = ToolNode(tools = tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")
graph.add_conditional_edges("our_agent", should_contnue, 
                            {"continue": "tools",
                              "end":END
                              },
                              )

graph.add_edge("tools", "our_agent")
app = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s['messages'][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {'messages': [("user", "add 3+4")]}
print_stream(app.stream(inputs, stream_mode = "values"))

