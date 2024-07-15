def generate_init_file(package_name, modules, ppath = ""):
    content = f"""# Auto-generated __init__.py for {package_name} package

# Import necessary modules
{chr(10).join(f"from .{module} import {module}" for module in modules)}

# Public API of the package
__all__ = {str(modules)}

# Version checking
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("{package_name}")
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

# You can add any initialization code here if needed
"""

    if not ppath:
        ppath = "src/" + package_name + "/"

    with open(ppath, 'w') as f:
        f.write(content)


# Usage
import os
from pathlib import Path
package_name = "pyfunc_config"
directory = "src/" + package_name + "/"
py_files = [f for f in os.listdir(directory) if f.endswith('.py') and f != '__init__.py']
modules = [os.path.splitext(f)[0] for f in py_files]
generate_init_file(package_name, modules)