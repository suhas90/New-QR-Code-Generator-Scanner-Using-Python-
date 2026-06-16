import os
import cv2

def scan_qr_file():
    print("\n--- QR Code Scanner ---")
    path = input("Enter the path to the QR code image file: ")
    
    if not os.path.exists(path):
        print("[Error] File pathway not found.")
        return

    img = cv2.imread(path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if data:
        print(f"\n[Decoded Successfully]:\n--> {data}")
    else:
        print("\n[Failure] Unable to decode a valid QR pattern. Colors might lack contrast.")
