#!/usr/bin/env python3
""" Windows Installer build script. """
import glob
import subprocess

with open("README.md") as file:
    original_file = file.read()
output_file = original_file.replace(".asc", ".pdf")
output_file = output_file.replace(".md", ".pdf")
with open("README.md", "w") as file:
    file.write(output_file)

for file in glob.glob("*.md"):
    subprocess.call(["mdpdf", file], shell=True)
    pdf_file = file[:-3] + ".pdf"
    subprocess.call(
        ["hexapdf", "optimize", "--compress-pages", "--force", pdf_file, pdf_file],
        shell=True,
    )

for file in glob.glob("docs/*.asc"):
    subprocess.call(["asciidoctor-pdf", "--verbose", file], shell=True)
    pdf_file = file[:-4] + ".pdf"
    subprocess.call(
        ["hexapdf", "optimize", "--compress-pages", "--force", pdf_file, pdf_file],
        shell=True,
    )

subprocess.call(["git", "checkout", "README.md"], shell=True)

subprocess.call(["pyinstaller", "build-windows-installer.spec"], shell=True)
subprocess.call(["iscc", r"inno\installer.iss"], shell=True)
