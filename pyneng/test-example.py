#!/usr/bin/env python3
import sys

interface, vlan = sys.argv[1:]

commands1 = ['switchport mode access',
            'switchport access vlan {}',
            'switchport nonegotiate',
            'spanning-tree portfast',
            'spanning-tree bpduguard enable']
print('interface {}'.format(interface))
print('\n'.join(commands1).format(vlan))
