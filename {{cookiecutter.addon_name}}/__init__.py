bl_info = {
    "name": "{{cookiecutter.addon_name}}",
    "author": "{{cookiecutter.author}}",
    "version": ({{cookiecutter.version.split(".") | join(", ")}}),
    "blender": ({{cookiecutter.blender_version.split(".") | join(", ")}}),
    "location": "",
    "description": "{{cookiecutter.description}}",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/{{cookiecutter.github}}/{{cookiecutter.addon_name}}/issues",
    "support": "COMMUNITY",
    "category": "{{cookiecutter.category}}",
}

__version__ = ".".join(map(str, bl_info["version"]))

import bpy
import numpy as np
import mathutils as mu


def register():
    pass


def unregister():
    pass
