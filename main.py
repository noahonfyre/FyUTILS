import concurrent.futures
import datetime
import json
import multiprocessing
import os
import platform
import random
import socket
import sys
import threading
import time

import paramiko
import psutil
import requests
import pwinput
from colorama import Fore, init
from pypresence import Presence
from pathlib import Path
from pytube import YouTube
import scapy.layers.l2 as scapy

init(convert=True)


def prefix(type):
    if threading.current_thread().name == "MainThread":
        current_thread_name = "FyUTILS"
    else:
        current_thread_name = threading.current_thread().name

    if type == "INFO":
        return accent_color + "[" + color + datetime.datetime.now().strftime("%H:%M:%S") + accent_color + "]" + " " + accent_color + "[" + text_color + current_thread_name + accent_color + "/" + Fore.LIGHTGREEN_EX + "INFO" + accent_color + "] " + text_color
    elif type == "ERROR":
        return accent_color + "[" + color + datetime.datetime.now().strftime("%H:%M:%S") + accent_color + "]" + " " + accent_color + "[" + text_color + current_thread_name + accent_color + "/" + Fore.RED + "ERROR" + accent_color + "] " + text_color
    elif type == "INIT":
        return accent_color + "[" + color + datetime.datetime.now().strftime("%H:%M:%S") + accent_color + "]" + " " + accent_color + "[" + text_color + current_thread_name + accent_color + "/" + color + "INIT" + accent_color + "] " + text_color
    elif type == "FUEL":
        return accent_color + "[" + color + datetime.datetime.now().strftime("%H:%M:%S") + accent_color + "]" + " " + accent_color + "[" + text_color + current_thread_name + accent_color + "/" + Fore.LIGHTMAGENTA_EX + "FUEL" + accent_color + "] " + text_color
    elif type == "SHIELD":
        return accent_color + "[" + color + datetime.datetime.now().strftime("%H:%M:%S") + accent_color + "]" + " " + accent_color + "[" + text_color + current_thread_name + accent_color + "/" + Fore.YELLOW + "SHIELD" + accent_color + "] " + text_color
    elif type == "RECOVERY":
        return accent_color + "[" + color + datetime.datetime.now().strftime("%H:%M:%S") + accent_color + "]" + " " + accent_color + "[" + text_color + current_thread_name + accent_color + "/" + Fore.RED + "RECOVERY" + accent_color + "] " + text_color
    else:
        return accent_color + "[" + color + datetime.datetime.now().strftime("%H:%M:%S") + accent_color + "]" + " " + accent_color + "[" + text_color + current_thread_name + accent_color + "/" + Fore.WHITE + str(type).upper() + accent_color + "] " + text_color


def update_status(status):
    os.system("title FyUTILS " + version + " - " + username + "@" + device + " - " + status)
    try:
        rpc.update(
            state=status, details=username + "@" + device, small_image="python",
            large_image="large",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(start_time))
    except:
        None


def update_ssh_status(status):
    os.system("title FyUTILS " + version + " - " + user + "@" + server + " - " + status)
    try:
        rpc.update(
            state="[REMOTE] " + status, details=user + "@" + server, small_image="ssh",
            large_image="large",
            buttons=[{"label": "Get FyUTILS", "url": "https://github.com/NoahOnFyre/FyUTILS/releases/latest"},
                     {"label": "View Project", "url": "https://github.com/NoahOnFyre/FyUTILS/"}],
            small_text="Python", large_text="FyUTILS v" + version,
            start=int(start_time))
    except:
        None


