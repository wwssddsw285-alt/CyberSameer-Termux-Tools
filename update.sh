#!/data/data/com.termux/files/usr/bin/bash
# CyberSameer Termux Tools - Update Script

echo -e "\033[1;36m"
echo "╔══════════════════════════════════════════════════╗"
echo "║        CYBERSAMEER TERMUX TOOLS UPDATE           ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "\033[0m"

echo -e "\033[1;33m[*] Updating from GitHub...\033[0m"
git pull origin main

echo -e "\033[1;33m[*] Updating Python packages...\033[0m"
pip install --upgrade pyfiglet

echo -e "\033[1;33m[*] Making scripts executable...\033[0m"
chmod +x cyberui.py install.sh update.sh

echo -e "\033[1;32m"
echo "╔══════════════════════════════════════════════════╗"
echo "║              ✅ UPDATE COMPLETE!                 ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "\033[0m"

echo -e "\033[1;36m[*] Tool updated to latest version!\033[0m"
echo -e "\033[1;32m[*] Run: python cyberui.py\033[0m"
