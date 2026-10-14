:: The pyinstaller command is provided by the pyinstaller Python module, so the command needs to be executed inside a valid Python environment
pyinstaller^
 --add-data "src/labell3r/res/*;labell3r/res"^
 --add-data "LICENSE;."^
 --add-data "licenses/*;licenses"^
 --onedir^
 --name "Labell3R"^
 --icon "src/labell3r/res/labell3r_logo.ico"^
 --noconsole^
 src/labell3r/main.py -y