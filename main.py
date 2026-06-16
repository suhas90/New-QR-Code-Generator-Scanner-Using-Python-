from src.generator import generate_custom_qr
from src.scanner import scan_qr_file

def main():
    while True:
        print("\n=================================")
        print("   CUSTOM QR ENGINE & SCANNER")
        print("=================================")
        print("1. Generate Custom Shaped/Colored QR")
        print("2. Scan QR from File")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            generate_custom_qr()
        elif choice == "2":
            scan_qr_file()
        elif choice == "3":
            print("System closed. Happy committing!")
            break
        else:
            print("Invalid system option. Please try again.")

if __name__ == "__main__":
    main()
