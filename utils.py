import subprocess
import os

def run_command(command):
    if command[:3] == "cd ":
        if command[3:] == "~":
            os.chdir(os.path.expanduser("~"))
        elif command[3] == "/":
            try:
                os.chdir(os.path.abspath(command[3:]))
                ret = os.getcwd()
            except Exception:
                print("cd: no such file or directory: {}".format(command[3:]))
        else:
            try:
                os.chdir(os.path.abspath(os.path.join(os.getcwd(), command[3:])))
                ret = os.getcwd()
            except Exception:
                print("cd: no such file or directory: {}".format(command[3:]))
    else:
        subprocess.run(command.split(" "))

def parse(output):
    """parse output from GPT-3, highlight code snippets"""
    
    return output

def help():
    """display help message"""
    print(
""" shellGPT - Support all shell commands as well as GPT inquiries.
    Commands:
        exit - exit shellGPT
        cd - change directory
        help - display this help message
          """)
    