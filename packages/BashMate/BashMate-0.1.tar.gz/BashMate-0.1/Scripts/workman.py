from cmd import Cmd
from colorama import Fore as F, Back as B, Style as S, init
from time import sleep
import pickle
import os
import shutil

cols, rows = shutil.get_terminal_size()

init(autoreset=True)
BOLD = '\033[1m'
NORM = '\033[0m'
SYSTEM = 'Windows' if os.name == 'nt' else 'Linux' if os.name == 'posix' else 'Unknown'

CLEAR = 'cls' if SYSTEM == 'Windows' else 'clear'


if SYSTEM == 'Windows': DATABSE_PATH = rf"C:\Users\{os.getlogin()}\.custom_script_data\WorkMan.bin"
elif SYSTEM == 'Linux': DATABSE_PATH = rf"/home/{os.getlogin()}/.custom_script_data/WorkMan.bin"

if SYSTEM == 'Unknown': exit()

try:
    with open(DATABSE_PATH,'rb+') as f: 
        SYSTEM_VARS = pickle.load(f)
except:
    with open(DATABSE_PATH,'wb') as f: 
        SYSTEM_VARS = {}

def updatedb():
    try:
        with open(DATABSE_PATH,'wb+') as f: 
            pickle.dump(SYSTEM_VARS, f)
    except Exception as e:
        print(e.__traceback__) 

WSPACES = SYSTEM_VARS['WSPACES']
aliases = SYSTEM_VARS['ALIASES']

# ---------------------------------------- System Vars ----------------------------------------

# SYSTEM_VARS = {
#     "config" : config,
#     "WSPACES": WSPACES,
#     "aliases": aliases
# }

# ---------------------------------------------------------------------------------------------

# Todo: Add more Commands
# Todo: clone, chat

