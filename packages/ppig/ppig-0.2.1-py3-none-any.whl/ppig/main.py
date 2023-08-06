import sys    
import pyperclip
from ppig.utils import process_prompt, send_request



def cli_commands():
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


def prompt_directly():
    args = sys.argv[1:]
    prompt = ' '.join(args)
    choices = send_request(prompt)
    command = choices.choices[0].text
    pyperclip.copy(command.strip())
    print(f"{command}")
    print("The command has been copied to the clipboard")




    
    







