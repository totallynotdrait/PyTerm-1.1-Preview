#PyTerm, a simple terminal write with python

#needed modules
import os, socket, shutil, sys, datetime, platform, subprocess, configparser, logging, json, itertools, threading, pathlib, winsound, webbrowser, curses
from rich.console import Console
from rich import print
from time import sleep
from rich.syntax import Syntax
from rich.progress import track
from rich.table import Column, Table
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree


table = Table(show_header=True, header_style="bold magenta")

ptver=1.1
log = logging.basicConfig(filename="sys/log.log")
dt_now = datetime.datetime.now()
console = Console()
 
settingsconfig = configparser.ConfigParser()
settingsconfig.add_section("settings")
settingsconfig.set("settings", "bootlog", "act")
settingsconfig.set("settings", "info", "act")
settingsconfig.read("Settings/config.ini")
settings = settingsconfig["settings"]


username = os.getlogin()
hostname = socket.gethostname()

bootlog = settings["bootlog"]


#definitions
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def shutdown(): print(quit())
def getlogin(): os.getlogin()
def gethostname(): socket.gethostname()
def getip():
    ip = socket.gethostbyname(hostname)
    print(ip)
def getinfo():
    print("computer name: "+os.getlogin())
    print("host name: "+socket.gethostname())
    print("IP address: "+socket.gethostbyname(hostname))
    print("python version: "+platform.python_version())

def getpythonversrion():
    pyv = platform.python_version()
    print(pyv)
def printdir():
    dire = '.'
    if len(input) > 1:
        dire = input[1]
    print('\n'.join(os.listdir(dire)))


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def shutdownhost(): os.system("shutdown /s /t 1")
def makedir(): os.mkdir(pyterm.mkdir)
def clear(): os.system('cls' if os.name == 'nt' else 'clear')
def pause(): pauseint=input("press enter to countuine . . . ")
def openfile(): subprocess.Popen(pyterm.op)
def ffcheck():
    console.print("Checking folders", style="bold green")
    print("Settings")
    if os.path.exists("Settings"):
        console.print("status: checked", style="green")
    else:
        console.print("folder not found", style="red bold")
        console.print("sending request", style="yellow")
        logging.critical("the folder Settings wasn't found causing PyTerm a complete shutdown")
        shutdown()

    print("sys")
    if os.path.exists("sys"):
        console.print("status: checked", style="green")
    else:
        console.print("folder not found", style="red bold")
        console.print("sending request", style="yellow")
        logging.critical("the folder PyTerm wasn't found causing PyTerm a complete shutdown")
        shutdown()


    console.print("Checking files", style="bold green")
    print("config.ini")
    if os.path.exists("Settings/config.ini"):
        console.print("status: checked", style="green")
    else: 
        console.print("file not found", style="red bold")
        console.print("sending request", style="yellow")
        logging.critical("the file config.ini wasn't found causing PyTerm a complete shutdown")
        shutdown()

    print("log.log")
    if os.path.exists("sys/log.log"):
        console.print("status: checked", style="green")
    else: 
        console.print("file not found", style="red bold")
        console.print("sending request", style="yellow")
        logging.critical("the file log.log wasn't found causing PyTerm a complete shutdown")
        shutdown()
def bootlogdef():
    clear()
    osplatform = sys.platform
    getpythonversrion()
    print("Using", osplatform)
    print("Access:", dt_now)
    print("Name:",__name__)
    sleep(2)
    ffcheck()
    sleep(1)
    clear()
