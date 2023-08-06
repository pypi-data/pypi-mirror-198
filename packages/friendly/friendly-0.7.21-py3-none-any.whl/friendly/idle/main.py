"""Experimental module to automatically install Friendly
as a replacement for the standard traceback in IDLE."""

import inspect
import sys
from pathlib import Path
from functools import partial


from idlelib import run as idlelib_run

import friendly_traceback  # noqa
from friendly_traceback.config import session
from friendly_traceback.console_helpers import *  # noqa
from friendly_traceback.console_helpers import _nothing_to_show
from friendly_traceback.console_helpers import History, helpers, Friendly  # noqa
from friendly_traceback.functions_help import add_help_attribute

from friendly import get_lang
from friendly import settings
from ..my_gettext import current_lang
from .. import idle_writer
from . import patch_source_cache  # noqa
from .get_syntax import get_syntax_error


settings.ENVIRONMENT = "IDLE"
friendly_traceback.set_lang(get_lang())

friendly_traceback.exclude_file_from_traceback(__file__)
_writer = partial(idle_writer.writer, stream=sys.stdout.shell)


class IdleHistory(History):
    def __call__(self):
        """Prints a list of recorded tracebacks and warning messages"""
        if not session.recorded_tracebacks:
            info = {"suggest": _nothing_to_show() + "\n"}
            explanation = session.formatter(info, include="hint")
            session.write_err(explanation)
            return
        for index, tb in enumerate(session.recorded_tracebacks):
            if "message" in tb.info:
                info = {"message": f"`{index}.` {tb.info['message']}"}
                explanation = session.formatter(info, include="message")
                session.write_err(explanation)


history = IdleHistory()
add_help_attribute({"history": history})
Friendly.add_helper(history)
_old_displayhook = sys.displayhook

helpers["get_syntax_error"] = get_syntax_error

Friendly.remove_helper("disable")
Friendly.remove_helper("enable")
Friendly.remove_helper("set_formatter")


def _displayhook(value):
    if value is None:
        return
    if str(type(value)) == "<class 'function'>" and hasattr(value, "__rich_repr__"):
        _writer(
            [
                (f"    {value.__name__}():", "default"),
                (f" {value.__rich_repr__()[0]}", "stdout"),
                "\n",
            ]
        )
        return
    if hasattr(value, "__friendly_repr__"):
        lines = value.__friendly_repr__().split("\n")
        for line in lines:
            if "`" in line:
                newline = []
                parts = line.split("`")
                for index, content in enumerate(parts):
                    if index % 2 == 0:
                        newline.append((content, "stdout"))
                    else:
                        newline.append((content, "default"))
                newline.append("\n")
                _writer(newline)
            elif "():" in line:
                parts = line.split("():")
                _writer(((f"{    parts[0]}():", "default"), (parts[1], "stdout"), "\n"))
            else:
                _writer(line + "\n")
        return

    _old_displayhook(value)


def install_in_idle_shell(lang=get_lang()):
    """Installs Friendly in IDLE's shell so that it can retrieve
    code entered in IDLE's repl.
    Note that this requires Python version 3.10+ since IDLE did not support
    custom excepthook in previous versions of Python.

    Furthermore, Friendly is bypassed when code entered in IDLE's repl
    raises SyntaxErrors.
    """
    friendly_traceback.exclude_file_from_traceback(idlelib_run.__file__)
    friendly_traceback.install(include="friendly_tb", redirect=_writer, lang=lang)


def install(lang=get_lang()):
    """Installs Friendly in the IDLE shell, with a custom formatter.
    For Python versions before 3.10, this was not directly supported, so a
    Friendly console is used instead of IDLE's shell.

    Changes introduced in Python 3.10 were back-ported to Python 3.9.5 and
    to Python 3.8.10.
    """
    _ = current_lang.translate

    sys.stderr = sys.stdout.shell  # noqa
    friendly_traceback.set_formatter(idle_writer.formatter)
    if sys.version_info >= (3, 9, 5) or (
        sys.version_info >= (3, 8, 10) and sys.version_info < (3, 9, 0)
    ):
        install_in_idle_shell(lang=lang)
        sys.displayhook = _displayhook
    else:
        _writer(_("Friendly cannot be installed in this version of IDLE.\n"))
        _writer(_("Using Friendly's own console instead.\n"))
        start_console(lang=lang, displayhook=_displayhook)


def start_console(lang="en", displayhook=None, ipython_prompt=True):
    """Starts a Friendly console with a custom formatter for IDLE"""
    sys.stderr = sys.stdout.shell  # noqa
    friendly_traceback.set_stream(_writer)
    friendly_traceback.start_console(
        formatter=idle_writer.formatter,
        lang=lang,
        displayhook=displayhook,
        ipython_prompt=ipython_prompt,
    )


def run(
    filename,
    lang=get_lang(),
    include="friendly_tb",
    args=None,
    console=True,
    ipython_prompt=True,
):
    """This function executes the code found in a Python file.

    ``filename`` should be either an absolute path or, it should be the name of a
    file (filename.py) found in the same directory as the file from which ``run()``
    is called.

    If friendly_console is set to ``False`` (the default) and the Python version
    is greater or equal to 3.10, ``run()`` returns an empty dict
    if a ``SyntaxError`` was raised, otherwise returns the dict in
    which the module (``filename``) was executed.

    If console is set to ``True`` (the default), the execution continues
    as an interactive session in a Friendly console, with the module
    dict being used as the locals dict.

    Other arguments include:

    ``lang``: language used; currently only ``en`` (default) and ``fr``
    are available.

    ``include``: specifies what information is to be included if an
    exception is raised.

    ``args``: strings tuple that is passed to the program as though it
    was run on the command line as follows::

        python filename.py arg1 arg2 ...


    """
    _ = current_lang.translate

    sys.stderr = sys.stdout.shell  # noqa
    friendly_traceback.set_formatter(idle_writer.formatter)
    friendly_traceback.set_stream(_writer)

    filename = Path(filename)
    if not filename.is_absolute():
        frame = inspect.stack()[1]
        # This is the file from which run() is called
        run_filename = Path(frame[0].f_code.co_filename)
        run_dir = run_filename.parent.absolute()
        filename = run_dir.joinpath(filename)

    if not filename.exists():
        print(_("The file {filename} does not exist.").format(filename=filename))
        return

    if not console:
        if sys.version_info >= (3, 9, 5) or (
            sys.version_info >= (3, 8, 10) and sys.version_info < (3, 9, 0)
        ):
            install_in_idle_shell()
        else:
            sys.stderr.write("Friendly cannot be installed in this version of IDLE.\n")

    return friendly_traceback.run(
        filename,
        lang=lang,
        include=include,
        args=args,
        console=console,
        formatter=idle_writer.formatter,
        ipython_prompt=ipython_prompt,
    )
