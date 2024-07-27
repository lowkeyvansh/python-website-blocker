import os
import sys

# Path to the hosts file
hosts_path = "/etc/hosts"  # For Linux and macOS
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # For Windows

# IP address to redirect blocked sites to
redirect_ip = "127.0.0.1"

def block_websites(websites):
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in websites:
            if website not in content:
                file.write(f"{redirect_ip} {website}\n")
                print(f"Blocked {website}")
            else:
                print(f"{website} is already blocked")

def unblock_websites(websites):
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        file.truncate()
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
        print(f"Unblocked {', '.join(websites)}")

if __name__ == "__main__":
    action = input("Enter 'block' to block websites or 'unblock' to unblock websites: ").strip().lower()
    websites = input("Enter the websites to block/unblock, separated by commas: ").strip().split(',')

    if action == 'block':
        block_websites([website.strip() for website in websites])
    elif action == 'unblock':
        unblock_websites([website.strip() for website in websites])
    else:
        print("Invalid action. Please enter 'block' or 'unblock'.")
