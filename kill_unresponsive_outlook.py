import os

process = "outlook.exe"
kill_process = r'taskkill /fi "IMAGENAME eq {}" /fi "STATUS eq {}" '.format(process, "running")

os.system(kill_process) 