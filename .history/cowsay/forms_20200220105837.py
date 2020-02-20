import subprocess
import sys
from sys import stdout, stdin, stderr


def cowsay_helper(text):
    cmd = subprocess.Popen(
        ['cowsay', text],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    out, err = cmd.communicate()
    if err:
        raise err
    else:
        return out.decode().split("\n")
