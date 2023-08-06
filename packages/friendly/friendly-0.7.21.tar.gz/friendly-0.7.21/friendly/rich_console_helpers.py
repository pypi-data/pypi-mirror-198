"""In this module, we modify the basic console helpers for friendly-traceback
to add custom ones for Rich-based formatters."""

from friendly_traceback.console_helpers import *  # noqa; include Friendly below
from friendly_traceback.console_helpers import Friendly, helpers
from friendly_traceback.functions_help import add_help_attribute, short_description
from friendly_traceback.config import session

from friendly.my_gettext import current_lang
from friendly import _print_settings
from friendly.settings import _remove_environment
from friendly.theme import colours

# The following is different from the one imported via the import * above
from friendly import set_formatter

helpers["set_formatter"] = set_formatter
add_help_attribute({"set_formatter": set_formatter})
Friendly.add_helper(set_formatter)

_ = current_lang.translate
# =================================
# Additional rich-specific helpers
# =================================


def dark():
    """Synonym of set_formatter('dark') designed to be used
    within iPython/Jupyter programming environments.
    """
    set_formatter("dark")


def disable():
    """Disable friendly's exception hook, restoring the previous one"""
    if not session.installed:
        print(_("Friendly is already disabled."))
        return
    try:
        get_ipython()  # noqa
    except NameError:
        session.uninstall()
        return
    from .ipython_common import excepthook

    excepthook.disable()


def enable():
    """Enable friendly's exception hook."""
    if session.installed:
        print(_("Friendly is already enabled."))
    try:
        get_ipython()  # noqa
    except NameError:
        session.install()
        return
    from .ipython_common import excepthook

    excepthook.enable()


def light():
    """Synonym of set_formatter('light') designed to be used
    within iPython/Jupyter programming environments.
    """
    set_formatter("light")


def plain():
    """Synonym of set_formatter('plain').
    Monochrome output without using Rich.
    """
    set_formatter("plain")


def set_background(color=None):
    """Sets the background color for the current environment."""
    if color is None:
        colours.set_background_color(None)
        return
    set_formatter(background=color)


def set_highlight(bg="#cc0000", fg="white"):
    """Sets the highlight colour. Use None to turn off highlight."""
    # Need to validate colour if not None, and revert to default
    colours.set_highlight(bg=bg, fg=fg)


def set_width(width=80):
    """Sets the width in a iPython/Jupyter session using a Rich formatter."""
    try:
        session.console.width = width
    except Exception:  # noqa
        return
    session.rich_width = width
    if session.is_jupyter and (
        session.rich_tb_width is not None and session.rich_width > session.rich_tb_width
    ):
        session.rich_tb_width = width


short_description["dark"] = lambda: _(
    "Sets a colour scheme designed for a black background."
)
short_description["disable"] = lambda: _("Disable friendly's exception hook.")
short_description["enable"] = lambda: _("Enable friendly's exception hook.")
short_description["light"] = lambda: _(
    "Sets a colour scheme designed for a white background."
)
short_description["plain"] = lambda: _("Plain formatting, with no colours added.")
short_description["set_background"] = lambda: _("Sets the background color.")
short_description["set_highlight"] = lambda: _("Sets the highlight colors; bg and fg.")
short_description["set_width"] = lambda: _("Sets the output width in some modes.")
short_description["_print_settings"] = lambda: _("Prints the saved settings.")
short_description["_remove_environment"] = lambda: (
    "Deletes an environment from the saved settings; default: current environment."
)
local_helpers = {
    "dark": dark,
    "disable": disable,
    "enable": enable,
    "light": light,
    "plain": plain,
    "set_width": set_width,
    "set_background": set_background,
    "set_highlight": set_highlight,
    "_print_settings": _print_settings,
    "_remove_environment": _remove_environment,
}
add_help_attribute(local_helpers)
for helper in local_helpers:
    Friendly.add_helper(local_helpers[helper])

helpers.update(local_helpers)
__all__ = list(helpers.keys())
