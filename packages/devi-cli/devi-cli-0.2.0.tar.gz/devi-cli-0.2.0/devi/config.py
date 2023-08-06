import os
import platform
from pathlib import Path
from devi.cli.log import deviprint, DEVI_COLORS
from devi.toml_parser import tomllib
from typing import Callable

is_windows = platform.system() == 'Windows'

DEVI_TEMPLATES: Path
DEVI_CONFIG: Path
DEVI_TEMPLATE_TOML_CONTENT: Callable[[str], str]
DEVI_DEFAULT_EDITOR: str
DEVI_COLORS: dict[str, Callable[[str], str]]

def init():
    """
    Initialize the config variables for devi.
    """
    global DEVI_TEMPLATES
    global DEVI_CONFIG

    global DEVI_TEMPLATE_TOML_FILENAME
    global DEVI_TEMPLATE_TOML_CONTENT
    global DEVI_DEFAULT_EDITOR

    global DEVI_COLORS # defined in log.py

    # Default home is ~/.devi
    is_custom_user_dir = False
    if (devi_templates_dir := os.getenv('DEVI_TEMPLATES')):
        DEVI_TEMPLATES = Path(devi_templates_dir)
        is_custom_user_dir = True
    else:
        DEVI_TEMPLATES = Path.home() / '.templates'

    try:
        # exists ok
        if not DEVI_TEMPLATES.exists():
            DEVI_TEMPLATES.mkdir()
            deviprint.success(
                f'we just setup \'{DEVI_TEMPLATES.resolve().as_posix()}\' just for you!'
            )
            if not is_custom_user_dir:
                deviprint.info(f"if you want to override it, define {DEVI_COLORS['info']('$DEVI_TEMPLATES')}\n")
    except Exception as e:
        deviprint.err(f'couldn\'t create $DEVI_TEMPLATES at \'{DEVI_TEMPLATES}\'. exiting')
        deviprint.err(f'error received: {e}')
        exit(1)

    # Config file for devi is ~/.devi.toml
    # (TODO: put this in a better cross-platform place)
    DEVI_CONFIG = Path.home() / '.devi.toml'

    try:
        with open(DEVI_CONFIG, 'rb') as f:
            conf = tomllib.load(f)
            # loading config options
            DEVI_DEFAULT_EDITOR = conf.get('editor', get_default_text_editor())
    except IOError:
        # deviprint.warn('couldn\'t found devi config')
        DEVI_DEFAULT_EDITOR = get_default_text_editor()
        pass

    DEVI_TEMPLATE_TOML_FILENAME = 'template.devi.toml'
    # TODO: make this a customizable file
    DEVI_TEMPLATE_TOML_CONTENT = lambda template_name: (
f"""# configuration for template '{template_name}'

# this description will be shown on 'devi list'
description = ''

# this name will be used as default name for 'devi create "{template_name}"'
default_name = '{template_name}'

# destination to be used when for 'devi create "{template_name}"'
# (can be relative or absolute)
destination = '.'

# command to execute after template creation
oncreate = ''

# wheter you want to 'cd' to the newly created template or not
change_dir = true
""")

def get_default_text_editor() -> str:
    """Try to get the default text editor from the environment variables.

    It falls back for notepad on Windows and
    [sensible-editor, editor, nano, vim, vi] on *nix.
    """
    # prefer VIEWER as sensible-editor does
    for editor in [os.getenv('VIEWER'), os.getenv('EDITOR')]:
        if editor: return editor

    find_cmd = 'where' if is_windows else 'which'
    null = 'NUL' if is_windows else '/dev/null'

    for editor in ['sensible-editor', 'editor', 'nano', 'vim']:
        if os.system(f'{find_cmd} {editor} >{null} 2>&1') == 0:
            return editor

    return 'notepad' if is_windows else 'vi'
