import pyperclip
import re

from_clipboard = pyperclip.paste()

no_line_breaks = re.sub(r"(\r\n|\n|\r)", ' ', from_clipboard, flags=re.MULTILINE)
final_version = re.sub(r"\s+", ' ', no_line_breaks)

pyperclip.copy(final_version)
