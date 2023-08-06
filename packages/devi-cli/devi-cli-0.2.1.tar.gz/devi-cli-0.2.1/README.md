<p align="center">
    <h1 align="center">devi</h1>
</p>
<p align="center">
  <code>devi is a cli tool for managing your project templates</code>
</p>

<p align="center">
<img src="https://img.shields.io/badge/pipx%20install-devi--cli-blue"/>
<img src="https://shields.io/pypi/v/devi-cli"/>
<img src="https://shields.io/pypi/l/devi-cli"/>
</p>

With `devi` you can create, use, reuse and manage your project templates.

## Usage

<div align="justify">
<div align="center">

```bash
devi <command> [options]
```

</div>
</div>

Available commands:

- `add` - Add a new template to your list
- `create` - Create a new project from a template
- `list` - List available templates
- `rm` - remove a template

`$DEVI_TEMPLATES` is the special directory where `devi` stores your templates.
By default is set to `~/.templates`, but it is customizable to easy migrate
your existing templates!

---

## Commands

<!-- here might be a showcase video -->

### Add a new template

The `add` command adds a new template to `$DEVI_TEMPLATES`.

```bash
devi add <path> [<template_name>]
```

```bash
devi add . my_new_template

# if template_name is not provided, devi will use the directory name
devi add ~/dev/my_template
```

### Create a new project from a template

The `create` command creates a new project from an existing template.

<!-- Aliases: `new`, `n`-->

```bash
devi create <template_name> [<destination>] [--name=<project-name>]

# or with syntactic sugar:
devi create <template_name> as <project_name> in <destination>
```
```bash
# this will create a new dir called "my_template"
devi create my_template .
# don't worry, you can give it a name
devi create my_template . --name=my_project
# equivalent to the following:
devi create my_template as my_project in .
```

Do you want more customization? we catch you!

Both parameters (`project-name` and `destination`) are optional. If not set,
`devi` will use the values defined in the `template.devi.toml` (see
[template config](#template-configuration-file)).

## Viewing and removing your templates

To see the list of available templates, run `devi list`. They are located on
`$DEVI_TEMPLATES`.

Don't want a template anymore? Remove it with

```bash
devi rm <template-name> [-y]
```

It will ask you to confirm the deletion, you can skip this with the `-y` flag.

## Devi's templates

`$DEVI_TEMPLATES` is special, the place where `devi` finds and stores all your
templates. By default is set to `~/.templates` or
`%USERPROFILE%\templates` on Windows.

If you already have a templates folder or you want to make your templates more
accesible, you can override it, e.g, for bash:

```bash
echo "export DEVI_TEMPLATES=~/my/templates" >> ~/.bashrc
```

`TODO:` configuration file for devi is not ready yet

### Template configuration file

The `template.devi.toml` file is used to customize the template. It is
**autocreated** by `devi`. Here is an example of a template for web projects:

```toml
description = 'my template for web projects'
default_name = 'new-project'
destination = '~/projects/web'
oncreate = 'npm init -y && npm install vite && npm run dev'
change_dir = true
```

- `description` - it will be shown on `devi list` (default: `None`).
- `default_name` - devi will use this name as default for `devi create`
  (default: the template's name).
- `destination` - the destination directory where the project will be created in
  (default: `"."`).
- `oncreate` - a shell command that will be executed after the project has been
  created. Commands will be relative to the newly created template
  (default: `None`).
- `change_dir` - wheter you want to change your directory to the newly created
  template or not (default: `true`)

After `oncreate` finishes its execution, all the files and directories with the
`*.devi.*` extension will be removed from the project. e.g.:
`whatever.devi.sh`, `my_dir.devi/`, and the `template.devi.toml` itself.

> **Note**
> Currently `change_dir` is not implemented for Windows (see [TODO.md](./TODO.md))

## Installation

`devi` is distributed as a [pypi package](https://pypi.org/project/devi-cli/)
which exposes the `devi` binary.

```bash
pip install devi-cli
```

However, since `devi` is just a cli tool, is preferable to install it using
`pipx`, which will create a separate python environment that won't interfere
with your system's one.

```bash
pipx install devi-cli
```

If you don't have `pipx` already, go [here](https://pypa.github.io/pipx/), it's
very handy! This will also avoid possible [environment errors](https://github.com/python/cpython/issues/102134) on most linux distributions.

## Development

Requires python `>= 3.7`.

```bash
# In the root project, install an editable version of devi
pip install -e .
# Or just invoque the __main__
alias devi="python3 devi"
```
