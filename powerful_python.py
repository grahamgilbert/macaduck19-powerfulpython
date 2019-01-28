#!/usr/bin/python

import subprocess


def requires_reboot(cmd_output):
    if "restart" in cmd_output.lower():
        return "True"
    else:
        return False


def main():
    cmd = [
        "/usr/sbin/softwareupdate",
        "-dla"
    ]
    output = subprocess.check_output(cmd)
    if requires_reboot == True:
        subprocess.call(["/sbin/reboot"])


if __name__ == "__main__":
    main()
