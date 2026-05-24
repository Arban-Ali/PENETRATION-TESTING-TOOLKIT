import sys
# Import the custom scanner module we just created
from modules import port_scanner

def main():
    print("====================================")
    print("    MODULAR PENETRATION TOOLKIT     ")
    print("====================================")
    
    target = input("Enter target IP (Use 127.0.0.1 for testing): ").strip()
    if not target:
        print("[-] Target cannot be empty. Exiting.")
        sys.exit()

    while True:
        print("\nAvailable Modules:")
        print("1. Port Scanner")
        print("2. Exit")
        
        choice = input("\nSelect an option (1-2): ").strip()
        
        if choice == "1":
            port_scanner.run(target)
        elif choice == "2":
            print("[+] Exiting toolkit. Stay safe!")
            break
        else:
            print("[-] Invalid selection. Try again.")

if __name__ == "__main__":
    main()
