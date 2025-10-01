# Import the sys module to access system-specific information.
import sys

# Import the textwrap module to format the list of module names.
import textwrap

# Get a sorted list of built-in module names in the system.
module_name = ', '.join(sorted(sys.builtin_module_names))

# Use textwrap to format the list of module names into lines with a maximum width of 70 characters.
# Then, print the formatted text.
print(textwrap.fill(module_name, width=70))
