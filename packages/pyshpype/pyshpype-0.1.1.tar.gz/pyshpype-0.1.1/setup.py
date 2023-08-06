# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pysh']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyshpype',
    'version': '0.1.1',
    'description': 'Run shell in python',
    'long_description': '## Pysh/Pype\n\nPython source file preprocessor/interpreter and subprocess pipe manager to enable running in-line bash/shell code during python runtime.\n\n```Python\n#!/usr/bin/env python\nfrom pysh import pysh\npysh()\n\n#$@ echo "Pysh activated"\nstdout = ""#$ echo "This is standard out"\nprint(stdout)\n\n##@!python print("Python through a pysh pype")\n```\n\nUse #$ flagged directives to signify shell code to be piped through a subprocess.\n\n##### Real usage\n```Python\n# Script your system in parallel with your python code execution\n# Do anything you can in bash e.g.\n\nbuild_service()\n#$ cd ~/hosted/myservice && docker compose up\n\naggregate_assets()\ncrf = "23"\nin_file = "/path/in.mp4"\nout_file = "/path/out.mp4"\nfmpg_result = ""#$ ffmpeg -i {$in_file$} \\\n#$ -crf {$crf$} -o {$out_file$} \\\n#$ && rm {$in_file$}\nprocess_assets(process_fmpg_stdout(fmpg_result))\n\nprint("Process complete")\n```\n\n### Installation\nFrom PyPI:\n\n`pip3 install pyshpype`\n\nGit to local folder:\n\n`pip3 install -e "git+https://github.com/blipk/pysh.git#egg=pysh"`\n\n\n\n###### General syntax\n```Python\n#!/usr/bin/python\n# This is a python comment\n#$  ls .         # pysh eol comment\n##$ sudo rm -rf  # disable pysh line with pysh comment\n\n# Pass any python variable thats in scope to the pysh script\nmy_var = "hello"\nstdout = ""#$ echo "{$myvar$}"\n\n# run external script with double $\n#$$ my_script.sh\n\n# optionally pass arguments to it\n#$$ argumentative_script.sh arg1 arg2\n\n# Use the ! flag to change the shell that interprets the script\n# must support -c command_strings or filepath if external $$\n#$!sh echo "simple"\n#$!perl oysters.pl\n#$$@!bash printscript.sh\n\n# Multiple flags/features\nstdout = ""#$@!python import time\n#$ print("The time and date", time.asctime())\n\n# Use the % flag to catch errors,\n# otherwise they will be printed but not raised\ntry:\n    result = ""#$$% tests/dinger/notfoundscript.sh "argone"\nexcept SystemExit as e:\n    print("Error", e)\n\n# Use the @ flag to always print(stdout)\n#$@ echo "hello"     # Will print it\'s stdout to sys.stdout without capturing in a var\n\nif __name__ == "main":\n    print("Before the above script blocks are run")\n```\n\n\n###### Multiple inline pysh\n```Python\n# Pysh runs code in blocks that are executed in-place\n\n# Block 0\n#$ cd $HOME\n\nstdout_block1 = ""#$ echo "first block is multiline"\n#$ echo "line1"\n#$ echo "line2"\n\n# The last script block won\'t be run\nsys.exit(1)\nstdout_block2 == ""#$ echo "Second"\n#$ echo "Block"\n```\n\n\n##### Advanced usage\n```Python\n# run pysh manually\nfrom pysh import Pysh\nsource_file = __file__\npysher = Pysh(source_file)\nblocks = pysher.findblocks()\n\n# Run a a single block\nblocks[0].run()  # Not run in-place, no stdout. Silent.\n\n# Run script block again, and print stdout with label for block\nblocks[0].runp()\n\n# Run all wanted blocks sequentially at this point,\n# and print their stdout with labels\nrun_blocks = [block.runp() for block in blocks\n              if "/root" in block.srcs]\n\n# Start the python interpreter with pysh on source_file\n# This is the same as running pysh(__file__)\npysher.shyp()\n#$ echo "pysh enabled"\n\n# Switch to another source file and run it through pysh\npysher.pysh(__file__)\n\n# Equivalent to above\npysher.updatesrc(__file__)\npysher.pysh()\n\n# Get information about the script blocks at runtime\nt_block = pysher.blocks[0]\nprint(t_block.hasrun, t_block.returncode)\nprint(t_block.srcs, "\\n--\\n", t_block.stdout)\n```',
    'author': 'Blipk A.D.',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/blipk/pysh',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
