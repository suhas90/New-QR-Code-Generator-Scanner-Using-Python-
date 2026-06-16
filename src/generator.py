import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer

def generate_custom_qr():
    print("\n--- QR Code Configuration ---")
    data = input("Enter the text or URL to encode: ")
    
    print("\nSelect Module Shape:")
    print("1. Standard Square")
    print("2. Smooth Rounded")
    print("3. Circles")
    shape_choice = input("Choice (1-3): ")
    
    # Select shape drawer
    if shape_choice == "2":
        drawer = RoundedModuleDrawer()
    elif shape_choice == "3":
        drawer = CircleModuleDrawer()
    else:
        drawer = SquareModuleDrawer()

    fill_color = input("\nEnter foreground color (e.g., 'black', 'navy', 'darkgreen'): ") or "black"
    back_color = input("Enter background color (e.g., 'white', 'yellow', 'lightgray'): ") or "white"
    filename = input("Enter output filename (default: custom_qr.png): ") or "custom_qr.png"
    
    if not filename.endswith(".png"):
        filename += ".png"

    # Configure structural parameters of the QR architecture
    qr = qrcode.QRCode(
        version=3,  # Higher version accommodates complex styles better
        error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction for custom shapes
        box_size=12,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Factory rendering with customized modules and color formatting
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        fill_color=fill_color,
        back_color=back_color
    )
    
    img.save(filename)
    print(f"\n[Success] Customized QR code exported as: {filename}")
