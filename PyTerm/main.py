#PyTerm, a simple terminal write with python

#needed modules
import os, socket, shutil, sys, datetime, platform, subprocess, configparser, logging, json, itertools, threading, pathlib
from time import sleep

log = logging.basicConfig(filename="PyTerm/log.log")
dt_now = datetime.datetime.now()

 
settingsconfig = configparser.ConfigParser()
settingsconfig.add_section("settings")
settingsconfig.set("settings", "bootlog", "act")
settingsconfig.set("settings", "info", "act")
settingsconfig.read("Settings/config.ini")
settings = settingsconfig["settings"]


username = os.getlogin()
hostname = socket.gethostname()

bootlog = settings["bootlog"]
ptver=1.0


#colors
def prRed(skk): print("\033[91m{}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk))
def prBlack(skk): print("\033[98 {}\033[00m" .format(skk))

class bcolors: #2nd
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#reverse
class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'

reset = '\033[0m'

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


def shutdownhost(): os.system("shutdown /s /t 1")
def makedir(): os.mkdir(pyterm.mkdir)
def clear(): os.system('cls' if os.name == 'nt' else 'clear')
def pause(): pauseint=input("press enter to countuine . . . ")
def openfile(): subprocess.Popen(pyterm.op)
def ffcheck():
    prYellow("Checking folders")
    print("Settings")
    if os.path.exists("Settings"):
        prGreen("status: checked")
    else:
        prRed("folder not fount")
        prYellow("sending request")
        logging.critical("the folder Settings wasn't found causing PyTerm a complete shutdown")
        shutdown()

    print("PyTerm")
    if os.path.exists("PyTerm"):
        prGreen("status: checked")
    else:
        prRed("folder not fount")
        prYellow("sending request")
        logging.critical("the folder PyTerm wasn't found causing PyTerm a complete shutdown")
        shutdown()


    prYellow("checking files")
    print("config.ini")
    if os.path.exists("Settings/config.ini"):
        prGreen("status: checked")
    else: 
        prRed("file not found")
        prYellow("sending request")
        logging.critical("the file config.ini wasn't found causing PyTerm a complete shutdown")
        shutdown()

    print("log.log")
    if os.path.exists("PyTerm/log.log"):
        prGreen("status: checked")
    else: 
        prRed("file not found")
        prYellow("sending request")
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
    



def pyterm():
    logging.warn("PyTerm started, all logs are located here")
    clear()
    #appslist=os.listdir("Apps")
    commandexe=[]
    cmdslist=["get username", "get hostname", "get pythonversion", "clear", "help", "read", "check", "pause", "make dir", "del dir", "dir", "exit", "get path", "pip install", "pip uninstall", "make file", "del file", "pip list", "run pip", "pip", "term --version", "term -dis info", "term -act info", "get info", "shutdown host", "open", "run cmd", "term", "term -dis bootlog", "echo", "get cmdlog", "get errorscount", "get cmdcount", "", " ", "get errorslog", "term -act bootlog", "get ip", "run py"]
    commandexe=[]
    erroslog=[]
    errors=0
    cmdcount=0

    if settings["info"] == "act":
        print("PyTerm [version",ptver,"]\nType 'help' for more information\n")
    else:
        pass
    while True:
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
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', revpipinst])
            prGreen("installed "+revpipinst)

        elif term.__contains__("pip uninstall"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revpipuninst = term.replace("pip uninstall ", "")
            subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', revpipuninst])
            prGreen("uninstalled "+revpipinst)

        elif term.__contains__("dir/"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdir = term.replace("dir/", "")
            if os.path.exists(revdir):
                print("Directory of "+revdir+"\n")
                print('\n'.join(os.listdir(revdir)))

                print("\nLast access:", os.path.getatime(revdir))
                print("Last modification:", os.path.getmtime(revdir))
                print("Mega data:", os.path.getctime(revdir))
            else:
                prRed("No such file or directory")

        elif term.__contains__("read"):
            revread=term.replace("read ", "")
            if os.path.exists(revread):
                file = open(revread, "r")
                for each in file:
                    print(each)
                file.close()
            else:
                prRed("No such file or directory")

        elif term.__contains__("write"): 
            wrt = term.split()
            wrtfile = wrt[1]
            wrtfile1 = open(wrtfile, "w+")
            if os.path.exists(wrtfile):
                text = term.replace("write ", "")
                text1 = text.replace(wrtfile+" ", "")
                print(bcolors.WARNING + "Writing", text1 + bcolors.ENDC)
                wrtfile1.write(text1)
                prGreen("Succefully writted")
                wrtfile1.close()
                print(bcolors.HEADER+ "Closed",wrtfile+ bcolors.ENDC)
            else:
                prRed("No such file or directory")

        
        elif term.__contains__("make dir"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revmkdir = term.replace("make dir ", "")
            os.mkdir(revmkdir)
            prGreen("Created "+revmkdir)
        
        elif term.__contains__("del dir"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdeldir = term.replace("del dir ", "")
            if os.path.exists(revdeldir):
                prYellow("Deleting "+revdeldir)
                os.rmdir(revdeldir)
                prGreen("Deleted "+revdeldir)
                logging.warning(revdeldir+" deleted")
            else:
                prRed(revdeldir+" : folder not found, cannot procced to delete this folder")
                prCyan("no changes were made on the folder")
                logging.error("cannot delete the directory because it was't existing")

        elif term.__contains__("make file"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revmkfile = term.replace("make file ", "")
            prYellow("Creating "+revmkfile)
            mkfile = open(revmkfile, "w")
            prGreen("Created "+revmkfile)
            mkfile.close()

        elif term.__contains__("del file"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdelfile = term.replace("del file ", "")
            if os.path.exists(revdelfile):
                prYellow("Deleting "+revdelfile)
                os.remove(revdelfile)
                prGreen("Deleted "+revdelfile)
            else:
                prRed(revdelfile+" : file not found, cannot procced to delete this file")
                prCyan("no changes were made on the file")
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
                prRed("The file "+revrunpy+" wasn't found couldn't run the script")
                logging.critical("The file "+revrunpy+" wasn't found couldn't run the script")

        elif term.__contains__("open"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revopen = term.replace("open ", "")
            if os.path.exists(revopen):
                prYellow("opening "+revopen)
                os.startfile(revopen)
            else:
                prRed("No such file or directory")

        elif "cd" in term:
            tmp = term.split()
            commandexe.append(term)
            cmdcount = cmdcount +1
            try:
                os.chdir(tmp[1])
            except:
                prRed("No such file or directory")
                erroslog.append(term)
                errors = errors +1 


################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################


        elif term not in cmdslist:
            prRed(term+" : Not A Valid Command")
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
            prYellow("Starting process")
            ffcheck()
            prGreen("\nCheck completed\nresult: no files or folder weren't found")




        #prints count of erros
        elif term=="get errorscount":
            commandexe.append("get errorscount")
            cmdcount = cmdcount +1
            print(errors)

        
        elif term=="help":
            print("""
Commands

Every command of PyTerm


//pip
pip install <package name>                              Installs a Python package 
pip uninstall <package name>                            Uninstall a Python package
pip list                                                Makes a list of all Python packages installed
pip                                                     Makes a list of all commands in pip and usage

//get
get username                                            Prints the host username
get hostname                                            Prints the host name
get cmdlog                                              Prints the list of all executed commands
get cmdcount                                            Prints the count of commands executed
get errorslog                                           Prints the list of all invalid commands
get errorcount                                          Prints the count of errors
get pythonversion                                       Prints your current version of Python installed
get path                                                Prints the current path
get info                                                Prints info about your computer
get ip                                                  Prints you IP address

//dir
dir                                                     Makes a list of files and folders of the current path
dir/<directory>                                         Makes a list of files and folders of the writed directory

//run
run py                                                  Emulates Python IDLE (exit: ctrl+z or 'exit()')
run cmd                                                 Emulates the default terminal of the Operating System

//term
term                                                    Makes a list of all term commands and usage
term -act <setting>                                     Activates a setting
term -dis <setting>                                     Disactivates a setting
term --version                                          Prints PyTerm current version

//make
make file <name of file>                                Creates a file
make dir <name of directory>                            Creates a directory

//del
del file <name of file>                                 Deletes a file
del dir <name of directory>                             Deletes a directory


//others
exit                                                    Closes PyTerm
shutdown host                                           Shutdowns you computer
pause                                                   Stops PyTerm proccesing
open <file, directory>                                  Opens a file or a directory
clear                                                   Clears all the stuff
check                                                   Controls if all files and folders are in the PyTerm directory
cd <directory>                                          Changes the current directory
python <.py file>                                       Runs a Python script
echo <any>                                              Prints whatever you writed
write <file name> <any>                                 Writes in any kinda of file extension whatever you want
read <file name>                                        Prints what is writed on a file


File and folders

//folders

PyTerm                                                  Contains important files to make PyTerm working
Settings                                                Contains a config file with different settings
testapp                                                 Contains Python scripts and EXE apps for testing

//files
log.log                                                 Records information while PyTerm is proccesing
config.ini                                              A file used for making settings, you can change the settings using the term commands


GitHub repo: https://github.com/totallynotdrait/PyTerm

PyTerm is a project to make a terminal written in Python Programming Launguage
Thanks for using PyTerm, if you're having problems with PyTerm, view PyTerm GitHub repository
            """)



        #prints cmd count
        elif term=="get cmdcount":
            commandexe.append("get cmdcount")
            cmdcount = cmdcount +1
            print(cmdcount)

            
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

        #runs pip
        elif term=="run pip":
            commandexe.append("run pip")
            cmdcount = cmdcount +1
            prRed(term+" : Command Not Avaible At This Time")
            #pip=input(fullpip)
            #subprocess.check_call([sys.executable, '-m', pip])
                

        #get the list of alll python packages the user installed
        elif term=="pip list":
            commandexe.append("pip list")
            cmdcount = cmdcount +1
            subprocess.check_call([sys.executable, '-m', 'pip', 'list'])

        
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

            print("\nLast access:", os.path.getatime(currentdir))
            print("Last modification:", os.path.getmtime(currentdir))
            print("Mega data:", os.path.getctime(currentdir))
            
            
        
        
        #exits the script
        elif term=="exit":
            commandexe.append("exit")
            cmdcount = cmdcount +1
            prYellow("sending request")
            logging.warning("PyTerm has been closed via command 'exit'")
            shutdown()

        #shutdown your computer
        elif term=="shutdown host":
            commandexe.append("shutdown host")
            cmdcount = cmdcount +1
            prYellow("sending request")
            logging.warning("the computer has benn shutdown via command 'shutdown host'")
            shutdownhost()


        #disactivate bootlog
        elif term=="term -dis bootlog":
            editbootlog = settingsconfig["settings"]
            editbootlog["bootlog"] = "dis"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                prGreen("disactivated bootlog")

        
        elif term=="term -act bootlog":
            editbootlog = settingsconfig["settings"]
            editbootlog["bootlog"] = "act"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                prGreen("activated bootlog")

        elif term=="term -act info":
            editbootlog = settingsconfig["settings"]
            editbootlog["info"] = "act"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                prGreen("activated info")

        elif term=="term -dis info":
            editbootlog = settingsconfig["settings"]
            editbootlog["info"] = "dis"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                prGreen("disactivated info")

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
            prYellow("sending request")
            sleep(1)
            clear()
            os.system("python")


            





#get info
if __name__ == "__main__":
    if settings["bootlog"] == "act":
        bootlogdef()
        pyterm()
    else:
        pyterm()