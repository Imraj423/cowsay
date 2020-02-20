from subprocess import Popen


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
