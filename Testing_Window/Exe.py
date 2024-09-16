import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

# os.environ['TCL_LIBRARY'] = r"C:/Users/divyesh.hadvani/AppData/Local/Programs/Python/Python38-32/tcl/tcl8.6"
# os.environ['TK_LIBRARY'] = r"C:/Users/divyesh.hadvani/AppData/Local/Programs/Python/Python38-32/tcl/tk8.6"

os.environ['TCL_LIBRARY'] = r"C:\Users\divyesh.hadvani\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\divyesh.hadvani\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base,icon="UDTE_icon.ico")]

cx_Freeze.setup(
    name = "Track_Tester",
    options = {"build_exe": {"packages":["os","sys"], "include_files":['tcl86t.dll','tk86t.dll','UDTE_icon.ico','logo.png','p.p']}},
    version = "1.0",
    description = "TrackTester for Stent| Developed by Divyesh Hadvani ",
    executables = executables
    )