def resolve_fuel_information(file):
    fuel = open(fuel_content_dir + file)
    fuel_json = json.load(fuel)
    print(prefix("FUEL") + "FUEL information of: " + file)
    print(prefix("FUEL") + "FUEL name: " + fuel_json["name"])
    print(prefix("FUEL") + "FUEL version: v" + fuel_json["version"])
    print(prefix("FUEL") + "FUEL author: " + fuel_json["author"])
    print(prefix("FUEL") + "FUEL description: " + fuel_json["description"])
    print(prefix("FUEL") + "FUEL format: " + str(fuel_json["format"]))
    print(prefix("FUEL") + "FUEL type: " + fuel_json["properties"]["type"])
    match fuel_json["properties"]["type"]:
        case "DEFAULT":
            print(prefix("FUEL") + "FUEL command name: " + fuel_json["properties"]["command_name"])
            print(prefix("FUEL") + "Head enabled: " + str(fuel_json["head"]["enabled"]))
            print(prefix("FUEL") + "Body enabled: " + str(fuel_json["body"]["enabled"]))
            print(prefix("FUEL") + "Argument length: " + str(fuel_json["head"]["argument_length"]))
            print(prefix("FUEL") + "Command status: " + fuel_json["head"]["status"])
            fuel_command_list.append(fuel_json["properties"]["command_name"])

        case "MIXIN":
            print(prefix("FUEL") + "Injecting from " + file)
            for line in list(fuel_json["mixin"]):
                exec(line)

        case _:
            print(prefix("FUEL") + "FUEL type is not supported by this version.")
    fuel.close()


def menu():
    os.system("cls")
    print(color + "  __________               _____  __   ________   ________   ______       ________")
    time.sleep(1/1000)
    print(color + "  ___  ____/  _____  __    __  / / /   ___  __/   ____  _/   ___  /       __  ___/")
    time.sleep(1/1000)
    print(color + "  __  /_      __  / / /    _  / / /    __  /       __  /     __  /        _____ \ ")
    time.sleep(1/1000)
    print(color + "  _  __/      _  /_/ /     / /_/ /     _  /       __/ /      _  /___      ____/ / ")
    time.sleep(1/1000)
    print(color + "  /_/         _\__, /      \____/      /_/        /___/      /_____/      /____/  ")
    time.sleep(1/1000)
    print(color + "             ___/  /")
    time.sleep(1/1000)
    print(color + "            /_____/ " + " "*8 + accent_color + "v" + text_color + version.replace(".", accent_color + "." + text_color) + accent_color + " | " + text_color + "Made by NoahOnFyre")
    time.sleep(1/1000)
    print("")
    time.sleep(1/1000)
    print(accent_color + "╔" + "═"*119)
    time.sleep(1/1000)
    print(accent_color + "║ " + accent_color + "[" + color + "VAR" + accent_color + "] " + text_color + "Username: " + username)
    time.sleep(1/1000)
    print(accent_color + "║ " + accent_color + "[" + color + "VAR" + accent_color + "] " + text_color + "Device: " + device)
    time.sleep(1/1000)
    print(accent_color + "║ " + accent_color + "[" + color + "VAR" + accent_color + "] " + text_color + "Version: " + version)
    time.sleep(1/1000)
    if update_available:
        print(accent_color + "╠" + "═"*119)
        time.sleep(1/1000)
        print(accent_color + "║ " + accent_color + "[" + color + "UPDATE" + accent_color + "] " + text_color + "A new version of FyUTILS is available! Install it now using \"update\".")
        time.sleep(1/1000)
        print(accent_color + "║ " + accent_color + "[" + color + "UPDATE" + accent_color + "] " + text_color + "Current version: " + Fore.RED + version)
        time.sleep(1/1000)
        print(accent_color + "║ " + accent_color + "[" + color + "UPDATE" + accent_color + "] " + text_color + "Target version: " + Fore.GREEN + newest_version)
        time.sleep(1/1000)
    print(accent_color + "╚" + "═"*119)


# INIT PHASE
os.system("title FyUTILS")

# Color initialization

color = Fore.LIGHTBLUE_EX
accent_color = Fore.LIGHTBLACK_EX
text_color = Fore.WHITE

