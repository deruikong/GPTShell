from langchain.agents import tool
from langchain.chat_models import ChatOpenAI
from utils import run_command, parse
import subprocess
import os

os.environ["OPENAI_API_KEY"]= "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"
llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0)

@tool
def execute_commands(commands):
    """Execute a list of commands in the shell"""
    ret = None
    for command in commands:
        while True:
            key = input(f"Running: {command}\n Explain [D] Continue [Y] Exit [N] ")
            if key.upper() == "D":
                gpt("Explain " + command)
                print(f"To understand more, run man {command}")
                # print(output.return_values["output"])
            elif key.upper() == "Y":
                cur = run_command(command)
                if cur is not None:
                    ret = cur
                break
            elif key.upper() == "N":
                print("Aborted Commands")
                return ret         

    return ret

# @tool
def gpt(inp):
    """Run GPT-3 on input"""
    print(parse(llm.invoke("Explain the following command in 2 sentences " + inp).content))
    return None

# gpt("pwd")
tools = [execute_commands]
# tools = [execute_commands, gpt]