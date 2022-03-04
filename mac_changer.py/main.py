import subprocess
import optparse
import re


def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="used to select the interface")
    parser.add_option("-m", "--mac", dest="mac", help="used to select the Mac_address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("interface was not specified! use --help to get the info to use ")
    elif not options.mac:
        print("mac was not specified use --help to get the info to use")
    else:
        return options

def mac_changer(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])




options = get_options()

mac_changer(options.interface, options.mac)



