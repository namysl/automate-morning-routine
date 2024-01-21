import subprocess
import time
import webbrowser
import os

# Apps and their paths
chrome_single_slash = "C:/Program Files/Google/Chrome/Application/chrome.exe"
all_apps_to_be_opened = {"chrome" : "C:\\Program Files\Google\Chrome\Application\chrome.exe",
                         "outlook" : "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
                         "notepad++" : "C:\\Program Files (x86)\\Notepad++\\notepad++.exe",
                         "mobaxterm" : "C:\\Program Files (x86)\\Mobatek\\MobaXterm\\MobaXterm.exe",
                         #"putty" : "C:\\Program Files\\PuTTY\\putty.exe",
                         }

# Links to be opened in Chrome
links = {"github" : "https://github.com/namysl",
         "duckduckgo" : "https://duckduckgo.com",
         }

# Example files to be opened in Notepad++
file1 = "C:/Users/eknam/Desktop/1.txt"
file2 = "C:/Users/eknam/Desktop/2.txt"
file3 = "C:/Users/eknam/Desktop/3.txt"

def open_all():
    """Interval between the apps is set to 10 seconds"""
    for app, path in all_apps_to_be_opened.items():
        if not os.path.exists(path):
            print(path, "is in a different dir or does not exist")
            continue

        print("Opening:", app)
        if app == "notepad++":
            if os.path.exists(file1) and os.path.exists(file2) and os.path.exists(file3):
                subprocess.Popen([path, file1, file2, file3])
            else:
                subprocess.Popen(path)
                print("One or more of defined txt files are not found")
        else:
            subprocess.Popen(path)
        time.sleep(10)
        if app == "chrome":
            wb = chrome_single_slash + " %s"
            for name, link in links.items():
                print("Opening pages in the browser:", name)
                webbrowser.get(wb).open(link)
                time.sleep(5)


open_all()  
