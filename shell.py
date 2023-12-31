from utils import *
from agentUtil import run
from colorama import Fore, Back, Style

def main():
    prefix = "$ "
    while True:
        inp = input(Fore.GREEN + prefix + Style.RESET_ALL)
        if inp == "exit":
            break
        elif inp == "help":
            help()
        else:
            ret = run(inp)
            if ret is not None:
                prefix = ret + "$ "


if __name__=="__main__":
    main()