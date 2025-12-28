
#!/data/data/com.termux/files/usr/bin/python3
"""
CYBERSAMEER TERMUX UI v3.0
Author: CyberSameer
Telegram Group: https://t.me/+PM5rI_RodBQ4NGZl
GitHub: https://github.com/wwssddsw285-alt/CyberSameer-Termux-Tools
"""

import os
import sys
import time
import getpass
from datetime import datetime
from pyfiglet import Figlet

# ==================== COLOR CODES ====================
R = "\033[1;31m"   # Red
G = "\033[1;32m"   # Green  
Y = "\033[1;33m"   # Yellow
B = "\033[1;34m"   # Blue
M = "\033[1;35m"   # Magenta
C = "\033[1;36m"   # Cyan
W = "\033[1;37m"   # White
RESET = "\033[0m"  # Reset

class TermuxUI:
    def __init__(self):
        self.user_name = ""
        self.cmd_count = 1
        self.login_time = ""
        
    def clear(self):
        os.system('clear')
    
    def typewriter(self, text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")
    
    def get_custom_prompt(self):
        time_str = self.get_time()
        prompt = f"""
{Y}┌─[{G}{self.user_name}{Y}]─[{R}@{time_str}{Y}]
└─[{M}${Y}]{RESET} """
        return prompt
    
    def login(self):
        self.clear()
        
        # Login header
        print(f"\n{R}╔{'═'*60}╗{RESET}")
        print(f"{R}║{RESET}{Y}             CYBERSAMEER TERMUX UI v3.0             {RESET}{R}║{RESET}")
        print(f"{R}╚{'═'*60}╝{RESET}")
        
        # Login banner
        try:
            f = Figlet(font='slant')
            login_banner = f.renderText("LOGIN PORTAL")
            print(f"{C}{login_banner}{RESET}")
        except:
            print(f"\n{Y}══════ LOGIN PORTAL ══════{RESET}\n")
        
        self.typewriter(f"{C}[*] Initializing security protocols...{RESET}")
        time.sleep(1)
        
        username = input(f"\n{G}[?] Enter your name: {RESET}")
        password = getpass.getpass(f"{G}[?] Enter password: {RESET}")
        
        self.user_name = username
        self.login_time = self.get_time()
        
        print(f"\n{G}[+] Welcome {username}! Creating your banner...{RESET}")
        time.sleep(1)
        
        self.create_welcome_banner(username)
        time.sleep(2)
        
        return True
    
    def create_welcome_banner(self, username):
        self.clear()
        
        side_panel = f"""
{R}╔══════════════════════════════════════════════════════════════════╗
║{M}  ░█████╗░██╗░░░██╗██████╗░███████╗██████╗░{R}                      ║
║{M}  ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗{R}                      ║
║{M}  ██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝{R}                      ║
║{M}  ██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗{R}                      ║
║{M}  ╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║{R}                      ║
║{M}  ░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝{R}                      ║
║{C}         Developer: {Y}CyberSameer{R}                            ║
║{C}         User: {Y}{username}{R}                                     ║
║{C}         Telegram: {Y}@CyberSameer{R}                              ║
║{C}         Group: {Y}t.me/+PM5rI_RodBQ4NGZl{R}                       ║
║{C}         GitHub: {Y}github.com/wwssddsw285-alt{R}                  ║
║{G}         Status: {Y}CONNECTED{R}                                   ║
╠══════════════════════════════════════════════════════════════════╣{RESET}"""
        
        print(side_panel)
        
        # User name banner
        try:
            f = Figlet(font='slant')
            banner_text = f.renderText(username)
            print(f"\n{G}{banner_text}{RESET}")
        except:
            print(f"\n{Y}══════ Welcome {username} ══════{RESET}")
        
        # Special message
        print(f"\n{M}╔{'═'*60}╗{RESET}")
        print(f"{M}║{C}     WELCOME TO CYBERSAMEER'S HACKING TERMINAL      {M}║{RESET}")
        print(f"{M}║{C}     Telegram Group: https://t.me/+PM5rI_RodBQ4NGZl {M}║{RESET}")
        print(f"{M}║{C}     GitHub: https://github.com/wwssddsw285-alt     {M}║{RESET}")
        print(f"{M}╚{'═'*60}╝{RESET}")
        
        input(f"\n{Y}[Press Enter to continue...]{RESET}")
    
    def create_banner(self):
        self.clear()
        
        side_panel = f"""
{R}╔══════════════════════════════════════════════════════════╗
║{C}         User: {Y}{self.user_name}{R}                               ║
║{C}         Session: {Y}{self.login_time}{R}                           ║
║{C}         Telegram: {Y}t.me/+PM5rI_RodBQ4NGZl{R}                     ║
║{C}         GitHub: {Y}github.com/wwssddsw285-alt{R}                   ║
║{G}         Status: {Y}ACTIVE{R}                                      ║
╠══════════════════════════════════════════════════════════╣{RESET}"""
        
        print(side_panel)
        
        try:
            f = Figlet(font='slant')
            banner_text = f.renderText(self.user_name)
            print(f"{G}{banner_text}{RESET}")
        except:
            print(f"\n{Y}══════ {self.user_name} ══════{RESET}\n")
    
    def show_menu(self):
        menu = f"""{R}║{B}  COMMANDS:{R}                                          ║
║{C}  help           - Show this menu{R}                       ║
║{C}  clear          - Clear screen{R}                         ║
║{C}  banner         - Show banner{R}                          ║
║{C}  scan           - Network scanner{R}                      ║
║{C}  vuln           - Vulnerability check{R}                  ║
║{C}  sysinfo        - System information{R}                   ║
║{C}  encrypt        - Encrypt text{R}                         ║
║{C}  decrypt        - Decrypt text{R}                         ║
║{C}  update         - Update tools{R}                         ║
║{C}  history        - Show command history{R}                 ║
║{C}  group          - Show Telegram group{R}                  ║
║{C}  github         - Show GitHub repository{R}               ║
║{C}  exit           - Exit program{R}                         ║
{R}╚══════════════════════════════════════════════════════════╝{RESET}"""
        print(menu)
    
    def execute_command(self, cmd):
        self.cmd_count += 1
        
        if cmd == "help":
            self.show_menu()
        elif cmd == "clear":
            self.create_banner()
        elif cmd == "banner":
            self.create_banner()
        elif cmd == "scan":
            self.fake_scan()
        elif cmd == "vuln":
            self.vulnerability_check()
        elif cmd == "sysinfo":
            self.system_info()
        elif cmd == "encrypt":
            self.encrypt_text()
        elif cmd == "decrypt":
            self.decrypt_text()
        elif cmd == "update":
            self.update_tools()
        elif cmd == "history":
            print(f"{C}[*] Command history: {self.cmd_count-1} commands executed{RESET}")
        elif cmd == "group":
            self.show_telegram_group()
        elif cmd == "github":
            self.show_github()
        elif cmd == "exit":
            print(f"\n{R}Logging out...{RESET}")
            time.sleep(1)
            sys.exit()
        elif cmd:
            print(f"{C}[*] Executing: {cmd}{RESET}")
            os.system(cmd)
    
    def show_telegram_group(self):
        print(f"\n{G}╔{'═'*50}╗{RESET}")
        print(f"{G}║{Y}     CYBERSAMEER TELEGRAM GROUP     {G}║{RESET}")
        print(f"{G}║{C}     Link: https://t.me/+PM5rI_RodBQ4NGZl {G}║{RESET}")
        print(f"{G}║{C}     Join for hacking tutorials!    {G}║{RESET}")
        print(f"{G}╚{'═'*50}╝{RESET}")
    
    def show_github(self):
        print(f"\n{B}╔{'═'*50}╗{RESET}")
        print(f"{B}║{Y}     CYBERSAMEER GITHUB REPOSITORY     {B}║{RESET}")
        print(f"{B}║{C}     https://github.com/wwssddsw285-alt {B}║{RESET}")
        print(f"{B}║{C}     /CyberSameer-Termux-Tools         {B}║{RESET}")
        print(f"{B}╚{'═'*50}╝{RESET}")
    
    def fake_scan(self):
        print(f"\n{C}[*] Starting network scan...{RESET}\n")
        targets = ["192.168.1.1", "192.168.1.100", "10.0.0.1"]
        
        for target in targets:
            print(f"{self.get_custom_prompt()}{C}scan {target}{RESET}")
            print(f"{G}[+] {target}: Port 22 (SSH) - OPEN{RESET}")
            print(f"{G}[+] {target}: Port 80 (HTTP) - OPEN{RESET}")
            print(f"{Y}[!] {target}: Vulnerable to CVE-2021-34527{RESET}")
            time.sleep(0.5)
        
        print(f"\n{G}[+] Scan complete. 3 hosts discovered.{RESET}")
    
    def vulnerability_check(self):
        print(f"\n{C}[*] Running vulnerability assessment...{RESET}")
        time.sleep(1)
        print(f"{Y}[!] 3 critical vulnerabilities found{RESET}")
        print(f"{Y}[!] 7 high vulnerabilities found{RESET}")
        print(f"{G}[+] 12 vulnerabilities patched{RESET}")
    
    def system_info(self):
        print(f"\n{C}[*] Gathering system information...{RESET}")
        time.sleep(0.5)
        print(f"{G}[+] User: {self.user_name}{RESET}")
        print(f"{G}[+] Time: {self.get_time()}{RESET}")
        print(f"{G}[+] Commands executed: {self.cmd_count-1}{RESET}")
        print(f"{G}[+] Session started: {self.login_time}{RESET}")
        print(f"{G}[+] Telegram Group: t.me/+PM5rI_RodBQ4NGZl{RESET}")
        print(f"{G}[+] GitHub: github.com/wwssddsw285-alt{RESET}")
        print(f"{G}[+] Developer: CyberSameer{RESET}")
    
    def encrypt_text(self):
        text = input(f"{self.get_custom_prompt()}{G}Enter text to encrypt: {RESET}")
        encrypted = text[::-1]
        print(f"{C}[+] Encrypted: {Y}{encrypted}{RESET}")
    
    def decrypt_text(self):
        text = input(f"{self.get_custom_prompt()}{G}Enter text to decrypt: {RESET}")
        decrypted = text[::-1]
        print(f"{C}[+] Decrypted: {Y}{decrypted}{RESET}")
    
    def update_tools(self):
        print(f"\n{C}[*] Updating all tools...{RESET}")
        time.sleep(1)
        print(f"{G}[+] apt update completed{RESET}")
        print(f"{G}[+] pip upgrade completed{RESET}")
        print(f"{G}[+] All packages are up to date{RESET}")
    
    def run(self):
        if not self.login():
            sys.exit()
        
        self.create_banner()
        self.show_menu()
        
        while True:
            try:
                cmd = input(f"{self.get_custom_prompt()}")
                self.execute_command(cmd.strip())
            except KeyboardInterrupt:
                print(f"\n{R}[!] Use 'exit' command to logout{RESET}")
            except EOFError:
                print(f"\n{R}Exiting...{RESET}")
                sys.exit()

if __name__ == "__main__":
    try:
        app = TermuxUI()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{R}Program terminated{RESET}")
        sys.exit()
