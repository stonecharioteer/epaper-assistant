#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess

def get_ips():
    """Returns a list of IP addresses assigned to this device."""
    import subprocess
    import re
    ip_information = subprocess.check_output(["ifconfig"]).decode("utf-8").strip().split("\n\n")
    ips = []
    pattern = re.compile(r"[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}")
    
    for ip_entry in ip_information:
        interface = ip_entry.split()[0]
        if "eth" in interface or "wlan" in interface:
            possible_ips = pattern.findall(ip_entry)
            ip = None
            if len(possible_ips)>0:
                ip = possible_ips[0]
            ip_entry_dict = {
                    "interface": interface,
                    "ip": ip
                    }
            ips.append(ip_entry_dict)
    return ips



