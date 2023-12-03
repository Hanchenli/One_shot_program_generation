import openai
import os
import json
import re
from langchain.llms import OpenAI


class LLM():
    def __init__(self, api_key):
        # Setup OpenAI key
        f = open(api_key)
        key_information = json.load(f)
        api_key = key_information['keys']
        print (api_key)
        os.environ["OPENAI_API_KEY"] = api_key

        self.llm = OpenAI(temperature=0.9)

    def generate_response(self, prompt):
        # Promp ChatGPT and obtain output
        return self.llm(prompt)

    def generate_code(self, prompt):
        # Extract code from response
        prompt += " .Please provide the code in a code block enclosed by triple backticks."
        response = self.generate_response(prompt)
        return self.extract_code(response)

    def extract_code(self, text):
        # Helper to extract code from response 
	    pattern = r"```(.*?)```"
	    match = re.search(pattern, text, re.DOTALL)
	    if match:
	    	return match.group(1).strip()
	    else:
	    	return "No code block found in the text."