# Variable initialization
try:
    print(prefix("INIT") + "Initializing system variables...")
    username = os.getlogin()
    print(prefix("INIT") + "Username: " + username)
    device = platform.node()
    print(prefix("INIT") + "Device: " + device)
    start_time = time.time()
    print(prefix("INIT") + "Start time: " + str(start_time))
    current_dir = sys.path.__getitem__(0)
    print(prefix("INIT") + "Directory: " + current_dir)
    version = "1.4.4"
    print(prefix("INIT") + "Version: " + version)
    threads = multiprocessing.cpu_count()
    print(prefix("INIT") + "ThreadWorkers: " + str(threads))
    user_dir = str(Path.home())
    print(prefix("INIT") + "User specific directory: " + user_dir)
    appdata_dir = user_dir + "\\AppData"
    print(prefix("INIT") + "AppData directory: " + appdata_dir)
    fyutils_appdata_dir = user_dir + "\\AppData\\Roaming\\FyUTILS\\"
    print(prefix("INIT") + "FyUTILS AppData directory: " + fyutils_appdata_dir)
    tmp_dir = user_dir + "\\AppData\\Roaming\\FyUTILS\\tmp\\"
    print(prefix("INIT") + "Temp files directory: " + tmp_dir)
    download_content_dir = current_dir + "\\DownloadedContent\\"
    print(prefix("INIT") + "Download Content Location: " + download_content_dir)
    fuel_content_dir = current_dir + "\\FUELS\\"
    print(prefix("INIT") + "FUEL Content Location: " + fuel_content_dir)
    cpu = platform.processor()
    print(prefix("INIT") + "CPU: " + cpu)
    releases = "https://api.github.com/repos/NoahOnFyre/FyUTILS/releases"
    print(prefix("INIT") + "Releases URL: " + releases)
    memory_amount = psutil.virtual_memory().total
    print(prefix("INIT") + "Memory amount: " + str(round(memory_amount/1024/1024)) + "MB")
except Exception as e:
    print(prefix("ERROR") + "Failed to get system variables!")
    print(prefix("ERROR") + "Shutting down...")
    print(e)
    os.system("pause")
    sys.exit(2048)

# Update checker
print(prefix("INIT") + "Checking for updates...")
try:
    releases_json = requests.get(releases).json()
    newest_release = releases_json[0]
    for r in range(len(newest_release["assets"])):
        if newest_release["assets"][r]["name"] == "main.py":
            release_download_url = newest_release["assets"][r]["browser_download_url"]
            break
        else:
            continue
    newest_version = newest_release["tag_name"]
    if version != newest_version:
        print(prefix("INIT") + "A new version of FyUTILS is available!")
        print(prefix("INIT") + "Current version identifier: " + version)
        print(prefix("INIT") + "Newest version identifier: " + newest_version)
        update_available = True
    else:
        print(prefix("INIT") + "No update found!")
        print(prefix("INIT") + "Current version identifier: " + version)
        print(prefix("INIT") + "Newest version identifier: " + newest_version)
        update_available = False
except Exception as e:
    print(prefix("ERROR") + "Checking for updates failed. Please check your internet connection.")
    print(prefix("ERROR") + "Possible error: " + str(e))
    update_available = False

# Discord RPC initialization
try:
    print(prefix("INIT") + "Initializing discord rich presence... (RPC)")
    rpc = Presence("1005822803997638696")
    print(prefix("INIT") + "Presence ID set to: '1005822803997638696'.")
    print(prefix("INIT") + "Connecting to discord...")
    rpc.connect()
    print(prefix("INIT") + "Discord is connected...")
    update_status("Starting up...")
except:
    print(prefix("ERROR") + "Can't connect with the discord RPC.")
    time.sleep(0.25)

# Multithreading initialization

print(prefix("INIT") + "Initializing multithreading...")
print(prefix("INIT") + "Setting up ThreadPoolExecutor with " + str(threads) + " threads ...")
executor = concurrent.futures.ThreadPoolExecutor(threads, "Worker-")
for i in range(threads):
    print(prefix("INIT") + "Worker-" + str(i+1) + " is online!")

# FUEL initialization

print(prefix("INIT") + "Initializing FUELS...")
fuel_list = []
fuel_command_list = []
for file in os.listdir(fuel_content_dir):
    fuel_list.append(file)
    resolve_fuel_information(file)
print(prefix("INIT") + "Active FUELS: " + str(fuel_list).replace("[", "").replace("]", "").replace("'", ""))
print(prefix("INIT") + "FUELS initialized")

