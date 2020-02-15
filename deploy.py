#!/usr/bin/env python3
""" PyPI Deployment and pyinstaller build script - automated, idiot-proofed from my own idiocy.
    Feel free to modify this monstrosity for use in your own projects.
    Note that it's HIGHLY Windows-centric. """
import glob
import os
import re
import subprocess
import sys
import time

VERSION_FILENAME = "src/basicwrangler/version.py"

# Initial warnings.

print(
    "First, you need to make sure that you have committed any changes you want to commit, and that you've merged that branch into whatever your release branch is."
)
print("You should also have checked out the release branch.")
print("Check git log to make sure you've got everything the way you want it.")
print("MAKE SURE THAT git status COMES UP CLEAN!!!")
check = input("Have you done this? Do you want to continue?\n")
if check != "y":
    sys.exit()

# This section automatically bumps the version number.

print("")
print("The following question asks if you want to change your version number.")
print(
    "If yes, it will bump the number in whatever files you have listed in this script, and it will add the changes, commit the changes, and push those changes."
)
print("")
with open(VERSION_FILENAME) as file:
    setup_file = file.read()
old_version_match = re.search(r"__version__ = \"(?P<version>.*?)\"", setup_file)
old_version = old_version_match.group("version")
print("The old version is: " + old_version)
check = input("Do you want to bump your version number? (y/n)\n")
if check == "y":
    """ Bumps the version number. Not terribly bright, but as long as the old version number ONLY
        exists as an actual version number, it will work without messing stuff up. """
    new_version = input("Type in the new version number:\n")
    print("")
    print("Bumping version number...")
    time.sleep(3)
    print("")
    with open(VERSION_FILENAME) as file:
        old_file = file.read()
    new_file = re.sub(old_version, new_version, old_file)
    with open(VERSION_FILENAME, "w") as file:
        file.write(new_file)
    print("")
    subprocess.call(["git", "add", "."], shell=True)
    command = ["git", "commit", "-m", f"Bumped version to v{new_version} for release."]
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print(stdout.decode("utf-8"))
    print(stderr.decode("utf-8"))
    print("")
    # Tells you to push the commit... YOURSELF.
    check = "n"
    while check != "y":
        check = input(
            "You should check your git log, then push the version bump to your git repo. Once you've done that, type y.\n"
        )
else:
    new_version = old_version

# This section builds the source distribution and wheel files for PyPI.

print("")
print("Building PyPI distribution files...")
time.sleep(3)
print("")
print("Building PyPI source distribution file...")
time.sleep(3)
print("")
subprocess.call(["python", "setup.py", "sdist"], shell=True)
print("")
print("Building PyPI wheel distribution file...")
time.sleep(3)
print("")
subprocess.call(["python", "setup.py", "bdist_wheel"], shell=True)
print("")
""" The following lines optimize the compression on the distribution files.
    This should be removed if you don't have the proper programs/batch files.
    I might eventually post those files amongst others in a git repo. """
print("")
print("Optimizing distribution files...")
time.sleep(3)
print("")
os.chdir("dist")
subprocess.call(["advdef", "-z", "-2", "*.gz"], shell=True)
subprocess.call(["advdef", "-z", "-3", "*.gz"], shell=True)
subprocess.call(["advdef", "-z", "-4", "*.gz"], shell=True)
subprocess.call(["deflopt", "/d", "*.gz"], shell=True)
subprocess.call(["ren", "*.whl", "*.zip"], shell=True)
subprocess.call(["rezip"], shell=True)
subprocess.call(["ren", "*.zip", "*.whl"], shell=True)
os.chdir("..")
print("")
print("Checking long description in distribution files...")
time.sleep(3)
print("")
subprocess.call(
    ["twine", "check", "dist/*"], shell=True,
)
print("")
check = "n"
while check != "y":
    check = input(
        "You might want to install the dist files in a venv now if you want. Once you've done that, type y.\n"
    )
print("")
# This next section uses twine to upload your distribution files to PyPI.
check = input("Do you want to upload your distribution files to PyPI? (y/n)\n")
if check == "y":
    print("")
    print("Uploading distribution files to PyPI...")
    time.sleep(3)
    print("")
    subprocess.call(
        ["twine", "upload", "dist/*"], shell=True,
    )
print("")

# This next section builds PDF documentation from the .md and .asc source files.
# It is hardcoded right now for my project. Change what you need to.

print("Building PDF documentation files...")
time.sleep(3)
print("")
# Edits the README to link to PDF files instead of source files.
with open("README.md") as file:
    original_file = file.read()
output_file = original_file.replace(".asc", ".pdf")
output_file = output_file.replace(".md", ".pdf")
with open("README.md", "w") as file:
    file.write(output_file)

# Builds PDF files from markdown files. Uses mdpdf from node.js and hexapdf from ruby.
for file in glob.glob("*.md"):
    subprocess.call(["mdpdf", file], shell=True)
    pdf_file = file[:-3] + ".pdf"
    subprocess.call(
        ["hexapdf", "optimize", "--compress-pages", "--force", pdf_file, pdf_file],
        shell=True,
    )

# Builds PDF file from asciidoc file. Uses asciidoctor-pdf and hexapdf from ruby.
for file in glob.glob("docs/*.asc"):
    subprocess.call(["asciidoctor-pdf", "--verbose", file], shell=True)
    pdf_file = file[:-4] + ".pdf"
    subprocess.call(
        ["hexapdf", "optimize", "--compress-pages", "--force", pdf_file, pdf_file],
        shell=True,
    )

print("")
# Reverts the changes to the README.
command = ["git", "checkout", "README.md"]
p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
print(stdout.decode("utf-8"))
print(stderr.decode("utf-8"))
print("")
print("Building PDF Documentation zip file...")
time.sleep(3)
print("")
# Make a copy of the PDF in the docs subfolder.
subprocess.call(["copy", r"docs\*.pdf", "."], shell=True)
# Zips up the documentation. Uses 7zip.
subprocess.call(
    [
        "C:/Program Files/7-Zip/7z.exe",
        "a",
        "-tzip",
        "dist/BASIC-Wrangler-" + new_version + "-PDF-Documentation.zip",
        "*.pdf",
    ],
    shell=True,
)
# Optimizes the docs zip file. Can be omitted if you don't have the rezip batch file.
print("")
print("Optimizing PDF Documentation zip file...")
time.sleep(3)
print("")
os.chdir("dist")
subprocess.call(["rezip"], shell=True)
os.chdir("..")
print("")

# pyinstaller build section.

print("")
print("Building Windows 32-bit pyinstaller version...")
time.sleep(3)
print("")
""" Builds pyinstaller Windows 32-bit version.
    Uses a 32-bit Python venv in ..\32-bit-build with pyinstaller and other dependencies installed.
    Then I modified the activate.bat script to run pyinstaller build.spec at the end and called it
    installer.bat and kept that in the Scripts directory in the venv.
    It's pretty hacky, I know, but I don't know how to make it build with 32-bit Python otherwise. """
subprocess.call(
    r"..\32-bit-build\Scripts\installer.bat", shell=True,
)
print("")
print("Building Inno Setup Installer...")
time.sleep(3)
print("")
# Builds the installer for the Windows version. Requires Inno Setup to be in your system path.
subprocess.call(
    ["iscc", f"/dMyAppVersion={new_version}", r"inno\installer.iss"], shell=True
)

print("")
print(
    "You should now upload your docs and Windows Installer contained in the dist subdirectory!"
)
