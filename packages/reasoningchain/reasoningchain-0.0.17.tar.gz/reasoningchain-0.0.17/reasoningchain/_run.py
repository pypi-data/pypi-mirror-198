#!/usr/bin/env python3

import os
import sys
import click
from reasoningchain.custom_tools.base import get_all_tool_names, load_tools

from langchain.callbacks.base import BaseCallbackHandler
from langchain.llms.base import BaseLLM
from langchain.llms import OpenAI, OpenAIChat

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

    if llm is None:
        llm = OpenAIChat(temperature=0)

    tools = load_tools(tool_names, tool_callbacks, llm=llm)

    if chain_callback_handler is not None:
        set_handler(chain_callback_handler)

    agent = agents.initialize_agent(tools, llm, agent=agent_name, verbose=True)
    return agent.run(query)

@click.command()
@click.option("--query", "-q", "query", type=str, required=True)
@click.option("--tools", "-t", "tool_names", type=str, default="BaiduSearchText", required=False)
@click.option("--llm",   "-m", "llm_name", type=str, default="OpenAIChat", required=False)
@click.option("--agent", "-g", "agent_name", type=str, default="zero-shot-react-description", required=False)
def cli(query:str, tool_names:str, llm_name:str, agent_name:str) -> int:
    tool_name_list = tool_names.split(",")
    if not llm_name:
        llm_name == 'OpenAIChat'
    if llm_name == 'OpenAIChat':
        llm = OpenAIChat(temperature=0)
    else:
        llm = None
    answer = run(query=query, agent_name=agent_name, tool_names=tool_name_list, llm=llm)

    print(f" Query:\x1b[33m{query}\x1b[0m")
    print(f"Params:tools=[\x1b[33m{tool_names}\x1b[0m]\tllm=[\x1b[33m{llm_name}\x1b[0m]\tagent=[\x1b[33m{agent_name}\x1b[0m]")
    print(f"Answer:\x1b[1;32m{answer}\x1b[0m")
    return 0

if __name__ == '__main__':
    sys.exit(cli())

