# Step By Step
- **Check the Open Ports** \
Langkah pertama adalah memeriksa port yang terbuka pada target dengan menggunakan alat seperti nmap. Berikut adalah hasil dari pemindaian port:
- **Check the Versions and Vulnerabilities** \
Setelah mengetahui port yang terbuka, langkah berikutnya adalah memeriksa versi layanan yang berjalan pada port tersebut untuk mencari potensi **CVE (Common Vulnerabilities and Exposures)** atau kerentanannya.
- **Directory Discovery (Finding Hidden Directories and Files)** \
Langkah berikutnya adalah mencari direktori atau file yang tersembunyi pada server menggunakan tools seperti gobuster, dirsearch, atau dirbuster. Hal ini membantu untuk menemukan area tersembunyi yang mungkin memiliki potensi kerentanannya.
- **Explore the Found Directories** \
Setelah menemukan direktori yang menarik, kamu bisa mencoba untuk mengaksesnya secara manual melalui browser atau menggunakan tools seperti curl untuk mengeksplorasi lebih lanjut. Di tahap ini, kamu akan mencari potensi untuk melakukan exploitation atau privilege escalation.
- **Vulnerability Analysis and Exploit (Optional)** \
Jika sudah menemukan celah atau kerentanannya, kamu bisa mencoba untuk mengeksploitasi celah tersebut. Ini bisa melibatkan teknik seperti:
  - **SQL Injection**
  - **RCE (Remote Code Execution)**
  - **Command Injection**
  - **LFI/RFI (Local/Remote File Inclusion)**
- **Post-Exploitation and Cleanup**
Jika eksploitasi berhasil dan kamu mendapatkan akses ke sistem, langkah berikutnya adalah melakukan post-exploitation, seperti mengumpulkan data lebih lanjut, mendapatkan akses root, atau mencari informasi sensitif. Pastikan untuk melakukan clean-up jika kamu bekerja dalam lingkungan uji coba atau CTF (Capture The Flag) untuk menghindari perubahan permanen pada sistem target.