def cmds():
    table.add_column("Commands", style="dim", width=60)
    table.add_column("Description", style="dim", width=100)
    table.add_row("[yellow]pip[/yellow] install [blue]<any>[/blue]", "Installs a Python package")
    table.add_row("[yellow]pip[/yellow] uninstall [blue]<any>[/blue]", "Uninstalls a Python package")
    table.add_row("[yellow]pip[/yellow] list", "Makes a list of all Python packages installed")
    table.add_row("[yellow]pip[/yellow]", "Makes a list of all commands in pip and usage")
    table.add_row(" ", " ")
    table.add_row("[yellow]get[/yellow] [blue]<username, hostname, cmdlog, cmdcount, errorslog, errorscount, pythonversion, path, info, ip>[/blue]", "Prints information about your computer or PyTerm")
    table.add_row(" ", " ")
    table.add_row("[yellow]dir[/yellow]", "Make a list of the files and folders of the current path")
    table.add_row("[yellow]dir/[/yellow][blue]<any>[/blue]", "Make a list of the files and folders of the choosen path")
    table.add_row(" ", " ")
    table.add_row("[yellow]run[/yellow] [blue]<py, cmd>[/blue]", "Emulates Python IDLE or your default Terminal (exit for Python IDLE: [blue]ctrl+z[/blue] [violet]or[/violet] [green]'exit()'[/green]")
    table.add_row(" ", " ")
    table.add_row("[yellow]make[/yellow] [blue]<file, dir>[/blue] [blue]<any>[/blue]", "Creates a file or directory to the current path")
    table.add_row(" ", " ")
    table.add_row("[yellow]del[/yellow] [blue]<file, dir>[/blue] [blue]<any>[/blue]", "Deletes a file or directory")
    table.add_row(" ", " ")
    table.add_row("[yellow]del[/yellow] [blue]<file, dir>[/blue] [blue]<any>[/blue]", "Deletes a file or directory")
    table.add_row(" ", " ")
    table.add_row("[yellow]exit[/yellow]", "Shutdowns PyTerm")
    table.add_row("[yellow]shutdown[/yellow] [blue]host[/blue]", "Shutdowns your computer")
    table.add_row("[yellow]pause[/yellow]", "Stops PyTerm procces")
    table.add_row("[yellow]open[/yellow] [blue]<file, dir>[/blue]", "Opens a file or folder")
    table.add_row("[yellow]clear[/yellow]", "Clears output")
    table.add_row("[yellow]check[/yellow]", "Check if all folders and files of PyTerm exitst")
    table.add_row("[yellow]cd[/yellow] [blue]<dir>[/blue]", "Changes current path")
    table.add_row("[yellow]python[/yellow] [blue]<.py file>[/blue]", "Runs a Python script")
    table.add_row("[yellow]echo[/yellow] [blue]<any>[/blue]", "Prints what the user typed")
    table.add_row("[yellow]write[/yellow] [blue]<file>[/blue] [blue]<any>[/blue]", "Writes to the choosen file what the user typed")
    table.add_row("[yellow]read[/yellow] [blue]<file>[/blue]", "Reads what is writen on a file")
cmds()


