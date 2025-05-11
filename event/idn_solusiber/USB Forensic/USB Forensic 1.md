# USB Forensic 1
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
Merek usb apa yang dipakai oleh hacker untuk delivery file nya ? \
format flag : IDN_FLAG{Nama_Device_Ukuran_USB_Device}

## tools
- reglookup, regripper (linux)
- registry explorer, shellbags (windows)

## solve
- Saya masih belum terlalu memahami USB forensics, sehingga saya meminta bantuan ChatGPT untuk membantu memandu proses analisis.
- Dalam pencarian flag, saya mencoba mengeksplorasi beberapa tools yang umum digunakan dalam analisis registry, salah satunya adalah reglookup. Saya menggunakan tool ini untuk melakukan analisis terhadap beberapa file registry (hive), seperti:
  ```
  MountPoints2.hiv  
  NTUSER.dat  
  RecentDocs.hiv  
  USBTOR.hiv  
  USRCLASS.dat
  ```
- Kemudian, saya menjalankan perintah: ```reglookup USBTOR.hiv```
  ![alt text](<images/USB Forensic 1/image.png>)
- Dari informasi tersebut, saya mencoba menebak beberapa kemungkinan format flag, seperti:
  - IDN_FLAG{JetFlash_Transcend_8GB}
  - IDN_FLAG{Transcend_8GB}
- Namun, setelah beberapa kali mencoba berbagai kombinasi, saya akhirnya menemukan format flag yang benar, yaitu: **IDN_FLAG{JetFlash_Transcend_8GB_USB_Device}**

## flag
IDN_FLAG{JetFlash_Transcend_8GB_USB_Device}