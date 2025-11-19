import os
import asyncio
import json
import requests
import urllib3
import certifi
import openai
import logging
import sys
import re
import time
import pandas as pd
import numpy as np
from constants.constants import Constants as constants
from services.get_a2a_token_v1 import get_auth_token
from utils.processor import discover_unstructured


def validate_json_structure(json_object):
    try:
        # Parse the input as JSON
        data = json.loads(json_object)

        # Check that it's a dictionary
        if not isinstance(data, dict):
            return False
        
        # Check required keys
        if "reasoning" not in data:
            return False
        if "answer" not in data:
            return False

        return True

    except json.JSONDecodeError as e:
        return False


system_prompt = """Please act as a puzzle solver and solve the word puzzle problem step by step. 
Output the reasoning steps leading to the final conclusion. Output the final answer, taking into account the reasoning steps. Make sure the answer only contain the final character string.
"""


structured_output = [
{
    "type": "function",
    "function": {
        "name": "structured_output",
        "description": "Output the reasoning steps leading to the final conclusion. Output the final answer, taking into account the reasoning steps. Make sure the answer only contain the final character string.",
        "parameters": {
            "type": "object",
            "properties": {
                "reasoning": {
                    "type": "string",
                    "description": "The reasoning steps leading to the final conclusion.",
                },
                "answer": {
                    "type": "string",
                    "description": "The final answer, taking into account the reasoning steps. Make sure the answer only contain the final character string.",
                },
            },
            "required": ["reasoning", "answer"]
        }
    }
}
]


def gpt_generation(problem):
    response = openai.ChatCompletion.create(
        engine=constants.AZURE_DEPLOYMENT_NAME_4,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": problem}
        ],
        tools=structured_output,
        tool_choice={"type": "function", "function": {"name": "structured_output"}}
    )
    final_response = response.choices[0].message["tool_calls"][0]["function"]["arguments"]

    if not validate_json_structure(final_response):
        print("JSON format failed; Regenerate answer")
        final_response = gpt_generation(problem)
    print("JSON format passed; Output answer")
    return final_response


with open('data/ellc_4_words_revised.json') as json_data:
    data = json.load(json_data)
results = []
for i in range(len(data)):
    print(f"The current sample id is {i}")
    if i % 5 == 0:
            # Access GPT-4o
            print("Refresh to avoid the api calling limit per conversation")
            auth_token_coro = get_auth_token()
            token = asyncio.run(auth_token_coro)
            print(token)
            auth_token = "Bearer " + token[0].get("authorization_token")
            openai.api_key = auth_token
            openai.api_base = constants.EAG_AZURE_SECURE_ENDPOINT

    words_tmp = '"' + data[i]['sampled_words'][0] + ' ' + data[i]['sampled_words'][1] + ' ' + data[i]['sampled_words'][2] + ' ' + data[i]['sampled_words'][3] + '"'
    problem = 'Take the last letters of each words in ' + words_tmp + ' and rearrange these selected letters to form a valid English word, using each letter exactly once. What is the word?'
    final_response_tmp_js = gpt_generation(problem)
    final_response_tmp_js = json.loads(final_response_tmp_js)
    results.append(final_response_tmp_js)


with open(f"ellc_results/test_4_last_function.json", "w") as f:
    json.dump(results, f)