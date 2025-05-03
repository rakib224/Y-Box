import os
import time
import socket
import platform
import requests
import base64
import hashlib
from pytube import YouTube
import phonenumbers
from phonenumbers import geocoder, carrier

# Colors
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[0m'

def custom_banner():
    print(f"{C} +-----------------------------+")
    print(f" |                             |")
    print(f" |     ____                    |")
    print(f" |    / __ )____  _  __        |")
    print(f" |   / __  / __ \\| |/_/        |")
    print(f" |  / /_/ / /_/ />  <          |")
    print(f" | /_____/\\____/_/|_|          |")
    print(f" |                             |")
    print(f" |      Advanced Tool          |")
    print(f" |    by  Rakib (Y-box)        |")
    print(f" |                             |")
    print(f" +-----------------------------+")
    print(Y + "="*47 + W)

def menu():
    print(G + """
[1] IP Info Checker
[2] Phone Number Info
[3] Ping a Website
[4] My IP Info
[5] YouTube Video Downloader
[6] Device Info
[7] Port Scanner
[8] Website Status Checker
[9] Hash Generator (MD5, SHA256)
[10] File Downloader
[11] Base64 Encode/Decode
[12] Fake Identity Generator
[13] Exit
""" + W)

def ip_info():
    ip = input("Enter IP Address: ")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(G + f"""
IP: {res['query']}
Country: {res['country']}
City: {res['city']}
ISP: {res['isp']}
Org: {res['org']}
Timezone: {res['timezone']}
        """ + W)
    except:
        print(R + "Failed to fetch IP info!" + W)

def my_ip_info():
    try:
        res = requests.get("http://ip-api.com/json/").json()
        print(G + f"""
Your IP: {res['query']}
Country: {res['country']}
City: {res['city']}
ISP: {res['isp']}
Timezone: {res['timezone']}
        """ + W)
    except:
        print(R + "Error fetching your IP info!" + W)

def phone_info():
    number = input("Enter phone number with country code (+880...): ")
    try:
        num = phonenumbers.parse(number)
        location = geocoder.description_for_number(num, 'en')
        sim = carrier.name_for_number(num, 'en')
        print(G + f"Location: {location}\nCarrier: {sim}" + W)
    except:
        print(R + "Invalid phone number!" + W)

def ping_site():
    site = input("Enter website (example.com): ")
    os.system(f"ping -c 4 {site}")

def youtube_downloader():
    link = input("Enter YouTube video link: ")
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        print(G + f"Downloading: {yt.title}..." + W)
        stream.download()
        print(G + "Download completed!" + W)
    except:
        print(R + "Download failed. Invalid link or no internet." + W)

def device_info():
    print(G + f"""
System: {platform.system()}
Node Name: {platform.node()}
Release: {platform.release()}
Version: {platform.version()}
Machine: {platform.machine()}
Processor: {platform.processor()}
    """ + W)

def port_scanner():
    host = input("Enter host (e.g. example.com): ")
    print("Scanning ports 1-100...")
    for port in range(1, 101):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(G + f"Port {port} is OPEN" + W)
        s.close()

def website_checker():
    url = input("Enter website URL (with http/https): ")
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print(G + "Website is UP!" + W)
        else:
            print(Y + f"Site returned status: {r.status_code}" + W)
    except:
        print(R + "Website is DOWN or URL invalid!" + W)

def hash_generator():
    text = input("Enter text to hash: ")
    print(G + f"""
MD5: {hashlib.md5(text.encode()).hexdigest()}
SHA256: {hashlib.sha256(text.encode()).hexdigest()}
    """ + W)

def file_downloader():
    url = input("Enter direct file URL: ")
    name = input("Save as (filename.ext): ")
    try:
        r = requests.get(url)
        with open(name, 'wb') as f:
            f.write(r.content)
        print(G + f"Downloaded as {name}" + W)
    except:
        print(R + "Download failed!" + W)

def base64_tool():
    choice = input("Encode or Decode? (e/d): ")
    if choice == 'e':
        text = input("Enter text to encode: ")
        encoded = base64.b64encode(text.encode()).decode()
        print(G + f"Encoded: {encoded}" + W)
    elif choice == 'd':
        code = input("Enter base64 code: ")
        try:
            decoded = base64.b64decode(code).decode()
            print(G + f"Decoded: {decoded}" + W)
        except:
            print(R + "Invalid base64 code!" + W)
    else:
        print(R + "Invalid choice!" + W)

def fake_identity():
    try:
        res = requests.get("https://randomuser.me/api/").json()['results'][0]
        print(G + f"""
Name: {res['name']['first']} {res['name']['last']}
Email: {res['email']}
Username: {res['login']['username']}
Phone: {res['phone']}
Location: {res['location']['city']}, {res['location']['country']}
        """ + W)
    except:
        print(R + "Failed to generate identity!" + W)

def main():
    while True:
        custom_banner()
        menu()
        ch = input("Select Option: ")

        if ch == '1':
            ip_info()
        elif ch == '2':
            phone_info()
        elif ch == '3':
            ping_site()
        elif ch == '4':
            my_ip_info()
        elif ch == '5':
            youtube_downloader()
        elif ch == '6':
            device_info()
        elif ch == '7':
            port_scanner()
        elif ch == '8':
            website_checker()
        elif ch == '9':
            hash_generator()
        elif ch == '10':
            file_downloader()
        elif ch == '11':
            base64_tool()
        elif ch == '12':
            fake_identity()
        elif ch == '13':
            print(Y + "Goodbye from Y-box!" + W)
            break
        else:
            print(R + "Invalid Option!" + W)
        input(Y + "\nPress Enter to continue..." + W)

if __name__ == "__main__":
    main()
