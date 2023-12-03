# Warning: becareful running this code because it costs money every time

import csv  
import json
import pandas as pd
from argparse import ArgumentParser

from chat import LLM

api_key = "my_API_key.json"


if __name__ == "__main__":
    parser = ArgumentParser()
    args = parser.parse_args()

    # Initialize chat
    llm = LLM(api_key) 

    # Generate code from prompt
    prompt = "Write Python function to generate fibonacci sequence. Only include the function and don't include example usages."
    code = llm.generate_code(prompt)
    print(code)