print(prefix("INIT") + "Initialization phase completed!")
update_status("Initialization phase completed!")

# INIT PHASE END

menu()
try:
    while True:
        print("")
        update_status("Idle")
        try:
            if threading.current_thread().name == "MainThread":
                current_thread_name = "FyUTILS"
            else:
                current_thread_name = threading.current_thread().name

            if os.getcwd() == current_dir:
                cwd_abbreviation = "#"
            elif os.getcwd() == "C:\\":
                cwd_abbreviation = "/"
            elif os.getcwd() == user_dir:
                cwd_abbreviation = "~"
            elif os.getcwd() == appdata_dir:
                cwd_abbreviation = "@"
            else:
                cwd_abbreviation = os.getcwd().replace("C:\\", "/").replace("\\", "/").replace(":", "").lower()
            request = input(accent_color + "╔═══[" + color + username + accent_color + "@" + text_color + device + accent_color + "]══(" + color + current_thread_name + accent_color + "/" + text_color + version + accent_color + ")══[" + text_color + cwd_abbreviation + accent_color + "]\n" +
                            accent_color + "╚═══> " + text_color).split(" ")
            cmd = request[0].lower()
            request.__delitem__(0)
            args = request
            print("")
        except KeyboardInterrupt:
            try:
                update_status("Shutting down...")
                print("\n" + prefix("INFO") + "Shutting down FyUTILS...")
                time.sleep(1)
                sys.exit(0)
            except KeyboardInterrupt:
                continue

        match cmd:
            case "flood":
                if len(args) != 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                target = args[0]
                port = int(args[1])
                activity_start = time.time()
                update_status("Flooding " + target + ":" + str(port))

                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.connect((target, port))
                    for i in range(sys.maxsize):
                        try:
                            sock.send(random.randbytes(10240))
                            print(prefix("INFO") + "Attacking target: " + color + target + accent_color + ":" + color + str(port) + text_color + "..." + accent_color + " - " + text_color + "Attack: " + color + str(i + 1) + accent_color, end='\r')
                        except socket.error:
                            print("")
                            print(prefix("ERROR") + "Request " + color + str(i) + text_color + " failed.", end='\r')
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")

            case "portscan":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                target = args[0]
                activity_start = time.time()
                update_status("Scanning on " + target)

                try:
                    print(prefix("INFO") + "Preparing scan.", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan..", end='\r')
                    time.sleep(0.1)
                    print(prefix("INFO") + "Preparing scan...", end='\r')
                    for port in range(1, 65535):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(0.05)
                        result = sock.connect_ex((target, port))
                        print(prefix("INFO") + "Scanning Port... " + color + str(port), end='\r')
                        if result == 0:
                            print(prefix("INFO") + "Port " + color + str(port) + text_color + " is open!                ")
                        sock.close()
                    print("\n")
                except KeyboardInterrupt:
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")

            case "arp":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                activity_start = time.time()
                target = args[0]
                update_status("ARP scanning in " + target + "...")

                try:
                    print(prefix("INFO") + "Make sure you have WinPcap or Npcap installed!")
                    print(prefix("INFO") + "Initialising ARP service...")
                    arp = scapy.ARP(pdst=target + "/24")
                    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
                    packet = ether/arp
                    print(prefix("INFO") + "Sending ARP packets...")
                    content = scapy.srp(packet, timeout=2, verbose=0)[0]
                    clients = []
                    print(prefix("INFO") + "Receiving data from " + target + "...")
                    for sent, received in content:
                        clients += [[received.psrc, received.hwsrc]]
                    print(prefix("INFO") + "Processing received data...")
                    print(prefix("INFO") + "Data received and processed.")
                    client_count = len(clients)
                    for i in range(client_count):
                        print(prefix("INFO") + accent_color + "[" + color + str(i) + accent_color + "] " + text_color + "IP: " +  clients[i][0] + " MAC: " + clients[i][1])
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")


            case "checkport":
                if len(args) != 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                target = args[0]
                port = int(args[1])
                activity_start = time.time()
                update_status("Checking" + target + ":" + str(port))

                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((target, port))
                    if result == 0:
                        print(prefix("INFO") + "Port " + color + str(port) + text_color + " is open!")
                    else:
                        print(prefix("ERROR") + "Port " + color + str(port) + text_color + " is not open!")
                    sock.close()
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")
                except Exception as e:
                    print(prefix("ERROR") + "An error occurred while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                try:
                    sock.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...")

            case "ssh":
                if len(args) != 3:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                server = args[0]
                port = int(args[1])
                user = args[2]
                activity_start = time.time()
                update_status("Starting FySSH service...")

                print(prefix("INFO") + "Connecting to " + server + ":" + str(port) + " as " + user)
                print(prefix("INFO") + "Creating SSH client...")
                ssh = paramiko.SSHClient()
                print(prefix("INFO") + "Loading host keys...")
                ssh.load_system_host_keys()
                print(prefix("INFO") + "Adding policy...")
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print(prefix("INFO") + "Requesting user's password...")
                password = pwinput.pwinput(text_color + "Enter password" + accent_color + " > " + text_color, "*")
                print(prefix("INFO") + "Connecting...")
                print("")
                try:
                    ssh.connect(server, port=port, username=user, password=password)
                    while True:
                        try:
                            update_ssh_status("Idle")
                            ssh_cmd = input(accent_color + "╔═══[" + Fore.LIGHTMAGENTA_EX + user + accent_color + "@" + Fore.LIGHTMAGENTA_EX + server + accent_color + ":" + Fore.LIGHTMAGENTA_EX + str(port) + accent_color + "]═══(" + color + "FySSH " + text_color + version + accent_color + ")" + "\n" + "╚═══" + accent_color + "> " + text_color)
                            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(ssh_cmd)
                            update_ssh_status("Running: " + ssh_cmd)
                            print("")
                            for line in ssh_stdout.readlines():
                                print(prefix("INFO") + line, end="\r")
                            for line in ssh_stderr.readlines():
                                print(prefix("ERROR") + line, end="\r")
                        except KeyboardInterrupt:
                            print("\n" + prefix("INFO") + "Canceling Action...")
                            break
                        except Exception as e:
                            print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                            print(prefix("ERROR") + str(e))
                            print("")
                except Exception as e:
                    print(prefix("ERROR") + "Can't connect to SSH host. Please make sure, that the requested port is open.")
                    print(prefix("ERROR") + "SSH error: " + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                    print(prefix("INFO") + "Cleaning up...\n")
                    continue

                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start : 0.2f}s")
                print(prefix("INFO") + "Disconnecting from " + color + server + accent_color + ":" + color + str(port) + text_color + "...")
                try:
                    ssh.close()
                except:
                    print(prefix("ERROR") + "Cannot disconnect from target!")
                print(prefix("INFO") + "Cleaning up...\n")

            case "fetch":
                if len(args) != 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                url = args[0]
                filename = args[1]
                activity_start = time.time()
                update_status("Fetching: " + url)

                try:
                    print(prefix("INFO") + "Fetching " + url + "...")
                    fetch_content = requests.get(url).content
                    print(prefix("INFO") + "Content of " + url + " cached!")
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                    print(prefix("INFO") + "Writing content of " + url + " from cache to local storage!")

                    try:
                        open(download_content_dir + "\\" + filename, mode="xb").write(fetch_content)
                        os.system("start explorer.exe " + download_content_dir)
                    except Exception as e:
                        print("\n" + prefix("ERROR") + "Could not save content to file.")
                        print(prefix("ERROR") + str(e))
                        print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                        print("")
                except KeyboardInterrupt:
                    print("")
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")

            case "youtube":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                url = args[0]
                activity_start = time.time()
                update_status("Downloading: " + url)

                try:
                    youtube = YouTube(url)
                    update_status("Downloading: " + youtube.title.title())
                    if not os.path.exists(download_content_dir):
                        os.makedirs(download_content_dir)
                        print(prefix("INFO") + "Media directory created!")
                    print(prefix("INFO") + "Download started!")
                    youtube.streams.filter(file_extension="mp4").order_by('resolution').desc().first().download(download_content_dir)
                    print(prefix("INFO") + f"Download finished in {time.time() - activity_start: 0.2f} seconds!")
                    os.system("start explorer.exe " + download_content_dir)
                except KeyboardInterrupt:
                    print("")
                    print("\n" + prefix("INFO") + "Canceling Action...")
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")
                    print("")

            case "fuels":
                print(prefix("FUEL") + "Active FUELS:")
                for file in fuel_list:
                    print(prefix("FUEL") + file)

            case "fuel":
                if len(args) != 2:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                fuel_action = args[0]
                fuel_location = args[1]
                activity_start = time.time()
                update_status("Installing FUEL " + fuel_location + "...")

                if fuel_action == "install":
                    print(prefix("FUEL") + "Installation process started!")
                    filename = fuel_location + ".json"
                    print(prefix("FUEL") + "Using \"" + fuel_location + "\" as target package.")
                    print(prefix("FUEL") + "Checking FUEL directory...")
                    if not os.path.exists(fuel_content_dir):
                        os.makedirs(fuel_content_dir)
                    if os.path.exists(fuel_content_dir + filename):
                        print(prefix("ERROR") + "Package \"" + fuel_location + "\" installation failed!")
                        print(prefix("ERROR") + "Error: Package is already installed.")
                        continue
                    print(prefix("FUEL") + "Installing to: " + fuel_content_dir + "...")
                    print(prefix("FUEL") + "Checking FUEL in NoahOnFyre/FUELS...")
                    fuel_repo_contents = requests.get("https://api.github.com/repos/NoahOnFyre/FUELS/contents/").json()
                    for i in range(len(fuel_repo_contents)):
                        fuel_download_url = ""
                        if fuel_repo_contents[i]["name"] == filename:
                            fuel_download_url = fuel_repo_contents[i]["download_url"]
                            break
                        else:
                            continue
                    if fuel_download_url == "":
                        print(prefix("ERROR") + "Package \"" + fuel_location + "\" installation failed!")
                        print(prefix("ERROR") + "Error: Package not found.")
                        continue
                    print(prefix("FUEL") + "Fetching FUEL from NoahOnFyre/FUELS...")
                    fuel_file_content = requests.get(fuel_download_url).content
                    print(prefix("FUEL") + "Writing content to file...")
                    local_fuel_file = open(fuel_content_dir + filename, mode="xb")
                    local_fuel_file.write(fuel_file_content)
                    local_fuel_file.close()
                    local_fuel_file = open(fuel_content_dir + filename, mode="rt")
                    print(prefix("FUEL") + "FUEL " + Fore.LIGHTMAGENTA_EX + fuel_location + text_color + " successfuly installed to \"" + fuel_content_dir + "\".")
                    print(prefix("FUEL") + "Adding FUEL to FyUTILS...")
                    local_fuel_file_json = json.load(local_fuel_file)
                    if local_fuel_file_json["properties"]["type"] == "DEFAULT":
                        fuel_command_list.append(local_fuel_file_json["properties"]["command_name"])
                    else:
                        print(prefix("FUEL") + Fore.RED + "WARNING: You're installing a mixin that can change the code of FyUTILS.")
                        print(prefix("FUEL") + Fore.RED + "Therefore you'll lose any warranty for this software.")
                        mixin_confirmation = input(prefix("FUEL") + "Do you want to continue installing? (y/n): ")
                        if mixin_confirmation.lower() == "n":
                            print(prefix("FUEL") + "Cancelling installation of " + Fore.LIGHTMAGENTA_EX + fuel_location + text_color + "...")
                            print(prefix("FUEL") + "Closing stashed files...")
                            local_fuel_file.close()
                            print(prefix("FUEL") + "Deleting temporary files...")
                            os.remove(fuel_content_dir + filename)
                            print(prefix("FUEL") + "Installation cancelled!")
                            print(prefix("FUEL") + f"Done! Took{time.time() - activity_start: 0.2f}s to cancel package installation of " + Fore.LIGHTMAGENTA_EX + fuel_location + text_color + "!")
                            continue

                    fuel_list.append(filename)
                    print(prefix("FUEL") + f"Done! Took{time.time() - activity_start: 0.2f}s to install package " + Fore.LIGHTMAGENTA_EX + fuel_location + text_color + "!")

                elif fuel_action == "remove":
                    filename = fuel_location + ".json"
                    print(prefix("FUEL") + "Unregistering " + fuel_content_dir + filename + "...")
                    if os.path.exists(fuel_content_dir + filename):
                        if json.load(open(fuel_content_dir + filename))["properties"]["type"] == "DEFAULT":
                            fuel_command_list.remove(json.load(open(fuel_content_dir + filename))["properties"]["command_name"])
                        fuel_list.remove(filename)
                    else:
                        print(prefix("ERROR") + "Package \"" + fuel_content_dir + filename + "\" remove failed!")
                        print(prefix("ERROR") + "Error: Local package not found.")
                        continue
                    print(prefix("FUEL") + "Deleting " + fuel_content_dir + filename + "...")
                    if os.path.exists(fuel_content_dir + filename):
                        os.remove(fuel_content_dir + filename)
                    else:
                        print(prefix("ERROR") + "Package \"" + fuel_content_dir + filename + "\" remove failed!")
                        print(prefix("ERROR") + "Error: Local package not found.")
                        continue
                    print(prefix("FUEL") + f"Done! Took{time.time() - activity_start: 0.2f}s to remove package " + Fore.LIGHTMAGENTA_EX + fuel_location)

                try:
                    None
                except KeyboardInterrupt:
                    print("")
                    print(accent_color + "╚" + "═" * 119)
                    print("\n" + prefix("INFO") + "Canceling Action...")
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

            case "update":
                update_status("Updating FyUTILS...")

                print(prefix("INFO") + "Update found! Updating to " + newest_version + "...")
                newest_file_content = requests.get(release_download_url).content
                open(current_dir + "\\main.py", mode="wb").write(newest_file_content)
                print(prefix("INFO") + "Update successfully installed!")
                time.sleep(1)
                print(prefix("INFO") + "Restarting FyUTILS...")
                os.system("start " + current_dir + "\\main.py")
                sys.exit(512)

            case "edit":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                filepath = args[0]
                activity_start = time.time()
                update_status("Editing " + filepath + "...")

                if not os.path.exists(filepath):
                    print(prefix("ERROR") + "File not found!")
                    confirmation = input(prefix("INFO") + "Do you want to let FyUTILS create a new file? (y/n): ")
                    if confirmation.lower() == "n":
                        continue
                    edit_file = open(filepath, "x+")
                    print(prefix("INFO") + "File created successfuly.")
                    print(prefix("INFO") + "End file editing by entering \"END\".")
                else:
                    edit_file = open(filepath, "w+")
                    print(prefix("INFO") + "File opened successfuly.")
                    print(prefix("INFO") + "End file editing by entering \"END\".")
                edit_string = ""
                for i in range(sys.maxsize):
                    try:
                        edit_line = input(str(i) + ": ")
                        if edit_line == "END":
                            break
                        edit_string = edit_string + edit_line + "\n"
                    except KeyboardInterrupt:
                        print("END")
                        print("")
                        break
                print(prefix("INFO") + "Writing cached content to " + filepath + "...")
                edit_file.writelines(edit_string)
                print(prefix("INFO") + "Saving file to " + filepath + "...")
                print(prefix("INFO") + "Closing " + filepath + "...")
                edit_file.close()
                print(prefix("INFO") + "File is saved and closed!")
                print(prefix("INFO") + f"Time elapsed: {time.time() - activity_start: 0.2f}s")

            case "calc":
                if len(args) != 1:
                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                    continue
                calculation = args[0]
                activity_start = time.time()
                update_status("Calculating " + calculation)

                print(prefix("INFO") + calculation + " is " + str(eval(calculation)))

            case "ls":
                try:
                    print(prefix("INFO") + "Content of " + os.getcwd())
                    for file in os.listdir(os.getcwd()):
                        if file.startswith("."):
                            if os.path.isfile(file):
                                print(prefix("INFO") + accent_color + file)
                            elif os.path.isdir(file):
                                print(prefix("INFO") + accent_color + "/" + file)
                        elif os.path.isfile(file):
                            print(prefix("INFO") + file)
                        elif os.path.isdir(file):
                            print(prefix("INFO") + Fore.GREEN + "/" + file)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

            case "exit":
                update_status("Shutting down...")
                print(prefix("INFO") + "Shutting down FyUTILS...")
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling action")
                    continue
                print("logout")
                sys.exit(0)

            case "quit":
                update_status("Shutting down...")
                print(prefix("INFO") + "Shutting down FyUTILS...")
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    print(prefix("INFO") + "Canceling action")
                    continue
                print("logout")
                sys.exit(0)

            case "cd":
                if len(args) != 1:
                    print(prefix("INFO") + os.getcwd().replace("C:\\", "/").replace("\\", "/").replace(":", "").lower())
                    continue
                change_dir = args[0]
                activity_start = time.time()
                update_status("Switching to " + change_dir + "...")

                match change_dir:
                    case "~":
                        change_dir = user_dir

                    case "#":
                        change_dir = current_dir

                    case "@":
                        change_dir = appdata_dir

                    case "/":
                        change_dir = "C:\\"

                    case _:
                        change_dir = change_dir

                try:
                    os.chdir(change_dir)
                    if os.getcwd() == current_dir:
                        cwd_abbreviation = "#"
                    elif os.getcwd() == "C:\\":
                        cwd_abbreviation = "/"
                    elif os.getcwd() == user_dir:
                        cwd_abbreviation = "~"
                    elif os.getcwd() == appdata_dir:
                        cwd_abbreviation = "@"
                    else:
                        cwd_abbreviation = os.getcwd().replace("C:\\", "/").replace("\\", "/").replace(":", "").lower()
                    print(prefix("INFO") + cwd_abbreviation)
                except Exception as e:
                    print("\n" + prefix("ERROR") + "An error occoured while trying to execute this command correctly.")
                    print(prefix("ERROR") + str(e))
                    print("")

            case "clear":
                update_status("Reloading...")
                os.system("cls")
                menu()

            case "rl":
                update_status("Reloading...")
                os.system("cls")
                menu()

            case "reload":
                update_status("Reloading...")
                os.system("cls")
                menu()

            case "restart":
                print("logout")
                os.system("start " + current_dir + "\\main.py")
                print("login")
                sys.exit(0)

            case "rs":
                print("logout")
                os.system("start " + current_dir + "\\main.py")
                print("login")
                sys.exit(0)

            case _:
                if fuel_command_list.__contains__(cmd):
                    for file in fuel_list:
                        json_fuel_file = json.load(open(fuel_content_dir + file, "r"))
                        if json_fuel_file["properties"]["command_name"] == cmd:
                            if json_fuel_file["head"]["enabled"]:
                                if len(args) != json_fuel_file["head"]["argument_length"]:
                                    print(prefix("ERROR") + "Unexpected arguments for command \"" + cmd + "\"")
                                    continue
                                for entry in range(len(json_fuel_file["head"]["arguments"])):
                                    exec(list(json_fuel_file["head"]["arguments"]).__getitem__(entry) + " = args[" + str(entry) + "]")
                                activity_start = time.time()
                                update_status(json_fuel_file["head"]["status"])

                            if json_fuel_file["body"]["enabled"]:
                                for line in list(json_fuel_file["body"]["content"]):
                                    exec(line)
                    continue

                arg_string = " "
                for entry in args:
                    arg_string = arg_string + entry + " "
                os.system(cmd + arg_string)
except Exception as e:
    os.system("title FyUTILS Crash Handler - Crash Log")
    print(prefix("ERROR") + "FyUTILS CRASH LOG @ " + datetime.datetime.now().strftime("%H:%M:%S"))
    print(prefix("ERROR") + "Error: " + str(e))
    os.system("pause")
    sys.exit(1024)
