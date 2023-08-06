
__version__ = '0.0.11'

import os
import sys

from typing import Union
from langchain.callbacks.base import BaseCallbackHandler
from langchain.llms.base import BaseLLM

from . import custom_tools
from . import index
from . import cache
from . import api

def run(
        query:str,
        agent_name:str="zero-shot-react-description",
        tool_names:list=["PythonExecutor"],
        llm:BaseLLM=None,
        custom_tool_callbacks:dict=None,
        chain_callback_handler:BaseCallbackHandler=None,
    ):
    
    query = query.strip()
    if not query:
        return None

    from langchain import agents
    from langchain.callbacks import set_handler
    from langchain.llms import OpenAI,OpenAIChat

    if llm is None:
        llm = OpenAIChat(temperature=0)

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

    tools = custom_tools.load_tools(custom_tool_names, custom_tool_callbacks) + \
            agents.load_tools(predefined_tool_names)

    if chain_callback_handler is not None:
        set_handler(chain_callback_handler)

    agent = agents.initialize_agent(tools, llm, agent=agent_name, verbose=True)
    return agent.run(query)
