# Mini virtual OS. v0.1 made 10/25/2026
#This is the Core file
from pathlib import Path
import time
import sys
import subprocess

Version = "0.1"
Build_Data = [Version, "Core File", "Gen1"]

SystemsFound = 0

#clear terminal function
def clear():
    print("\033[H\033[J", end="")



#Checks that the Core Framework Exists
def bootup():
    global SystemsFound
    global Version
    coremodules = []
    print()
    print(f"\033[34m--- CetraByte Virtual OS {Version} ---\033[0m")

    bootupmessage = ["\033[32mRunning system checks\033[0m", ".", ".", "."]

    for i in bootupmessage:
        print(i, end="", flush=True)
        time.sleep(0.75)
    print()
    print()
    

    file_path = Path(__file__).parent / "CetraVOS_Shell.py"
    if file_path.is_file():
        SystemsFound += 1
        coremodules.append("CetraVOS_Shell.py")




    if SystemsFound < 1:
        print("\033[31mBootup Failed: \033[0m")
        if not "CetraVOS_Shell" in coremodules:
            print("\033[31mCetraVOS_Shell Missing\033[0m")
            print("^^^^^^^^^^^^^^^^^^")

        time.sleep(1)
        print()
        print("\033[31mYour Version of CetraVOS is likely corrupted\033[0m")
        print("You can redownload at:")
        print("GitHub.com/Cetri12/CetraVOS")
        print()

    else:
        print()
        clear()

        #checks that the .txt is set up
        DataFile = Path(__file__).parent / "TFS.txt"
        with open(DataFile, "r") as file:
            lines = file.readlines()
            if len(lines) > 0:
                if lines[0] != "1":
                    print("...")
            else:
                print()

        Shell = Path(__file__).parent / "CetraVOS_Shell.py"
        subprocess.run(["python", Shell])
bootup()

#Structure of TFS.txt:
#is setup (0/1)
#apps list
