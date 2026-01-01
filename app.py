import os

def run_cmd(cmd):
    os.system(cmd)   # security issue (command injection)

run_cmd("ls")
