import os
from _utils import write_script, execute_bash_script
import argparse


############################################
## ------- Input variable to change (Only change this section)
############################################

# 1.- Customize these variables
git_username = 'reneang17'
travis_username = 'reneang17'
author = 'Rene Angeles'
author_email = 'reneang17@gmail.com'


# 2. - Variables to set when running this script
parser = argparse.ArgumentParser()
parser.add_argument('--repo', type=str,help="your github repo name")
parser.add_argument('--pack', type=str,help="your package repo name")
parser.add_argument('--travis', type=bool, default = True,
 help="add travis yml (default: True)")
parser.add_argument('--template', type=bool, default = True,
  help="add notebooks and data folder (default: True)")
args = parser.parse_args()

repo = args.repo
pack = args.pack
travis = args.travis # whether or not to add travis yml
template = args.template # add notebooks and data folder

############################################
## ------- Instructions and variables to parse
############################################

############################################
## ------- Create readme
############################################

readme_content = \
"""# {}
""".format(pack)
if travis:
    readme_content+=\
    "[![Build Status](https://travis-ci.com/{0}/{1}.svg?branch=main)](https://travis-ci.com/{0}/{1})\n".format(travis_username,repo)

write_script(dir = './', script_name = 'README.md',
    script_content = readme_content)

################################## = ##########
## ------- Create package
############################################

if not os.path.exists(pack):
    os.makedirs(pack)

init_content = "from .{} import *".format(pack)
write_script(dir = pack, script_name = '__init__.py',
    script_content = init_content)

inital_object = pack+'_object'
package_content = \
"""class {}(object):
    def __init__(self):
        print('et print, ergo sum')

    def fizz(self):
        return 'buzz'
""".format(inital_object)
write_script(dir = pack, script_name = pack + '.py',
    script_content = package_content)



############################################
## ------- create/install setup file
############################################

url = ''.join(['git@github.com:',git_username, '/', repo])
packages = [pack]
setup_dir = pack
setup_content = \
"""from distutils.core import setup

setup(name = '{}',
author = '{}',
author_email = '{}',
url = '{}',
packages = {}
)
""".format(repo, author, author_email, url, packages)
write_script('./', 'setup.py', setup_content)


############################################
## ------- Add test
############################################

if not os.path.exists('test'):
    os.makedirs('test')
test_file_name = 'test_' + pack + '.py'
test_content = \
"""import numpy as np
import numpy.testing as npt

import {0}

def test_{0}_smoke():
    #Smoke_test
    obt = {0}.{1}()

def test_{1}_fizz():
    #test the fizz_function
    obj = {0}.{1}()
    output = obj.fizz()

    npt.assert_equal(output, "buzz")
""".format(pack, inital_object)

write_script('./test', test_file_name, test_content)


################################## = ##########
## ------- Add python based template folders
############################################

template_dirs = ['data', 'notebooks']
if template:
    for dir in template_dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)


############################################
## ------- Install Package, test, Push to github
############################################

github_bash_content = \
"""#!/bin/bash
rm -rf .git
cd ..
mv gitter {0}
cd {0}
pip install -r requirements.txt
#python setup.py install && pytest
pip install -e .
pytest
git init
git add .
git add -f ./{1}/__init__.py
""".format(repo, pack)

if travis:
    github_bash_content+='git add -f .travis.yml\n'
if template:
    for dir in template_dirs:
        github_bash_content+="cp .gitignore {}\n".format(dir)
        github_bash_content+="git add {}\n".format(dir)

github_bash_content+="""
git commit -m "first commit"
git branch -M main
git remote add origin {}.git
git push -u origin main
""".format(url)

write_script('.', '_first_commit.sh', github_bash_content)
execute_bash_script('./', '_first_commit.sh')
