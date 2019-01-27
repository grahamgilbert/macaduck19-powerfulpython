#!/usr/bin/python

import subprocess

SUPER_SECRET_PASSWORD = "4DBAA9CF-1E0A-4AFD-9444-7062CA4A2C7D"


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
