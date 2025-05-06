# USB Forensic 1
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
Merek usb apa yang dipakai oleh hacker untuk delivery file nya ? \
format flag : IDN_FLAG{Nama_Device_Ukuran_USB_Device}

## tools
- registry explorer
- reglookup
- regripper

## solve
- disini saya maasih belum terlalu paham dengan usb forensic dan saya meminta bantuan chat gpt untuk membantu saya
- disini saya mencoba menemukan beberapa tools seperti **reglookup**, dll
- disini saya mencoba tools reglookup dan melakukan hive pada file 
  ![alt text](<images/USB Forensic 1/image.png>)
  ```bash
  ls
  MountPoints2.hiv  NTUSER.dat  RecentDocs.hiv  USBTOR.hiv  USRCLASS.dat

  reglookup USBTOR.hiv 
  PATH,TYPE,VALUE,MTIME
  /,KEY,,2025-05-03 03:44:25
  /Disk&Ven_JetFlash&Prod_Transcend_8GB&Rev_8.07,KEY,,2025-05-03 03:44:25
  /Disk&Ven_JetFlash&Prod_Transcend_8GB&Rev_8.07/XRVZQBFR&0,KEY,,2025-05-03 03:44:25
  /Disk&Ven_JetFlash&Prod_Transcend_8GB&Rev_8.07/XRVZQBFR&0/DeviceDesc,SZ,@disk.inf%2C%25disk_devdesc%25;Disk drive,
  ```
- setelah itu saya mencoba beberapa format seperti **IDN_FLAG{JetFlash_Transcend_8GB}**, **IDN_FLAG{Transcend_8GB}**, dll.
- setelah mencoba banyak saya menemukan flag yang benar yaitu **IDN_FLAG{JetFlash_Transcend_8GB_USB_Device}**

## flag
IDN_FLAG{JetFlash_Transcend_8GB_USB_Device}