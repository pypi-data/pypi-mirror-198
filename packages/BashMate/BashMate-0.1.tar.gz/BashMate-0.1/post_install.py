import os
import sys
import pickle

LINE = '---------------------------------------------------------------------------'

def install_workman(PATH):

    print(f'\n\n{LINE}\n\nInstalling WorkMan ...')
    try:
        DATA_PATH = PATH + "WorkMan.bin"
        INITIAL_DATA = {
            'WSPACES': {},
            'ALIASES': {},
            'SCRIPTS': {}
        }
        if os.path.exists(DATA_PATH):
            if input('System Vars Already present. RECREATE ? [y/n] : ') in 'yes':
                with open(DATA_PATH, 'wb+') as f: pickle.dump(INITIAL_DATA, f)
        else: 
            with open(DATA_PATH, 'wb+') as f: pickle.dump(INITIAL_DATA, f)

        print("\nWorkMan Installed !!")
    except:
        print("\n\nWizard could not be Installed")

def install_wizard(PATH):

    print(f'\n\n{LINE}\n\nInstalling Wizard ...')

    try:
        DATA_PATH = PATH + "Wizard.bin"
        CHATS_PATH = PATH + "Wiz_Chats/"
        if not os.path.isdir(CHATS_PATH): os.mkdir(CHATS_PATH)

        API_KEY = input("\nEnter your ChatGPT API key ... \nGet yours at : https://platform.openai.com/account/api-keys\nEnter : ").strip()

        INITIAL_DATA = {
            'API_KEY': API_KEY, 
            'CHATS': set(os.listdir(CHATS_PATH))
        }

        if os.path.exists(DATA_PATH):
            if input('System Vars Already present. RECREATE ? [y/n] : ') in 'yes':
                with open(DATA_PATH, 'wb+') as f: pickle.dump(INITIAL_DATA, f)
        else: 
            with open(DATA_PATH, 'wb+') as f: pickle.dump(INITIAL_DATA, f)

        print("\nWizard Installed !!")
    except: print("\n\nWorkMan could not be Installed")

def post_install():

    if os.name == 'nt': PATH = f"C:/Users/{os.getlogin()}/.custom_script_data/"
    elif os.name == 'posix': PATH = f"/home/{os.getlogin()}/.custom_script_data/"
    else: sys.exit("OS not supported")

    if not os.path.exists(PATH): os.mkdir(PATH)

    choice = input("""Configure which tool\n1        : WorkMan\n2.       : Wizard\ndefault  : All\nCtrl + C : Stop\nEnter : """)

    if choice == '1':
        install_workman(PATH)
    elif choice == '2':
        install_wizard(PATH)
    else:
        install_workman(PATH)
        install_wizard(PATH)

# post_install()