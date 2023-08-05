from pathlib import Path

from devi.commands.add_template import add_template
from devi.commands.list import list_templates
from devi.commands.create import create_project
from devi.commands.remove import remove_template

def main():
    """devi: a tool for managing your project templates"""
    from devi.cli.args_parser import args

    if args['add']:
        src_path: Path = Path(args['<path>'])
        template_name: str = args['<template-name>']
        add_template(src_path, template_name)

    elif args['list']:
        list_templates()

    elif args['create']:
        template_name = args['<template-name>']
        project_name = args['--name'] or args['<project-name>']
        destination = args['<destination>']
        create_project(
            template_name,
            destination,
            project_name
        )

    elif args['rm']:
        template_name = args['<template-name>']
        confirm = bool(args['-y'])
        remove_template(template_name, confirm)
