#!/usr/bin/env python

example1 = ['switchport mode access',
            'switchport access vlan {}',
            'switchport nonegotiate',
            'spanning-tree portfast',
            'spanning-tree bpduguard enable']
print('\n'.join(example1).format(5))
