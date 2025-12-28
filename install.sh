#!/data/data/com.termux/files/usr/bin/bash
# CyberSameer Termux Tools - Installation Script

echo -e "\033[1;36m"
echo "╔══════════════════════════════════════════════════╗"
echo "║     CYBERSAMEER TERMUX TOOLS INSTALLATION        ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "\033[0m"

echo -e "\033[1;33m[*] Updating packages...\033[0m"
pkg update -y
pkg upgrade -y

echo -e "\033[1;33m[*] Installing Python and pip...\033[0m"
pkg install -y python python-pip

echo -e "\033[1;33m[*] Installing pyfiglet...\033[0m"
pip install pyfiglet

echo -e "\033[1;33m[*] Making scripts executable...\033[0m"
chmod +x cyberui.py install.sh update.sh

echo -e "\033[1;32m"
echo "╔══════════════════════════════════════════════════╗"
echo "║           ✅ INSTALLATION COMPLETE!              ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "\033[0m"

echo -e "\033[1;36m[*] To run CyberSameer Termux Tools:\033[0m"
echo -e "\033[1;32m    python cyberui.py\033[0m"
echo ""
echo -e "\033[1;36m[*] Default login credentials:\033[0m"
echo -e "\033[1;33m    Username: CyberSameer\033[0m"
echo -e "\033[1;33m    Password: hack123\033[0m"
echo ""
echo -e "\033[1;35m[*] Join Telegram: https://t.me/+PM5rI_RodBQ4NGZl\033[0m"
