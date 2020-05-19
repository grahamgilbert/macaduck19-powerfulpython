#!/usr/bin/python

import subprocess


def requires_reboot(cmd_output):
    """
    Input: output from softwareupdate. Tests if "restart" is in the output.
    Output: Boolean.
    """
    if "restart" in cmd_output.lower():
        return True
    else:
        return False


def main():
    cmd = ["/usr/sbin/softwareupdate", "-dla"]
    output = subprocess.check_output(cmd)
    if requires_reboot(output) == True:
        subprocess.call(["/sbin/reboot"])


if __name__ == "__main__":
    main()
