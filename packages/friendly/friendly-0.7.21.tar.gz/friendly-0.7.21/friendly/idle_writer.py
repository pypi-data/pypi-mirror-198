"""Custom writer and formatter for IDLE.
"""

# IMPORTANT
# Do not put this module in the idle/ subdirectory as it will prevent
# it from being used by other packages such as friendly_idle.
# This module does not depend on any code found in idle/

import sys
from friendly_traceback.base_formatters import select_items, no_result, repl_indentation
from friendly_traceback.utils import get_highlighting_ranges

if sys.version_info >= (3, 9, 5):
    repl_indentation["suggest"] = "single"  # more appropriate value


def writer(output, color=None, stream=None):
    """Use this instead of standard sys.stderr to write traceback so that
    they can be colorized.
    """
    if isinstance(output, str):
        if color is None:
            stream.write(output, "stderr")  # noqa
        else:
            stream.write(output, color)  # noqa
        return
    for fragment in output:
        if isinstance(fragment, str):
            stream.write(fragment, "stderr")  # noqa
        elif len(fragment) == 2:
            stream.write(fragment[0], fragment[1])  # noqa
        else:
            stream.write(fragment[0], "stderr")  # noqa


# The logic of the formatter is quite convoluted,
# unless one is very familiar with how the basic formatting is done.
#
# All that matters is that, it is debugged and works appropriately! ;-)
# TODO: add unit tests


def format_source(text):
    """Formats the source code shown by where().

    Often, the location of an error is indicated by one or more ^ below
    the line with the error. IDLE uses highlighting with red background the
    normal single character location of an error.
    This function replaces the ^ used to highlight an error by the same
    highlighting scheme used by IDLE.
    """
    lines = text.split("\n")
    while not lines[-1].strip():
        lines.pop()
    error_lines = get_highlighting_ranges(lines)

    new_lines = []
    for index, line in enumerate(lines):
        if index in error_lines:
            continue
        colon_location = line.find("|") + 1

        if line.lstrip().startswith("-->"):
            new_lines.append((line[:colon_location], "stderr"))
        else:
            new_lines.append((line[:colon_location], "stdout"))
        if index + 1 in error_lines:
            no_highlight = True
            end = -1
            for begin, end in error_lines[index + 1]:
                text = line[begin:end]
                if no_highlight:
                    if begin < colon_location:
                        text = line[colon_location:end]
                    new_lines.append((text, "default"))
                    no_highlight = False
                else:
                    if not text:
                        text = " "
                    new_lines.append((text, "ERROR"))
                    no_highlight = True
            new_lines.append((line[end:], "default"))
        else:
            new_lines.append((line[colon_location:], "default"))
        new_lines.append(("\n", "default"))
    return new_lines


def format_text(info, item, indentation):
    """Format text with embedded code fragment surrounded by back-quote characters."""
    new_lines = []
    text = info[item].rstrip()
    for line in text.split("\n"):
        if not line.strip():
            continue
        if "`" in line and line.count("`") % 2 == 0:
            fragments = line.split("`")
            for index, fragment in enumerate(fragments):
                if index == 0:
                    new_lines.append((indentation + fragment, "stdout"))
                elif index % 2:
                    if (
                        "Error" in fragment
                        or "Warning" in fragment
                        or "Exception" in fragment
                    ) and " " not in fragment.strip():
                        new_lines.append((fragment, "stderr"))
                    else:
                        new_lines.append((fragment, "default"))
                else:
                    new_lines.append((fragment, "stdout"))
            new_lines.append(("\n", "stdout"))
        else:
            colour = "default" if line.startswith("    ") else "stdout"
            new_lines.append((indentation + line + "\n", colour))

    return new_lines


def format_traceback(text):
    """We format tracebacks using the default stderr color (usually red)
    except that lines with code are shown in the default color (usually black).
    """
    lines = text.split("\n")
    if lines[-2].startswith("SyntaxError:"):
        if lines[2].strip().startswith("File"):
            lines = lines[3:]  # Remove everything before syntax error
        else:
            lines = lines[1:]  # Remove file name
    new_lines = []
    for line in lines:
        if line.startswith("    "):
            new_lines.append((line, "default"))
        elif line:
            new_lines.append((line, "stderr"))
        new_lines.append(("\n", "default"))
    return new_lines


def formatter(info, include="friendly_tb"):
    """Formatter that takes care of color definitions."""
    items_to_show = select_items(include)
    spacing = {"single": " " * 4, "double": " " * 8, "none": ""}
    result = ["\n"]
    for item in items_to_show:
        if item == "header":
            continue

        if item in info:
            if "traceback" in item:  # no additional indentation
                result.extend(format_traceback(info[item]))
            elif "source" in item:  # no additional indentation
                result.extend(format_source(info[item]))
            elif "header" in item:
                indentation = spacing[repl_indentation[item]]
                result.append((indentation + info[item], "stderr"))
            elif "message" in item:  # Highlight error name
                parts = info[item].split(":")
                parts[0] = "`" + parts[0] + "`"
                _info = {item: ":".join(parts)}
                indentation = spacing[repl_indentation[item]]
                result.extend(format_text(_info, item, indentation))
            elif item == "exception_notes":
                result.extend([note + "\n" for note in info[item]])
            else:
                indentation = spacing[repl_indentation[item]]
                result.extend(format_text(info, item, indentation))
            if "traceback" not in item:
                result.extend("\n")

    if result == ["\n"]:
        return no_result(info, include)

    if result[-1] == "\n" and include != "friendly_tb":
        result.pop()

    return result
