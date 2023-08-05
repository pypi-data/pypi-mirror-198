devi_bin = f"\u001b[32m{'devi'}\u001b[0m"

__doc__ = f"""{devi_bin}: a tool for managing your project templates

usage:
    {devi_bin} add <path> [<template-name>]
    {devi_bin} create <template-name> [<destination>] [--name=<project-name>]
    {devi_bin} create <template-name> as <project-name> in <destination>
    {devi_bin} list
    {devi_bin} rm     <template-name> [-y]
    {devi_bin} (-h | --help) | --version

options:
    -d, --dest=<destination>    Destination directory for the new project
    -n, --name=<project-name>   Name of the new project
    -h, --help   Shows this screen.
    --version    Shows {devi_bin} version.
"""

from docopt import docopt
from devi import __version__

args = docopt(__doc__, help=True, version=__version__)
