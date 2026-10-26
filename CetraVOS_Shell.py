#CetraVOS Shell. v0.1 made 10/25/2026

import sys
from pathlib import Path
import subprocess

Version = "0.1"
Build_Data = [Version, "Core File", "Gen1"]

ShellOn = True

#clear terminal function
def clear():
    print("\033[H\033[J", end="")

def Shell():
    global ShellOn
    while ShellOn:
        a = input("> ")

        if a.lower() == "help":
            print()
            print("\033[34m---Help---\033[0m")
            print("Type 'Commands' to view commands")
            print("Your Data is Currently not saved in this version (v0.1)")

        if a.lower() == "commands":
            print()
            print("\033[34m---Commands---\033[0m")
            print("help : Get Help")
            print("commands : List of Commands")
            print("clear : Clears the terminal")
            print("open [runtime] [app]: Opens an application")
            print("apps : Prints a list of Apps")
            print("More commands coming in v0.2")
            print()

        if a.lower() == "clear":
            clear()
            print()

        if a.lower() == "apps":
            DataFile = Path(__file__).parent / "TFS.txt"
            with open(DataFile, "r") as file:
                apps = file.readlines()

                if len(apps) > 1:
                    if apps[1]:
                        print("\033[34m--Apps---\033[0m")
                        for i in apps[1].split(","):
                            print(i)
                else:
                    print("No apps")

        if "open" in a.lower():
            b = a.lower().split(" ")
            specruntime = ""

            if len(b) != 3:
                print("Error: Invalid Arguments")

            else:
                #Currently Supports: .py, .js, .java, .cs
                if b[1].lower() == "python":
                    ext = ".py"
                    rt = "python"

                if b[1].lower() == "js" or b[1].lower() == "javascript":
                    ext = ".js"
                    rt = "node"

                if b[1].lower() == "java":
                    ext = ".java"
                    rt = "java"

                #if b[1].lower() == "kotlin":
                    #ext = ".kt"
                    #rt = "kotlin"
                    #specruntime = "C#"

                if b[1].lower() == "c#" or b[1].lower() == "csharp":
                    ext = ".cs"
                    specruntime = "C#"

                else:
                    ext = "." + b[1].lower()

                if not specruntime:
                    Open = Path(__file__).parent / (b[2] + ext)
                    subprocess.run(rt, Open)

                if specruntime:
                    if specruntime == "C#":
                        Opem = Path(__file__).parent / (b[2] + ext)
                        subprocess.run(['dotnet', 'script', Open])
            






print()
Shell()