def pyterm():
    global revpipuninst
    logging.warn("PyTerm started, all logs are located here")
    clear()
    #appslist=os.listdir("Apps")
    commandexe=[]
    cmdslist=["get username", "get hostname", "get pythonversion", "clear", "run ptx", "rich", "beep", "help", "cat", "clone", "tree", "read", "check", "pause", "make dir", "del dir", "dir", "exit", "get path", "pip install", "pip uninstall", "make file", "del file", "pip list", "run pip", "pip", "term --version", "term -dis info", "term -act info", "get info", "shutdown host", "open", "run cmd", "term", "term -dis bootlog", "echo", "get cmdlog", "get errorscount", "get cmdcount", "", " ", "get errorslog", "term -act bootlog", "get ip", "run py"]
    commandexe=[]
    erroslog=[]
    errors=0
    cmdcount=0

    if settings["info"] == "act":
        print("PyTerm [version",ptver,"]\nType 'help' for more information\n")
    else:
        pass

    import sys
    osplatform = sys.platform
    pyv = platform.python_version()
    console.print("[dodger_blue2] ⢠⣿⣿⠿⢿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⣿⣿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[/dodger_blue2]",)
    console.print("[dodger_blue1] ⢸⣿⡇⠀⠀⣿⣿⡇⢸⣿⡇⠀⠀⣾⣿⠇⠀⠀⢀⣿⣿⠀⠀⠀⠀⣰⣾⠿⢿⣷⡆⠀⢀⣿⣿⣰⣾⡇⢀⣿⣿⣶⣿⣿⣆⣰⣾⣿⣷[/dodger_blue1]"+"    [blue]PyTerm[/blue]", ptver)
    console.print("[deep_sky_blue3] ⣿⣿⣧⣤⣶⣿⠟⠁⠘⣿⣇⠀⣼⡿⠃⠀⠀⠀⢸⣿⡇⠀⠀⠀⣾⣿⣥⣤⣤⣿⣿⠀⢸⣿⡟⠉⠉⠁⢸⣿⠏⠀⢸⣿⡏⠁⠀⣿⣿[/deep_sky_blue3]"+"    [blue]Python[/blue]", pyv)
    console.print("[turquoise4]⣴⣿⡟⠉⠉⠀⠀⠀⠀⠀⣿⣿⣾⡿⠁⠀⠀⠀⢀⣿⣿⠁⠀⠀⠀⣿⣯⡉⠉⠉⣉⠁⠀⣿⣿⠁⠀⠀⠀⣿⣿⠀⠀⣼⣿⠃⠀⢸⣿⡇[/turquoise4]"+"    [blue]Using [/blue]"+ "[dark_slate_gray2]"+osplatform+"[/dark_slate_gray2]")
    console.print("[dark_cyan]⠿⡿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠀⠀⠀⠀⠀ ⠿⠏⠀⠀⠀⠀⠈⠿⣿⣿⡿⠿⠀⠸⠿⠇⠀⠀⠀⠸⠿⠇⠀⠀⠿⠿⠀⠀⠾⠿⠁[/dark_cyan]"+"    [black]██[/black][red]██[/red][green]██[/green][yellow]██[/yellow][blue]██[/blue][magenta]██[/magenta][cyan]██[/cyan][white]██[/white][bright_black]██[/bright_black][bright_red]██[/bright_red][bright_green]██[/bright_green][bright_yellow]██[/bright_yellow][bright_blue]██[/bright_blue][bright_magenta]██[/bright_magenta][bright_cyan]██[/bright_cyan][bright_white]██[/bright_white]")
    console.print("[spring_green4] ⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[/spring_green4]\n")
    while True:
        try:
            import playsound
        except ImportError:
            console.print("Trying to Install required module: playsound\n", style="bold red")
            os.system('python -m pip install playsound')
        import playsound

        nilpath = os.path.abspath(__file__)
        currentdir = os.path.basename(os.getcwd()) or "/"
        path = os.path.dirname(__file__)
    
        fullname = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.OKBLUE+"/"+currentdir+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "
        fullpip = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.OKBLUE+"/pip"+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "
        fullcmd = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.OKBLUE+"/cmd"+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "
        fullecho = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.OKBLUE+"/echo"+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "

        term=input(fullname)

        #check if user input a wrong command

        if term.__contains__("pip install"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revpipinst = term.replace("pip install ", "")
            os.system("pip3 install "+revpipinst)
            console.print("installed "+revpipinst, style="green")

        elif term.__contains__("pip uninstall"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revpipuninst = term.replace("pip uninstall ", "")
            os.system("pip3 uninstall "+revpipuninst)
            console.print("Uninstalled "+ revpipuninst, style="green")

        elif term.__contains__("dir/"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdir = term.replace("dir/", "")
            if os.path.exists(revdir):
                print("Directory of "+revdir+"\n")
                print('\n'.join(os.listdir(revdir)))
            else:
                console.print("No such file or directory", style="bold red")

        elif "clone" in term:
            revclone = term.replace("clone ", "")
            if os.path.exists(revclone):
                console.print("Cloning "+revclone+" in "+currentdir, style="yellow")
                for step in track(range(100)):
                    shutil.copy(revclone, "clone_"+revclone)
                console.print("Cloned "+revclone, style="green")

        elif term.__contains__("read"):
            revread=term.replace("read ", "")
            if os.path.exists(revread):
                file = open(revread, "r")
                for each in file:
                    print(each)
                file.close()
            else:
                console.print("No such file or directory", style="bold red")

        elif "su" in term:
            revsu=term.replace("su ", "")
            

        elif term.__contains__("write"): 
            wrt = term.split()
            wrtfile = wrt[1]

            def main(stdscr):
                s = curses.initscr(); s.nodelay(1); curses.noecho(); curses.raw(); s.keypad(1)
                b = []; src = wrtfile; R, C = s.getmaxyx(); x, y, r, c = [0] * 4
                if len(sys.argv) == 2: src = sys.argv[1]
                try:
                    with open(sys.argv[1]) as f:
                        cont = f.read().split('\n'); cont = cont[:-1] if len(cont) > 1 else cont
                        for rw in cont: b.append([ord(c) for c in rw])
                except: b.append([])
                if len(sys.argv) == 1: b.append([])
                while True:
                    s.move(0, 0)
                    if r < y: y = r
                    if r >= y + R: y = r - R+1
                    if c < x: x = c
                    if c >= x + C: x = c - C+1
                    for rw in range(R):
                        brw = rw + y
                        for cl in range(C):
                            bcl = cl + x
                            try: s.addch(rw, cl, b[brw][bcl])
                            except: pass
                    s.clrtoeol()
                    try: s.addch('\n')
                    except: pass
                    curses.curs_set(0); s.move(r-y, c-x); curses.curs_set(1); s.refresh(); ch = -1
                    while (ch == -1): ch = s.getch()
                    if ch != ((ch) & 0x1f) and ch < 128: b[r].insert(c, ch); c += 1
                    elif chr(ch) in '\n\r': l = b[r][c:]; b[r] = b[r][:c]; r += 1; c = 0; b.insert(r, [] + l)
                    elif ch in [8, 263]:
                        if c: c -= 1; del b[r][c]
                    elif r: l = b[r][c:];  del b[r]; r -= 1; c = len(b[r]); b[r] += l
                    elif ch  == curses.KEY_LEFT:
                        if c != 0: c -= 1
                    elif r > 0: r -= 1; c = len(b[r])
                    elif ch == curses.KEY_RIGHT:
                        if c < len(b[r]): c += 1
                    elif r < len(b)-1: r += 1; c = 0
                    elif ch == curses.KEY_UP and r != 0: r -= 1
                    elif ch == curses.KEY_DOWN and r < len(b)-1: r += 1
                    rw = b[r] if r < len(b) else None; rwlen = len(rw) if rw is not None else 0
                    if c > rwlen: c = rwlen 
                    if ch == (ord('q') & 0x1f): sys.exit()
                    elif ch == (ord('s') & 0x1f):
                        cont = ''
                        for l in b: cont += ''.join([chr(c) for c in l]) + '\n'
                        with open(src, 'w') as f: f.write(cont)
            curses.wrapper(main)

        
        elif term.__contains__("make dir"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revmkdir = term.replace("make dir ", "")
            for step in track(range(100)):
                pass
            os.mkdir(revmkdir)
            console.print("Created "+revmkdir, style="green")
        
        elif term.__contains__("del dir"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdeldir = term.replace("del dir ", "")
            if os.path.exists(revdeldir):
                console.print("Deleting "+revdeldir, style="yellow")
                for step in track(range(100)):
                    pass
                os.rmdir(revdeldir)
                console.print("Deleted "+revdeldir, style="green")
                logging.warning(revdeldir+" deleted")
            else:
                console.print(revdeldir+" : folder not found, cannot procced to delete this folder", style="bold red")
                console.print("No changes were made in the folder", style="cyan")
                logging.error("cannot delete the directory because it was't existing")

        elif term.__contains__("make file"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revmkfile = term.replace("make file ", "")
            console.print("Creating "+revmkfile, style="yellow")
            for step in track(range(100)):
                mkfile = open(revmkfile, "w")
            console.print("Created "+revmkfile, style="green")
            for step in track(range(100)):
                mkfile.close()

        elif term.__contains__("del file"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdelfile = term.replace("del file ", "")
            if os.path.exists(revdelfile):
                console.print("Deleting "+revdelfile, style="yellow")
                for step in track(range(100)):
                    pass
                os.remove(revdelfile)
                console.print("Deleted "+revdelfile, style="green")
            else:
                console.print(revdelfile+" : file not found, cannot procced to delete this folder", style="bold red")
                console.print("No changes were made in the file", style="cyan")
                logging.error("cannot delete the file because it was't existing")

        elif term.__contains__("echo"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revecho = term.replace("echo ", "")
            print(revecho)

        elif term.__contains__("python"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revrunpy = term.replace("python ", "")
            fullpy = "python "+revrunpy
            if os.path.exists(revrunpy):
                os.system(fullpy)
            else:
                console.print("The file "+revrunpy+" wasn't found couldn't run the script", style="red bold")
                logging.critical("The file "+revrunpy+" wasn't found couldn't run the script")

        elif term.__contains__("open"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revopen = term.replace("open ", "")
            if term.__contains__("www.") or term.__contains__(".com"):
                for step in track(range(100)):
                    webbrowser.open(revopen)
            elif os.path.exists(revopen):
                if osplatform == "linux":
                    for step in track(range(100)):
                        os.system("open "+revopen)
                elif osplatform == "darwin":
                    for step in track(range(100)):
                        os.system("open "+revopen)
                else:
                    for step in track(range(100)):
                        os.startfile(revopen)
            else:
                console.print("No such file or directory", style="red bold")

        elif "cd" in term:
            tmp = term.split()
            commandexe.append(term)
            cmdcount = cmdcount +1
            try:
                os.chdir(tmp[1])
            except:
                console.print("No such file or directory", style="red bold")
                erroslog.append(term)
                errors = errors +1 
        
        elif "play" in term:
            revplay = term.replace("play ", "")
            if os.path.exists(revplay):
                console.print("Playing "+revplay, style="green")
                playsound.playsound(revplay)
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################


        elif term not in cmdslist:
            console.print(term+" : Not A Valid Command", style="red bold")
            erroslog.append(term)
            errors = errors +1
            logging.error(term+" : the command was not found to the cmdslist, couldn't run the command")


        #get pc username    
        elif term=="get username":
            commandexe.append("get username")
            cmdcount = cmdcount +1
            print(username)

        #print all commands exe
        elif term=="get cmdlog":
            commandexe.append("get commandlog")
            cmdcount = cmdcount +1
            print(commandexe)

        elif term=="check":
            console.print("Starting process", style="yellow")
            ffcheck()
            console.print("\nCheck completed\nresult: no files or folder weren't found", style="green")

        #prints count of erros
        elif term=="get errorscount":
            commandexe.append("get errorscount")
            cmdcount = cmdcount +1
            print(errors)



        #prints cmd count
        elif term=="get cmdcount":
            commandexe.append("get cmdcount")
            cmdcount = cmdcount +1
            print(cmdcount)

        elif term=="run ptx":
            commandexe.append(term)
            cmdcount = cmdcount +1
            os.system("python3 ptx.py")

            
        #prints cmd count
        elif term=="get errorslog":
            commandexe.append("get errorslog")
            cmdcount = cmdcount +1
            print(erroslog)

        #get pc hostname
        elif term=="get hostname":
            commandexe.append("get hostname")
            cmdcount = cmdcount +1
            print(hostname)


        #get python version
        elif term=="get pythonversion":
            commandexe.append("get pythonversion")
            cmdcount = cmdcount +1
            getpythonversrion()


        #print the current path is the user
        elif term=="get path":
            commandexe.append("get path")
            cmdcount = cmdcount +1
            print(nilpath)
            print(path)
            print(currentdir)

        elif term=="help":
            console.print(table)
            print("GitHub repo: https://github.com/totallynotdrait/PyTerm\n")
            print("PyTerm is a project to make a terminal written in Python Programming Launguage\nThanks for using PyTerm, if you're having problems with PyTerm, view PyTerm GitHub repository")
        


        #gets user ip
        elif term=="get ip":
            commandexe.append("get ip")
            cmdcount = cmdcount +1
            getip()


        #gets user info
        elif term=="get info":
            commandexe.append("get info")
            cmdcount = cmdcount +1
            getinfo()

        #gets info about pip
        elif term=="pip":
            commandexe.append("pip")
            cmdcount = cmdcount +1
            subprocess.check_call([sys.executable, '-m', 'pip'])

        elif term=="beep":
            commandexe.append("beep")
            cmdcount = cmdcount +1
            winsound.Beep(1000,600)

                

        #get the list of alll python packages the user installed
        elif term=="pip list":
            commandexe.append("pip list")
            cmdcount = cmdcount +1
            os.system("pip3 list")

        
        #run command prompt
        elif term=="run cmd":
            commandexe.append("run cmd")
            cmdcount = cmdcount +1
            while True:
                cmd=input(fullcmd)
                if cmd=="exit":
                    break
                os.system(cmd)

        #clears any prints and inputs
        elif term=="clear":
            commandexe.append("clear")
            cmdcount = cmdcount +1
            clear()


        #does a pause
        elif term=="pause":
            commandexe.append("pause")
            cmdcount = cmdcount +1
            pause()

        #prints all files and folders that are in the current directory
        elif term=="dir":
            commandexe.append("dir")
            cmdcount = cmdcount +1
            print("Directory of "+currentdir+"\n")
            print('\n'.join(os.listdir()))
            
        #exits the script
        elif term=="exit":
            commandexe.append("exit")
            cmdcount = cmdcount +1
            console.print("Sending request", style="yellow")
            logging.warning("PyTerm has been closed via command 'exit'")
            shutdown()

        #shutdown your computer
        elif term=="shutdown host":
            commandexe.append("shutdown host")
            cmdcount = cmdcount +1
            console.print("Sending request", style="yellow")
            logging.warning("the computer has benn shutdown via command 'shutdown host'")
            shutdownhost()


        #disactivate bootlog
        elif term=="term -dis bootlog":
            editbootlog = settingsconfig["settings"]
            editbootlog["bootlog"] = "dis"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                console.print("Disactivated bootlog", style="green")

        
        elif term=="term -act bootlog":
            editbootlog = settingsconfig["settings"]
            editbootlog["bootlog"] = "act"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                console.print("Activated bootlog", style="green")

        elif term=="term -act info":
            editbootlog = settingsconfig["settings"]
            editbootlog["info"] = "act"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                console.print("Activated info", style="green")

        elif term=="term -dis info":
            editbootlog = settingsconfig["settings"]
            editbootlog["info"] = "dis"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                console.print("Disactivated info", style="green")

        elif term=="term":
            print("\nusage:")
            print(" term <command> [options]")
            print("\ncommands:")
            print(" -act            Activates a option")
            print(" -dis            Disactivates a option")
            print("\n")
            print("options:")
            print(" bootlog         Prints information and check files and folders if does exists")
            print(" info            Prints some information about the computer")

        elif term=="term --version":
            print(ptver)

        elif term=="run py":
            console.print("Sending request", style="yellow")
            sleep(1)
            clear()
            os.system("python")

        elif term=="cat":
            if currentdir == "sys":
                os.startfile("gatto.gif")
            else:
                console.print("You're not in the 'sys' folder", style="red bold")


            





#get info
if __name__ == "__main__":
    if settings["bootlog"] == "act":
        bootlogdef()
        pyterm()
    else:
        pyterm()