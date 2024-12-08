# by chat gpt
import os

# Template untuk README.md header
header = """# ctf_aria

This file is what I studied while learning CTF

<p align="center">
  <a href="#introduction">introduction</a> •
  <a href="#file-list">file_list</a> •
  <a href="#table-of-contents">table of contents</a> •
  <a href="#download">Download</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

<p id="introduction"></p>

## 🚀 introduction

<p align="left"> 
  <a href="#">
    <img alt="Capture The Flag" src="https://img.shields.io/badge/-Capture%20The%20Flag-FF5733?style=flat-square&logo=flag&logoColor=white" />
  </a>
</p>

<p id="table-of-contents"></p>

## 📋 Table of Contents
<details>
  <summary><b>List Resources</b></summary>

  - JEOPARDY
    - https://play.picoctf.org
  - BOOT TO ROOT
    - https://hacktrace-ranges.id
</details>

<p id="file-list"></p>

# 📄 File List
"""

footer = """<p id="download"></p>

## 🔨 download

1. Open a terminal or command prompt on your computer.
2. Navigate to the directory where you want to save this project.
3. Use the following command to download the project from the GitHub repository:
```sh
git clone https://github.com/ariafatah0711/ctf_aria.git
```

<p id="related"></p>

## 📈 related

<p id="license"></p>

## ©️ license
<a href="https://github.com/ariafatah0711" alt="CREATED"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=CREATED%20BY&message=ariafatah0711&color=000000"></a>
<a href="https://github.com/ariafatah0711/ariafatah0711/blob/main/LICENSE" alt="LICENSE"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=LICENSE&message=MIT&color=000000"></a>
"""

# Fungsi untuk membuat daftar file markdown
def generate_file_list(path):
    output = ""
    for dirpath, dirnames, filenames in os.walk(path):
        if dirpath == path:
            continue
        
        markdown_files = sorted([f for f in filenames if f.endswith('.md')])
        if markdown_files:
            relative_path = os.path.relpath(dirpath, root_path)
            folder_name = os.path.basename(relative_path)

            # output += f"<details>\n<summary><b>{relative_path}</b></summary>\n\n"
            output += f"<details>\n<summary><b>{relative_path}</b></summary>\n<ul>\n"            

            for file in markdown_files:
                # Ganti spasi dengan %20 untuk URL
                file_path = os.path.join(relative_path, file).replace("\\", "/").replace(" ", "%20")
                # output += f"- [{file}]({file_path})\n"
                output += f" <li><a href='{file_path}'>{file}</a></li>\n"
              
            output += "</ul>\n"
            output += "\n</details>\n\n"
    return output

# Hasilkan isi File List
root_path = "."
file_list_content = generate_file_list(root_path)
markdown_content = header + file_list_content + footer

# Tulis ke README.md
with open("README.md", "w", encoding='utf-8') as readme:
    readme.write(markdown_content)

print("README.md updated successfully!")
