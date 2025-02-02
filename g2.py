import os, re

header = """# ctf_aria

This file is what I studied while learning CTF

<p align="center">
  <a href="#introduction">introduction</a> •
  <a href="#table-of-contents">table of contents</a> •
  <a href="#file-list">file_list</a> •
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

<b>List Resources</b>

<ul>
  <li>Platform JEOPARDY<ul>
    <li><a href="https://play.picoctf.org">picoctf</a></li>
    <li><a href="https://overthewire.org">overthewire</a></li>
    <li><a href="https://ringzer0ctf.com">ringzer0ctf</a></li>
    <li><a href="https://labex.io">labex</a></li>
    <li><a href="https://pwn.college">pwn.college</a></li>
  </ul></li>
  <li>Platform BOOT TO ROOT<ul>
    <li><a href="https://hacktrace-ranges.id">hacktrace-ranges</a></li>
    <li><a href="https://tryhackme.com">tryhackme</a></li>
    <li><a href="https:/www.hackthebox.com">hackthebox</a></li>
  </ul></li>
  <li>MATERIAL<ul>
    <li><a href="https://dimasma0305.github.io/Cyber-Security-Learning-Resources/Resource_List/Link_Bermanfaat">material list dimasma0305</a></li>
    <li><a href="https://book.hacktricks.xyz/crypto-and-stego/stego-tricks">hacktricks stego</a></li>
    <li><a href="https://www.quipqiup.com/">subsitusi cipher</a></li>
  </ul></li>
   <li>Write Up Lomba Yang Saya Ikuti<ul>
    <li><a href="https://drive.google.com/drive/folders/1vyxHyRjd-YIiS12Yys3Tfl03jCzN8Q5a?usp=sharing">LKSP Jawa Barat 2024 (#2) 3/5 flag</a></li>
    <li><a href="https://drive.google.com/drive/folders/1BdVNx5qjON1tRhbKsVNTvZAf4j1kbIcK?usp=sharing">HIDC 2024 (#36)</a></li>
    <li><a href="https://drive.google.com/drive/folders/1tWKEWgygs_bMwF3wFQvLpKDsLTb0dqCA?usp=sharing">Cyber Nexus 2024 (#) 2/19 flag</a></li>
  </ul></li>
</ul>

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

def generate_file_list(path, output_type="md"):
    output = ""
    exclude_dirs = {r"\.git", r"tool", r"_bak", r"_layouts", r"thm_learn", r"\.vscode", r"_includes", r"docs"}
    folder_structure = {}

    def is_excluded(dirname):
        return any(re.match(pattern, dirname, re.IGNORECASE) for pattern in exclude_dirs)

    for dirpath, dirnames, filenames in os.walk(path):
        dirnames[:] = [d for d in dirnames if not is_excluded(d)]
        
        if dirpath == path:
            continue
        
        markdown_files = sorted([f for f in filenames if f.lower().endswith('.md')])
        if not markdown_files:
            continue  # Skip folders without markdown files

        relative_path = os.path.relpath(dirpath, path)
        parts = relative_path.split(os.sep)
        
        # Menyusun struktur folder
        current_level = folder_structure
        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
        
        current_level["_files"] = markdown_files
    
    def generate_html(nested_dict, parent_path="", first_level=True):
        html = ""
        for key, value in nested_dict.items():
            if key == "_files":
                html += "<ul>\n"
                for file in value:
                    file_path = os.path.join(parent_path, file).replace("\\", "/").replace(" ", "%20")
                    if output_type == "html":
                        file_path = file_path.replace(".md", ".html")
                    file_name = os.path.splitext(file)[0]
                    html += f"  <li><a href='{file_path}'>{file_name}</a></li>\n"
                html += "</ul>\n"
            else:
                new_parent_path = os.path.join(parent_path, key).replace("\\", "/")
                style = " style='margin: 20px; color: #fc0;'" if first_level==False else ""
                html += f"<details>\n<summary{style}><b>{key}</b></summary>\n"
                html += generate_html(value, new_parent_path, first_level=False)
                html += "</details>\n\n"
        return html
    
    return generate_html(folder_structure)

root_path = "."
# md
file_list_content_md = generate_file_list(root_path, "md")
markdown_content_md = header + file_list_content_md + footer
# html
file_list_content_html = generate_file_list(root_path, "html")
markdown_content_html = header + file_list_content_html + footer

# write
with open("README.md", "w", encoding='utf-8') as readme:
    readme.write(markdown_content_md)

with open("index.md", "w", encoding='utf-8') as readme:
    readme.write(markdown_content_html)

print("README.md updated successfully!")