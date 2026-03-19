#!/bin/bash

echo -e "\e[94m[*] Installing LogicHunter Dependencies...\e[0m"

# Update and install basic tools
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip golang jq curl wget

# Install Go tools (ProjectDiscovery & FFUF)
echo -e "\e[93m[*] Installing Go-based Security Tools...\e[0m"
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/ffuf/ffuf/v2@latest
go install -v github.com/s0md3v/Arjun@latest

# Move Go binaries to /usr/local/bin so they can be run from anywhere
echo -e "\e[93m[*] Moving binaries to /usr/local/bin...\e[0m"
sudo cp ~/go/bin/subfinder /usr/local/bin/
sudo cp ~/go/bin/httpx /usr/local/bin/
sudo cp ~/go/bin/nuclei /usr/local/bin/
sudo cp ~/go/bin/katana /usr/local/bin/
sudo cp ~/go/bin/ffuf /usr/local/bin/
sudo cp ~/go/bin/Arjun /usr/local/bin/

# Update nuclei templates
echo -e "\e[93m[*] Updating Nuclei Templates...\e[0m"
nuclei -update-templates

echo -e "\e[92m[+] Installation Complete! Run 'pip install -r requirements.txt' then 'python3 logichunter.py' \e[0m"
