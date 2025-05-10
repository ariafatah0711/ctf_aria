# Browser Forensic 4
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !!
(Filenya ada di pertanyaan pertama)
Vpn apa saja yang diinstal oleh user ?
format flag : IDN_FLAG{VPN_1-VPN_2} example : IDN_FLAG{IPSEC_SECURITY-L2TP_SECURITY}

## solve
- disini saya mencari vpn apa saja yang di install bisa dilihat di history atau di extension id nya
  ![alt text](<images/Browser Forensic 4/image-2.png>)
  ![alt text](<images/Browser Forensic 4/image-1.png>)
- disini pas dilhat terdapat 2 vpn
  ![alt text](<images/Browser Forensic 4/image-3.png>)
  ![alt text](<images/Browser Forensic 4/image-4.png>)
- dan saya coba submit flagnya dengan berbagai format dan pola seperti IDN_FLAG{Browsec_VPN-VeePN}, IDN_FLAG{Browsec_VPN-VeePN}, dan banyak lagi dan setelah mencoba sekian banyak dan sempet berhenti 3 harian saya akhirnya berhasil mendapatkan flagnya

## flag
IDN_FLAG{Browsec_VPN-VPN_Proxy_VeePN}