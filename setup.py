import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "sys", "tkinter", "tkinter.ttk", "math"],
                     "include_files": ["PURPYANG.ICO", "SuperDuper_support.py"]}

company_name = "JonRob Inc"
product_name = "SuperDuper"

bdist_msi_options = {
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    'target_name': "SuperDuper"
    }
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Super Duper",
      version="1.0",
      description="CNC Mill speeds and feeds calculator",
      options={
          'bdist_msi': bdist_msi_options,
          'build_exe': build_exe_options},
      executables=[Executable("SuperDuper.py", base=base, icon='PURPYANG.ICO')])
