#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import json
import time
import regex
import logging
import traceback
import pandas as pd
import numpy as np
from io import BytesIO
from langchain.agents import mrkl
from langchain.callbacks import set_handler as lc_set_handler
from langchain.callbacks.base import BaseCallbackHandler
#from langchain.callbacks.streamlit import StreamlitCallbackHandler

from reasoningchain.custom_tools import custom_tool, get_all_custom_tool_info, get_all_custom_tool_names, get_all_tool_names
from reasoningchain._run import run as run_rc

def render():
    import streamlit as st
    st.set_page_config(
        page_title="Reasonging Chain Is All You Need",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    def multiline_markdown(text):
        for line in text.split('\n'):
            line = line.rstrip()
            st.markdown(line)

    class CustomCallbackHandler(BaseCallbackHandler):
        @property
        def always_verbose(self) -> bool:
            """Whether to call verbose callbacks even if verbose is False."""
            return True

        def on_llm_start(self, serialized, prompts, **kwargs):
            print('on_llm_start():', serialized, prompts, kwargs)
            with st.expander(f"Calling LLM: {serialized['name']}"):
                for prompt in prompts:
                    st.write(prompt)

        def on_llm_new_token(self, token, **kwargs):
            print('on_llm_new_token():', token, kwargs)

        def on_llm_end(self, response, **kwargs):
            pass
            #print('on_llm_end():', response, kwargs)

        def on_llm_error(self, error, **kwargs):
            print('on_llm_error():', error, kwargs)

        def on_chain_start(self, info, inputs, **kwargs):
            return
            try:
                input_str = inputs["input"].strip().replace('\n', ' ')
                print(f'\x1b[33m{info["name"]}\x1b[0m(\x1b[32m{input_str}\x1b[0m)')
                st.markdown(f'{info["name"]}(`{input_str}`)')
            except:
                pass

        def on_chain_end(self, outputs, **kwargs):
            with st.container():
                if 'answer' in outputs:
                    text = outputs['answer']
                elif 'text' in outputs:
                    text = outputs['text']
                elif 'output' in outputs:
                    text = outputs['output']
                else:
                    text = ''
                st.markdown(f'Chain output:`{text}`')

        def on_chain_error(self, error, **kwargs):
            error = str(error)
            print(f'Chain error:\x1b[31m{error}\x1b[0m')
            st.caption(f'Chain error::red[{error}]')

        def on_tool_start(self, info, input_str: str, **kwargs):
            pass
            #raise RuntimeError("on_tool_start()")
            #for c in '" \n':
            #    input_str = input_str.strip(c)
            #print(f'Action:\x1b[33m{info["name"]}\x1b[0m(\x1b[32m{input_str}\x1b[0m)')
            #st.markdown(f'Action: **{info["name"]}**(`{input_str}`)')

        def on_tool_end(self, output: str, **kwargs):
            output = output.strip(' "')
            print(f'Output:\x1b[32m{output}\x1b[0m')
            if ' url:http' in output:
                pass
            elif ' gps:{' in output:
                try:
                    gpsv = output.split(':',1)[1]
                    gps = json.loads(gpsv)
                    st.markdown(f'gps:`{gpsv}`')
                    df = pd.DataFrame(
                        np.array([[gps['latitude'], gps['longitude']]]),
                        columns=['lat', 'lon'])
                    st.map(df)
                except Exception as e:
                    st.error(e)
                    traceback.print_exc(file=sys.stderr)
            else:
                st.markdown(f'**Output:** `{output}`')

        def on_tool_error(self, error, **kwargs):
            print(f'Tool error:\x1b[31m{error}\x1b[0m')

        def on_text(self, text: str, **kwargs):
            pass
            #print('Text:', text)

        def on_agent_action(self, action, **kwargs):
            try:
                tool_input = action.tool_input.strip().replace('\n', ' ')
                print(f'Action:\x1b[33m{action.tool}\x1b[0m(\x1b[32m{tool_input}\x1b[0m)')
                show_text = tool_input if f'`{tool_input}`' else ''
                st.markdown(f'Action: **{action.tool}** ({show_text})')
            except:
                print(action, kwargs)

        def on_agent_finish(self, finish, **kwargs):
            pass
            #print('on_agent_finish():', finish, kwargs)

    sthandler = CustomCallbackHandler()
    lc_set_handler(sthandler)

    @custom_tool(
        name = "TableTool",
        description = (
            "A tool for displaying data as tables. "
            "Useful for when you need to display some data in table format. "
            "Input should be the data in json format. "
        )
    )
    def table_tool(input_data:str, callback:callable=None) -> str:
        try:
            chart_data = json.loads(input_data)
            st.table(
                pd.DataFrame(
                    np.array([chart_data['x_data'], chart_data['y_data']]).T,
                    columns=[chart_data['x_name'], chart_data['y_name']],
                ))
            return "A table containing the data has been drawed successfully as you wish. "
        except Exception as e:
            traceback.print_exc(file=sys.stderr)
            st.error(f'Line chart error:{e}')
            return 'Some error occurred when drawing the line chart. '

    @custom_tool(
        name = "DrawLineChart",
        description = (
            "A tool for drawing line charts. "
            "Useful for when you need to draw a line chart with some data. "
            "Input should be the data in json format. "
        )
    )
    def draw_line_chart_tool(input_data:str, callback:callable=None) -> str:
        try:
            st.write('Drawing line chart')
            chart_data = json.loads(input_data)
            st.line_chart(
                data=pd.DataFrame(
                    np.array([chart_data['x_data'], chart_data['y_data']]).T,
                    columns=[chart_data['x_name'], chart_data['y_name']],
                ),
                x=chart_data['x_name'],
                y=chart_data['y_name'])
            return "A line chart has been drawed successfully. "
        except Exception as e:
            traceback.print_exc(file=sys.stderr)
            st.error(f'Line chart error:{e}')
            return 'Some error occurred when drawing the line chart. '

    def on_weather_result(query, weather_forcasts):
        if not weather_forcasts:
            return weather_forcasts
        #st.json(weather_forcasts)
        cols = st.columns(len(weather_forcasts))
        x, y_high, y_low = [], [], []
        for i in range(len(cols)):
            weather = weather_forcasts[i]
            x.append(weather['date'])
            y_high.append(float(weather['high_temp']))
            y_low.append(float(weather['low_temp']))
            cols[i].metric(weather['date'], weather['text_day'])

        #st.line_chart(
        #    data=pd.DataFrame(
        #        np.array([x, y_high, y_low]).T,
        #        columns=['日期', '最高气温', '最低气温'],
        #    ),
        #    x='日期',
        #    y=['最高气温','最低气温'])
        return weather_forcasts

    def on_image_result(query, url):
        st.image(url)
        return url

    def on_play_music(query, music_info):
        if not music_info:
            return music_info
        if music_info['type'] == 'video':
            st.video(music_info['url'])
        elif music_info['type'] == 'audio':
            st.audio(music_info['url'])
        return music_info

    def on_search_result(query, result):
        return result

    def on_python_executor(input_text, result):
        codes = input_text.strip()
        if codes.startswith('```'):
            codes = codes.split('\n')[1].strip()
        codes = '```Python\n' + codes
        if not codes.endswith('```'):
            codes += '\n```'

        st.caption("Python codes:")
        st.markdown(codes)
        st.markdown(f'Execution output: `{result}`')

    tool_callbacks = {
        "BaiduSearchText": on_search_result,
        "OpenaiAIPainter": on_image_result,
        'SearchImage': on_image_result,
        "WeatherForcast": on_weather_result,
        "PythonExecutor": on_python_executor,
        "Calculator": on_python_executor,
    }

    col_left, col_main, col_rght = st.columns([25,50,25])

    with col_left:
        st.empty()

    with col_main:
        st.title(":blue[ReasoningChain] Is All You Need")
        tab_chat, tab_toolbox, tab_help = st.tabs(["问答", "工具箱", "帮助"])

        #img_file_buffer = st.camera_input("Take a picture")
        with tab_chat:
            agent_name = st.selectbox("Agent:", ["zero-shot-react-description"])
            tool_options = st.multiselect(
                    "选择工具（tools）",
                    get_all_tool_names(),
                    ["BaiduSearchText","GoogleSearchImage","GoogleSearchMap","OpenaiAIPainter","WeatherForecast"])

            def assistant(query):
                query = query.strip()
                if query:
                    text = run_rc(query, tool_names=tool_options)
                    st.markdown("#### Final Answer:")
                    re = regex.compile('.* image.*: ?(https?://[^ ]*)')
                    for ans in text.split('\n'):
                        urls = re.findall(ans)
                        if len(urls) > 0:
                            for url in urls:
                                pos = ans.find(url)
                                if pos < 0:
                                    continue
                                part1 = ans[:pos]
                                part2 = ans[pos+len(url):]
                                #tts1 = get_tts(part1)
                                #tts2 = get_tts(part2)

                                st.markdown(f'{part1}')
                                #st.audio(BytesIO(tts1))
                                st.image(url)
                                st.markdown(f'{part2}')
                                #st.audio(tts2)
                        else:
                            st.markdown(f"{ans}")
                            #tts = get_tts(ans)
                            #st.audio(tts)


            def on_submit(user_question):
                t = time.strftime("%Y-%m-%d %H:%M:%S")
                with st.spinner('努力思考中 ...'):
                    with st.container():
                        assistant(user_question)

            with st.form("el_input_block"):
                user_question = st.text_input(label="问题：", placeholder="在此输入问题")
                # Every form must have a submit button.
                submitted = st.form_submit_button("提交", use_container_width=True)
                if submitted:
                    on_submit(user_question)

            with st.expander("Edit Agent's LLM Prompt:"):
                st.markdown("#### Zero Shot React Agent")
                prompt_prefix = st.text_area(label='prefix:', value=mrkl.prompt.PREFIX)
                prompt_format_instructions = st.text_area(label='format_instructions:', value=mrkl.prompt.FORMAT_INSTRUCTIONS)
                prompt_suffix = st.text_area(label='suffix:', value=mrkl.prompt.SUFFIX)
                def on_save_prompt():
                    mrkl.prompt.PREFIX = prompt_prefix
                    mrkl.prompt.FORMAT_INSTRUCTIONS = prompt_format_instructions
                    mrkl.prompt.SUFFIX = prompt_suffix
                    st.write('保存成功!')
                st.button(label="保存", on_click=on_save_prompt, use_container_width=True)

        with tab_toolbox:
            st.caption("predefined tools: https://langchain.readthedocs.io/en/latest/modules/agents/tools.html")
            with st.container():
                st.header("Custom Tools")
                for name, description in get_all_custom_tool_info().items():
                    with st.container():
                        st.markdown(f"#### {name}")
                        st.markdown(f'{description}')
        with tab_help:
            st.write("Reasoning Chain is all you need, try it!")

    with col_rght:
        st.empty()

if __name__ == '__main__':
    render()
