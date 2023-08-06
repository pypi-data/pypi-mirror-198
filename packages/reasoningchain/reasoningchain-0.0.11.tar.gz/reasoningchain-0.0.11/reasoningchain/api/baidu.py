#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import json
import requests
import traceback

def search_text(query, max_result_length=600):
    query = query.strip()
    if not query:
        return ""

    try:
        url = os.environ['BAIDU_SEARCH_API'] + query
        response = requests.get(url)
        if response.status_code >= 300:
            return ''
        res = json.loads(response.content)
        res_data = res['data']
        items = res_data['tplData']['asResult']['item']
        res_text = ''
        seq = 1
        res_items = []
        total_length = 0
        for i in range(min(len(items), 5)):
            if total_length >= max_result_length:
                break
            item = items[i]
            result = item.get('result', None)
            if not result:
                continue
            title = ''
            content = ''
            if 'dqa_result' in result:
                title = result['dqa_result'].get('title', '')
                content = result['dqa_result']['content']
            else:
                title = result.get('title', '')
                for k in ('abstraction', 'tts'):
                    content = result.get(k)
                    if content:
                        break
            if title or content:
                text  = f'{seq}) ' + title + '\n'
                text += content + '\n'
                res_items.append(text)
                seq += 1
                total_length += len(text)
        res_text = '\n'.join(res_items)
        if len(res_text) > max_result_length:
            return res_text[:max_result_length-3] + '...'
        return res_text
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return ""

if __name__ == '__main__':
    query = sys.argv[1]
    res = search_text(query)
    print(res)

