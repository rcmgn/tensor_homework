#!/usr/bin/python

import re

from ansible.errors import (
    AnsibleFilterTypeError,
    AnsibleFilterError
)

def convert_mac(mac):
    '''
        Covert MAC address from str to MAC view
    '''
    if not isinstance(mac, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(mac))
    if len(mac) != 12:
        raise AnsibleFilterError("Wrong size of MAC address 12 expected, "
                                     "%d instead" % len(mac))
    for s in mac:
        if s not in "0123456789ABCDEF":
            raise AnsibleFilterError("MAC address must contain only 0-9 and A-F")

    return re.sub(r'(.{2})(?!$)', r'\1:', mac)

    #  Other versions
    # return ":".join(re.findall(r'..', mac))
    # return ":".join([mac[i:i+2] for i in range(0, len(mac), 2)])


class FilterModule(object):
    def filters(self):
        return {
            'convert_mac': convert_mac
        }
