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

import bmesh

import os
from bpy_extras.io_utils import ImportHelper


class TEMPLATE_ImportOperator(bpy.types.Operator, ImportHelper):
    bl_idname = ""
    bl_label = ""
    bl_description = ""

    filter_glob: bpy.props.StringProperty(default="*.txt", options={"HIDDEN"})
    files: bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)

    def execute(self, context):
        folder = os.path.dirname(self.filepath)
        # iterate through the selected files
        for j, i in enumerate(self.files):
            # generate full path to file
            path_to_file = os.path.join(folder, i.name)
            # run(path_to_file)
        return {"FINISHED"}


class TEMPLATE_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        pass


classes = (TEMPLATE_ImportOperator, TEMPLATE_AddonPreferences)


# def menu_func_import(self, context):
#     self.layout.operator(ImportOperator.bl_idname, text="Text files (.txt)")


def register():
    for c in classes:
        bpy.utils.register_class(c)
    # bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    for c in classes[::-1]:
        bpy.utils.unregister_class(c)
    # bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