class Manager(Cmd):
    banner = [
                '██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███╗   ███╗ █████╗ ███╗   ██╗',
                '██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝████╗ ████║██╔══██╗████╗  ██║',
                '██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██╔████╔██║███████║██╔██╗ ██║',
                '██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║╚██╔╝██║██╔══██║██║╚██╗██║',
                '╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║ ╚═╝ ██║██║  ██║██║ ╚████║',
                ' ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝',
        ]

    # banner = [
    #     r" /\ \  __/\ \               /\ \      /'\_/`\                      ",
    #     r" \\\ \/\ \\\ \    ___   _ __\ \ \/'\ /\      \     __      ___     ",
    #     r"  \\\ \\\ \\\ \  / __`\/\`'__\ \ , < \ \ \__\ \  /'__`\  /' _ `\   ",
    #     r"   \\\ \_/ \_\ \/\ \L\ \ \ \/ \ \ \\`\\ \ \_/\ \/\ \L\.\_/\ \/\ \  ",
    #     r"    \\\ ___x___/\ \____/\ \_\  \ \_\ \_\ \_\\ \_\ \__/.\_\ \_\ \_\ ",
    #     r"    '\\/==//==/  \/___/  \/_/   \/_/\/_/\/_/ \/_/\/__/\/_/\/_/\/_/ ",
    # ]

    # banner = [
    #     f"{BOLD+F.RED}▄▄▌ ▐ ▄▌      ▄▄▄  ▄ •▄ • ▌ ▄ ·.  ▄▄▄·  ▐ ▄ ",
    #     f"{BOLD+F.BLACK}██· █▌▐█▪     ▀▄ █·█▌▄▌▪·██ ▐███▪▐█ ▀█ •█▌▐█",
    #     f"{BOLD+F.RED}██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐▀▀▄·▐█ ▌▐▌▐█·▄█▀▀█ ▐█▐▐▌",
    #     f"{BOLD+F.BLACK}▐█▌██▐█▌▐█▌.▐▌▐█•█▌▐█.█▌██ ██▌▐█▌▐█ ▪▐▌██▐█▌",
    #     f"{BOLD+F.RED} ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀·▀  ▀▀▀  █▪▀▀▀ ▀  ▀ ▀▀ █▪",
    # ]

    bannerstr = ' '*cols +'\n'+' '*cols + ('\n'.join([i.center(cols," ") for i in banner])) + '\n' + ' '*cols + '\n' + BOLD + f"{F.WHITE}Hi {F.BLUE}{ os.getlogin() },{F.WHITE} Welcome to {F.RED}WorkSpace Manager".center(cols+15)
    intro = bannerstr
    prompt = f'\n{BOLD}{F.BLUE}$ WorkMan{F.RESET} > '
    doc_header = 'Documented Commands'

    def preloop(self):
        os.system(CLEAR)

    # *-------------------------------------------------------------------------------------
    
    def do_ls(self, *args):
        'List the WorkSpaces'
        if not WSPACES: print('No Workspaces created')
        else:
            print()
            for i in sorted(WSPACES.keys(), key = lambda x: WSPACES[x]): print('- '+BOLD+F.BLUE+ i.ljust(15), "  :  ", WSPACES[i],sep = "")

    # *-------------------------------------------------------------------------------------

    def do_add(self, *args):
        try:
            key, path, *waste = args[0].split()
            path = path.replace('\\','/')
            if os.path.exists(path):
                WSPACES[key] = path
                print(f"\n{F.GREEN+BOLD}> REGISTERED : "+F.WHITE+NORM+key,path)
                # updatedb()
            else:
                print(f"\n{F.RED}X  WorkSpace Doesn't Exists")
        except:
            print(f'\n{F.RED}> Invalid Arguments')
    
    def complete_add(self, text, line, begidx, endidx):
        if len(line.split()) != 3: return []
        path = line.split()[2][:-len(text)]
        if not path: return os.listdir(path)
        return [f for f in os.listdir(path) if f.startswith(text)]

    # *-------------------------------------------------------------------------------------
    
    def do_open(self, *args):
        'Opens a Workspace'
        if not args[0]: print(F.RED+"\n X Name not supplied"); return
        name, *waste = args[0].split()
        if name in WSPACES:
            os.system(f'code {WSPACES[name]}')
            print("\n"+F.GREEN + "> WorkSpace Opened : " + F.WHITE + NORM + name)
        elif os.path.exists(name):
            os.system(f'code {name}')
            print("\n"+F.GREEN + "> Path Opened : " + F.WHITE + NORM + name)
        else: 
            print("\n"+F.RED + "> Failed to Open"+ F.WHITE + NORM + " : WorkSpace not registered")

    def complete_open(self, text, line, begidx, endidx):
        if not text: completions = WSPACES.keys()
        else: completions = [ f for f in WSPACES.keys() if f.startswith(text) ]
        return completions

    # *-------------------------------------------------------------------------------------
    
    def do_del(self, *args):
        '''Unregister a Workspace'''
        if not args[0]: print(F.RED+"\n X Name not supplied"); return
        key, *args = args[0].split()
        try:
            if key in WSPACES:
                del WSPACES[key]
                print(f"\n{F.GREEN}> WorkSpace Deleted : {key}")
            else:
                print(f"\n{F.RED}> WorkSpace Doesn't exist")
        except:
            print(f"\n{F.RED}> Invalid Arguments")
    do_rm = do_del

    # *-------------------------------------------------------------------------------------

    def do_run(self, *args):
        '''Run a workspace'''
        if not args[0]: print(F.RED+"\n X Name not supplied"); return
        key, *args = args[0].split()
        if key in WSPACES: os.system(f"cd {WSPACES[key]} && npm run dev")
        else: print(F.RED + "> Failed to Run"+ F.WHITE + NORM + " : WorkSpace not registered")

    def complete_run(self, text, line, begidx, endidx):
        if not text: completions = WSPACES.keys()
        else: completions = [ f for f in WSPACES.keys() if f.startswith(text) ]
        return completions

    # *-------------------------------------------------------------------------------------
    
    def do_cls(self, *args):
        '''Clears the terminal'''
        os.system(CLEAR)
        print(self.intro)
    do_clear = do_cls

    # *-------------------------------------------------------------------------------------

    def do_chat(self,*args):
        '''Chat with ChatGPT'''
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.system(f'python3 {file_path}/wizard.py')
        os.system(CLEAR)
        print(F.RESET+self.intro)

    # *-------------------------------------------------------------------------------------
    
    def do_sys(self,*args):
        '''Interact with System Variables'''
        for key in SYSTEM_VARS:
            if key == 'WSPACES': continue
            if type(SYSTEM_VARS[key]) == dict and len(SYSTEM_VARS[key]) == 0: continue
            print()
            print(f"{BOLD+F.BLUE}  {key} :  ",end = F.CYAN)
            if type(SYSTEM_VARS[key]) == dict:
                print()
                for i in SYSTEM_VARS[key]:
                    print(f"{BOLD+F.CYAN}      {i} : ", SYSTEM_VARS[key][i])
            else: print(SYSTEM_VARS[key])

    # *-------------------------------------------------------------------------------------
    
    def do_exit(self, *args):
        '''Close the Terminal'''
        updatedb()
        os.system(CLEAR)
        exit()
    do_quit = do_exit
    do_close = do_exit

    # *-------------------------------------------------------------------------------------

    def default(self, line):
        if line == "EOF": os.system(CLEAR); updatedb() ;quit()
        # try: os.system(line)
        # except: 
        print(f'\n{BOLD + F.RED}X Command {F.CYAN+line+F.RED} not available\n  {F.CYAN}SUGGEST HERE : {NORM + F.WHITE}https://github.com/developer-kush/CLI_Tools/issues/new')

    # *-------------------------------------------------------------------------------------
    
    def do_help(self, arg):
        commands = [
            ["ls", "Lists the currently monitored workspaces"],
            ["open <name>", "Open a workspace"],
            ["add <name> <path>", "Add a new workspace to monitor"],
            ["[rm / del] <name>", "Remove a workspace from being monitored"],
            ["[cls / clear]", "Clear the terminal screen"],
            ["run <name>", "Run a workspace based on info available"],
            ["chat","Chat with ChatGPT"],
            ["sys", "Check System Variables and Configuration"],
            ["help","Check help for the commands"],
            ["[quit / close / exit]", "Exit from this Application"],
        ]
        completables = ["open", "run"]
        print(f"\n  Hi {os.getlogin()}, Welcome to help\n  Below is a list of the commands available\n")
        for command, info in commands:
            print(f"  {F.YELLOW + BOLD}{command}".ljust(35) + f"{F.MAGENTA}{info}\n")
        print(f"{BOLD}  Tab completion available for :")
        print(f"\n  {BOLD+F.CYAN}"+ ", ".join(completables))


def main():
    try:
        manager = Manager()
        manager.cmdloop()
    except KeyboardInterrupt:
        updatedb()
        os.system(CLEAR)
        exit()

if __name__ == '__main__': main()