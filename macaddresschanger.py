#!/usr/bin/env python

import subprocess
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[.] Please specify an interface, check --help for more info")
    elif not options.new_mac:
        parser.error("[.] Please specify a MAC Address, check --help for more info")
    return options
    
def change_mac(interface, new_mac):
    print("[+] Changing the MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
