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
    'version': '0.1.0',
    'description': 'Run shell in python',
    'long_description': '## Pysh\n\nPython source file preprocessor/interpreter to enable running in-line bash code during python runtime\n\nAlso can capture stdout into a python variable and use shells beyond bash.\n\nThis is done by processing the source with regex and a basic subprocess wrapper using shell command strings.\n\n### Installation\n\nInstall to local folder:\n`pip3 install -e "git+https://github.com/blipk/pysh.git#egg=pysh"`\n\n### Examples\n[demo file](demo.py)\n\n###### Run pysh whenever this source file is interpreted\n```Python\n#!/usr/bin/env python\nfrom pysh import pysh\npysh()\n\n#$ echo "Pysh activated"\nstdout = ""#$ echo "This is standard out"\n```\n\n##### Real usage\n```Python\n# Script your system in paralel with your python code execution\n# Do anything you can in bash e.g.\n#$ firefox https://news.ycombinator.com && echo "opened link in firefox"\n\nbuild_service()\n#$ cd ~/hosted/myservice && docker compose up\n\naggregate_assets()\ncrf = "23"\nout_file = "out.mp4"\nfmpg_result = ""#$ ffmpeg -i raw_video.mkv -crf {$crf$} -o {$out_file$}\nprocess_assets(process_fmpg_stdout(fmpg_result))\n```\n\n###### General syntax\n```Python\n#!/usr/bin/python\n# This is a python comment\n#$  ls .         # pysh eol comment\n##$ sudo rm -rf  # disable pysh line with pysh comment\n\n# Pass any python variable thats in scope to the pysh script\nmy_var = "hello"\nstdout = ""#$ echo "{$myvar$}"\n\n# run external script with double $\n#$$ my_script.sh\n\n# optionally pass arguments to it\n#$$ argumentative_script.sh arg1 arg2\n\n# Use the ! flag to hange the shell that interprets the script\n# must support -c command_strings or filepath if external $$\n#$!sh echo "simple"\n#$!perl oysters.pl\n#$$!bash script.sh\nstdout = ""#$!python import time; print("The time and date", time.asctime())\n\n# Use the % flag to catch errors\ntry:\n    result = ""#$$% tests/dinger/notfoundscript.sh "argone"\nexcept SystemExit as e:\n    print("Error", e)\n\n# Use the @ flag to always print(stdout)\n#$@ echo "hello"     # Will print it\'s stdout to sys.stdout without capturing in a var\n\nif __name__ == "main":\n    print("Before the above script blocks are run")\n```\n\n\n###### Multiple inline pysh\n```Python\n# Pysh runs code in blocks that are executed in-place\n\n# Block 0\n#$ cd $HOME\n\nstdout_block1 = ""#$ echo "first block is multiline"\n#$ echo "line1"\n#$ echo "line2"\n\n# The last script block won\'t be run\nsys.exit(1)\nstdout_block2 == ""#$ echo "Second"\n#$ echo "Block"\n```\n\n\n##### Advanced usage\n```Python\n# run pysh manually\nfrom pysh import Pysh\nsource_file = __file__\npysher = Pysh(source_file)\nblocks = pysher.findblocks()\n\n# Run a a single block\nblocks[0].run()  # Not run in-place, no stdout. Silent.\nblocks[0].runp() # Run script block again, and print stdout with label for block\n\n# Run all wanted blocks sequentially at this point,\n# and print their stdout with labels\nrun_blocks = [block.runp() for block in blocks\n              if "/root" in block.srcs]\n\n# Start the python interpreter with pysh on source_file\n# This is the same as running pysh(__file__)\npysher.shyp()\n#$ echo "pysh enabled"\n\n# Switch to another source file and run it through pysh\npysher.pysh(__file__)\n\n# Equivalent to above\npysher.updatesrc(__file__)\npysher.pysh()\n\n# Get information about the script blocks at runtime\nt_block = pysher.blocks[0]\nprint(t_block.hasrun, t_block.returncode)\nprint(t_block.srcs, "\\n--\\n", t_block.stdout)\n```',
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
