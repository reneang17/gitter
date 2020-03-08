#!/usr/bin/env python
import os, sys
import itertools


############################################
## ------- Funct write/run bash scripts -----
############################################
def write_script(dir, script_name, script_content):
    path_to_script = os.path.join(dir, script_name)
    with open(path_to_script, 'w') as fout:
        fout.write(script_content)



def execute_bash_script(dir, script_name):
    if dir != './': os.system('cd {}'.format(dir))
    os.system('chmod +x {}'.format(script_name))
    os.system('./{}'.format(script_name))
    if dir != './': os.system('cd ..')
