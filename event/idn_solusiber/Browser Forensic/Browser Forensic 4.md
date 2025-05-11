# Browser Forensic 4
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !!
(Filenya ada di pertanyaan pertama)
Vpn apa saja yang diinstal oleh user ?
format flag : IDN_FLAG{VPN_1-VPN_2} example : IDN_FLAG{IPSEC_SECURITY-L2TP_SECURITY}

## solve
- Di sini saya mencari tahu VPN apa saja yang diinstal, yang bisa dilihat melalui riwayat (history) atau dari ID extension-nya.
  ![alt text](<images/Browser Forensic 4/image-2.png>)
  ![alt text](<images/Browser Forensic 4/image-1.png>)
- Setelah dicek, terdapat dua VPN yang terdeteksi:
  - Browsec VPN
    ![alt text](<images/Browser Forensic 4/image-3.png>)
  - VeePN
    ![alt text](<images/Browser Forensic 4/image-4.png>)
- setelah itu saya mengecek ke browser untuk melihat
- Saya pun mencoba submit flag dengan berbagai format dan pola, seperti IDN_FLAG{Browsec_VPN-VeePN}, IDN_FLAG{BrowsecVPN_VeePN}, dan banyak variasi lainnya.
- Setelah mencoba berkali-kali dan sempat berhenti selama 3 hari karena frustrasi, akhirnya saya berhasil menemukan format flag yang benar: **IDN_FLAG{Browsec_VPN-VPN_Proxy_VeePN}**

## flag
IDN_FLAG{Browsec_VPN-VPN_Proxy_VeePN}