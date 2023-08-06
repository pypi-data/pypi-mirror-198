import sys
import os
import shutil



from distutils.dir_util import copy_tree
if os.path.isdir("Flet_StoryBoard"):
    print("Please reType the command again.")
    shutil.rmtree('Flet_StoryBoard')
    sys.exit()

os.mkdir("Flet_StoryBoard")
os.mkdir("Flet_StoryBoard/Flet_StoryBoard")
open("Flet_StoryBoard/pyodide.py", "w+", encoding="utf-8").write("from .Flet_StoryBoard.pyodide import *")
open("Flet_StoryBoard/__init__.py", "w+", encoding="utf-8").write("from .Flet_StoryBoard import *; from .Flet_StoryBoard.loadFletStoryboard import load_flet_storyboard")
open("Flet_StoryBoard/README.md", "w+", encoding="utf-8").write("This is the Flet_StoryBoard library. please do NOT play with it without understanding your actions.")
current = str(__file__).replace("pyodide.py", "")
copy_tree(f"{current}", "Flet_StoryBoard/Flet_StoryBoard")