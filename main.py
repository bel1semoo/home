from xml.dom import minidom
import os
import subprocess

subprocess.call("netsh wlan show profile")
subprocess.call("netsh wlan export profile folder=C:\\ key=clear")

for file in os.listdir("C:/"):
    if file.endswith(".xml"):
        document = minidom.parse(f"C:/{file}")
        wifi = {
            "name": document.getElementsByTagName("name")[0].firstChild.data,
            "password": document.getElementsByTagName("keyMaterial")[0].firstChild.data
        }

        print(wifi)
a = input()
        #  with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
        #     file.write(f'Profile: {wifi["name"]}\nPassword: {wifi["password"]}\n{"#" * 20}\n')

        # my_file = open("passwordandname.txt", "w+")
        # my_file.write(wifi)
        # my_file.close()
