import os #line:1
import re #line:2
import platform #line:3
import subprocess #line:4
import time #line:5
from colorama import Fore ,Style #line:6
import shutil #line:7
def clear_terminal ():#line:9
    os .system ('cls'if os .name =='nt'else 'clear')#line:10
def print_centered_colored_text (OO0O00O0O00O0OO0O ,O0OOOOOO00O000OOO ):#line:12
    OO00OOOOOO0OOOO00 ,O00OO0OOOO0OOOOOO =shutil .get_terminal_size ()#line:13
    O0OOOO0OO0O0OOOO0 =OO0O00O0O00O0OO0O .split ('\n')#line:15
    O0O00O0O0O0OOOOOO =max (len (OO0O00OO00OO0O000 )for OO0O00OO00OO0O000 in O0OOOO0OO0O0OOOO0 )#line:16
    for O00OOO000OO0O0O00 in O0OOOO0OO0O0OOOO0 :#line:18
        OO0000O000OOO0O0O =max ((OO00OOOOOO0OOOO00 -O0O00O0O0O0OOOOOO )//2 ,0 )#line:19
        print (O0OOOOOO00O000OOO +' '*OO0000O000OOO0O0O +O00OOO000OO0O0O00 +Style .RESET_ALL )#line:20
def print_horizontal_line (OOOO0000000OOOOO0 ,O00OOOOO00O000000 ):#line:22
    print (OOOO0000000OOOOO0 +'-'*O00OOOOO00O000000 +Style .RESET_ALL )#line:23
def validate_host (O0OO0OO0O00O00O00 ):#line:25
    O000OOO00OOOOOOOO =re .compile (r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")#line:26
    OO0OO0OO00O00OOO0 =re .compile (r"^(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$")#line:27
    return O000OOO00OOOOOOOO .match (O0OO0OO0O00O00O00 )or OO0OO0OO00O00OOO0 .match (O0OO0OO0O00O00O00 )#line:29
def validate_port (O0OO0000O0O00OOO0 ):#line:31
    OO0OO0O0OO00OO00O =re .compile (r"^\d{1,5}$")#line:32
    return OO0OO0O0OO00OO00O .match (O0OO0000O0O00OOO0 )#line:33
def validate_amount (OO00OO000O000O00O ):#line:35
    OOO00O00O0OOOO0O0 =re .compile (r"^\d+$")#line:36
    return OOO00O00O0OOOO0O0 .match (OO00OO000O000O00O )#line:37
def ping_host (O00OO0O0OO0OOOO00 ,O0OO0OO0O000OOO0O ):#line:39
    OOO00OO0O0000O00O =f"ping -n {O0OO0OO0O000OOO0O} {O00OO0O0OO0OOOO00}"#line:40
    try :#line:42
        print ("[+] Starting ping...")#line:43
        O0OOOOOOO0O00O00O =subprocess .run (OOO00OO0O0000O00O ,shell =True ,stdout =subprocess .PIPE ,text =True ,check =True )#line:45
        for OOO000OOO000OO0O0 in O0OOOOOOO0O00O00O .stdout .split ('\n'):#line:47
            if "Packets: Sent"in OOO000OOO000OO0O0 or OOO000OOO000OO0O0 .startswith ("Reply from"):#line:48
                print (OOO000OOO000OO0O0 )#line:49
                time .sleep (0.1 )#line:50
        OO000O00OO0OO0O00 =re .search (r"Ping statistics for .+:\s+Packets: Sent = (\d+), Received = (\d+), Lost = (\d+) \((\d+)% loss\),\s+Approximate round trip times in milli-seconds:\s+Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms",O0OOOOOOO0O00O00O .stdout )#line:52
        if OO000O00OO0OO0O00 :#line:54
            O0OOO0OO0OO00OO00 ,OOOOO00O0OO00OO0O ,O0O00OO0OOOO0OOOO ,O00O0OOO0O00OOO00 ,O0OO0000OOOOOO0OO ,O0OOO0OOO0O000000 ,OOO0OOOO0OOO00O00 =OO000O00OO0OO0O00 .groups ()#line:55
            print (f"\nPing statistics for {O00OO0O0OO0OOOO00}:\n    Packets: Sent = {O0OOO0OO0OO00OO00}, Received = {OOOOO00O0OO00OO0O}, Lost = {O0O00OO0OOOO0OOOO} ({O00O0OOO0O00OOO00}% loss),\nApproximate round trip times in milli-seconds:\n    Minimum = {O0OO0000OOOOOO0OO}ms, Maximum = {O0OOO0OOO0O000000}ms, Average = {OOO0OOOO0OOO00O00}ms")#line:56
    except subprocess .CalledProcessError as OO0OOOO0O0O00000O :#line:58
        print (f"Error: {OO0OOOO0O0O00000O}")#line:59
correct_username ="admin"#line:62
correct_key ="gHz1lW9kNp3sR5jY2mX8oA7dH6tL4eU0iF1cV2bJ3nM4qZ5xK6vP7yO8uI9"#line:63
username =input ("Enter Username: ")#line:66
key =input ("Enter Key: ")#line:67
if username ==correct_username and key ==correct_key :#line:69
    clear_terminal ()#line:70
    text ="""
    ▄█▀▀▀█▄█     ██      ▄█▀▀▀█▄███▀▀██▀▀███████▀███▄   ▀███▀ ▄▄█▀▀▀█▄█    ▀████▀   ▀███▀       
    ▄██    ▀█    ▄██▄    ▄██    ▀█▀   ██   ▀█ ██   ███▄    █ ▄██▀     ▀█      ▀██     ▄█         
    ▀███▄       ▄█▀██▄   ▀███▄        ██      ██   █ ███   █ ██▀       ▀       ██▄   ▄█   ███▀██▄
      ▀█████▄  ▄█  ▀██     ▀█████▄    ██      ██   █  ▀██▄ █ ██                 ██▄  █▀  ███   ██
    ▄     ▀██  ████████  ▄     ▀██    ██      ██   █   ▀██▄█ ██▄    ▀████       ▀██ █▀       ▄▄██
    ██     ██ █▀      ██ ██     ██    ██      ██   █     ███ ▀██▄     ██         ▄██▄     ▄▄█▀   
    ▀▀█████▀▄███▄   ▄████▄▀█████▀   ▄████▄  ▄████▄███▄    ██   ▀▀███████          ██     ████████

                             Time Remaining: inf   Logged as: admin 
    """#line:82
    additional_text ="""
    [$] Made by Bluer on doxbin
    [$] Version: 2.0.1
    [$] Special thanks to PsyFlood for design ideas
    [$] Type `cmd` If You dont know commands [+]
    """#line:89
    help_text ="""
    Help:

    >>>> /host - Enter the Host Domain or Ip Address
    >>>> /port - Enter a custom port if you have one, or just don't use it will use port 80
    >>>> /amount - Enter a custom amount of attack, Default 1000
    >>>> /start - Will start attacking and display outputs on the console
    """#line:98
    user_host =None #line:100
    user_amount ="1000"#line:101
    clear_terminal ()#line:103
    print_centered_colored_text (text ,Fore .RED )#line:105
    print_horizontal_line (Fore .WHITE ,shutil .get_terminal_size ().columns )#line:106
    print_horizontal_line (Fore .WHITE ,shutil .get_terminal_size ().columns )#line:107
    print_centered_colored_text (additional_text ,Fore .YELLOW )#line:108
    print_horizontal_line (Fore .WHITE ,shutil .get_terminal_size ().columns )#line:109
    while True :#line:111
        user_input =input (Fore .BLUE +"admin >> "+Style .RESET_ALL )#line:112
        if user_input .lower ()=="/cmd":#line:114
            print (help_text )#line:115
        elif user_input .lower ().startswith ("/host "):#line:116
            host_input =user_input [6 :]#line:117
            if validate_host (host_input ):#line:119
                user_host =host_input #line:120
                print (f"[+] Target saved: {user_host}")#line:121
            else :#line:122
                print (f"[-] Invalid host: {host_input}")#line:123
        elif user_input .lower ().startswith ("/port "):#line:124
            port_input =user_input [6 :]#line:125
            if validate_port (port_input ):#line:127
                print (f"[+] Port saved: {port_input}")#line:128
            else :#line:129
                print (f"[-] Invalid port: {port_input}")#line:130
        elif user_input .lower ().startswith ("/amount "):#line:131
            amount_input =user_input [8 :]#line:132
            if validate_amount (amount_input ):#line:134
                user_amount =amount_input #line:135
                print (f"[+] Amount saved: {user_amount}")#line:136
            else :#line:137
                print (f"[-] Invalid amount: {amount_input}")#line:138
        elif user_input .lower ()=="/start":#line:139
            if user_host :#line:140
                ping_host (user_host ,user_amount )#line:141
            else :#line:142
                print (Fore .BLUE +"[+] Please enter target host, port, and amount before starting."+Style .RESET_ALL )#line:143
        else :#line:144
            print ("[-] Invalid command")#line:145
else :#line:147
    print ("\033[91mInvalid name or key\033[0m")#line:148
