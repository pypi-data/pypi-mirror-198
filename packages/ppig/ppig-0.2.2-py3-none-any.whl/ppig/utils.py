import yaml
import openai
import sys    
import pyperclip
import os 
from os.path import expanduser

def load_cfg(file_path='.ppig/ppig_cfg.yaml'):
    home = expanduser("~")
    file_path = f'{home}/.ppig/ppig_cfg.yaml'
    # If file does not exist, search in local directory
    if not os.path.exists(file_path):
        print(f'Config file not found in {file_path}')
        file_path = './ppig_cfg.yaml'
        if not os.path.exists(file_path):
            print(f'Config file not found in {file_path}')
            raise Exception('Config file not found')

    # Load the yaml config file
    cfg = yaml.load(open(file_path, 'r'), Loader=yaml.FullLoader)
    return cfg

def get_api():
    # Load the config file
    cfg = load_cfg()
    # Set the API key
    openai.api_key = cfg['api_key']
    return openai

api = get_api()

def send_request(prompt):
    # Send the request to the OpenAI API
    response = api.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,        
    )
    return response


def process_prompt(prompt):
    _prompt = f"""
      Question: {prompt}
      I will answer with the command only, which is:
    """

    result = send_request(_prompt)

    return result.choices