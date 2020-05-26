#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
# 'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
# The \1 in that string will be replaced by whatever text was matched by group 1 —
# that is, the (\w) group of the regular expression.
# A**** told C**** that E**** knew B**** was a double agent.'"""
