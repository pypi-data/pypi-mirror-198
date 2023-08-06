__version__ = '0.0.12'

import os
import sys

from typing import Union
from langchain.callbacks.base import BaseCallbackHandler
from langchain.llms.base import BaseLLM

from . import custom_tools
from . import index
from . import cache
from . import api

def get_all_tool_names():
    from langchain import agents
    return custom_tools.get_all_custom_tool_names() + agents.get_all_tool_names()

def load_tools(tool_names:list, tool_callbacks:dict=None, llm:BaseLLM=None) -> list:
    from langchain import agents

    custom_tool_names = []
    predefined_tool_names = []
    all_agent_tool_names = agents.get_all_tool_names()
    for name in tool_names:
        if name in custom_tools.get_all_custom_tool_names():
            custom_tool_names.append(name)
        elif name in all_agent_tool_names:
            predefined_tool_names.append(name)
        else:
            raise RuntimeError(f"Unknown tool name:[{name}]")

    tools = []
    if len(custom_tool_names) > 0:
        tools += custom_tools.load_tools(custom_tool_names, tool_callbacks)

    if len(predefined_tool_names) > 0:
        from langchain.llms import OpenAI, OpenAIChat
        if llm is None:
            llm = OpenAI(temperature=0)
        tools += agents.load_tools(predefined_tool_names, llm)

    return tools

def run(
        query:str,
        agent_name:str="zero-shot-react-description",
        tool_names:list=["PythonExecutor"],
        llm:BaseLLM=None,
        tool_callbacks:dict=None,
        chain_callback_handler:BaseCallbackHandler=None,
    ):
    
    query = query.strip()
    if not query:
        return None

    from langchain import agents
    from langchain.callbacks import set_handler
    from langchain.llms import OpenAI, OpenAIChat

    if llm is None:
        llm = OpenAIChat(temperature=0)

    tools = load_tools(tool_names, tool_callbacks)

    if chain_callback_handler is not None:
        set_handler(chain_callback_handler)

    agent = agents.initialize_agent(tools, llm, agent=agent_name, verbose=True)
    return agent.run(query)
