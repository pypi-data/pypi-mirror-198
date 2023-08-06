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

def process_prompt(prompt):
    _prompt = f"""
      Question: {prompt}
      I will only ansert with the command, which is:
    """

    result = api.Completion.create(
        engine="text-davinci-003",
        prompt=_prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,        
    )

    return result.choices

def main():
    # Parse arguments from the command line
    args = sys.argv[1:]

    # Check if the user provided a prompt
    if len(args) == 0:
        print("Please provide a prompt")
        return
    
    # Join the prompt 
    prompt = ' '.join(args)

    # Process the prompt
    choices = process_prompt(prompt)

    # Print the result
    command = choices[0].text
    
    # COpy the result to the clipboard
    pyperclip.copy(command.strip())
    print(f"{command}")
    print("The command has been copied to the clipboard")



    
    
        

    


if __name__ == "__main__":
    main()

    
    







