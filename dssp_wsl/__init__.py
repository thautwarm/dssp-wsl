import sys
import subprocess


def dssp():
    subprocess.check_call(["wsl", "dssp", *sys.argv[1:]])

def mkdssp():
    subprocess.check_call(["wsl", "mkdssp", *sys.argv[1:]])
