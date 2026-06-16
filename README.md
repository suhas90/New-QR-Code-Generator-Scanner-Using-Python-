### Advanced QR Code Customizer & Scanner

An advanced command-line tool built in Python to generate highly customized QR codes (with custom colors and rounded shapes) and scan existing QR codes from image files.


### Features
- **Shape Control**: Choose between standard square blocks or modern rounded/circle modules.
- **Color Customization**: Define custom hex codes or standard color names for both the background and foreground.
- **Robust Scanner**: Decode QR patterns instantly from local files.
- **Modular Codebase**: Organized into clear logical modules (`src/`) for scalable development.

### Installation
1. Clone this repository.
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the main program:
```bash
python main.py
```
Project File Structure 

qr-customizer/
├── src/
│   ├── __init__.py
│   ├── generator.py
│   └── scanner.py
├── requirements.txt
├── README.md
└── main.py

Important Note :

IF You Try to Run Code ON Ubuntu 24.XX VM and you got an following error while installing requirements.txt  

pip install -r requirements.txt

error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification. 
 
to fix this error pls perform the following steps:

This is expected behavior on Ubuntu 24.04 (and newer Debian/Ubuntu releases). Ubuntu implements PEP 668, which prevents pip from installing packages into the system Python environment to avoid breaking OS-managed packages.
Recommended Solution: Use a Virtual Environment

From your project directory:

cd ~/qr-code/New-QR-Code-Generator-Scanner-Using-Python-

# Install venv support if needed
sudo apt update
sudo apt install python3-venv -y

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

You should then see your shell prompt change to something like:

(venv) suhas@suhas-vm:~/qr-code/New-QR-Code-Generator-Scanner-Using-Python-$

Run the application while the virtual environment is activated: python main.py

if got the following error after final step 


python3 main.py

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.4.6 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/main.py", line 2, in <module>
    from src.scanner import scan_qr_file
  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/src/scanner.py", line 2, in <module>
    import cv2
  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/venv/lib/python3.12/site-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/venv/lib/python3.12/site-packages/cv2/__init__.py", line 153, in bootstrap
    native_module = importlib.import_module("cv2")
  File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
AttributeError: _ARRAY_API not found
Traceback (most recent call last):
  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/main.py", line 2, in <module>
    from src.scanner import scan_qr_file
  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/src/scanner.py", line 2, in <module>
    import cv2
  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/venv/lib/python3.12/site-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
  File "/home/suhas/qr-code/New-QR-Code-Generator-Scanner-Using-Python-/venv/lib/python3.12/site-packages/cv2/__init__.py", line 153, in bootstrap
    native_module = importlib.import_module("cv2")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ImportError: numpy.core.multiarray failed to import

***********************************************************

Now to fix this 
do the following 



your setup is now correctly isolated in a venv. The remaining problem is purely a version mismatch between NumPy and OpenCV.
❌ Root Cause

You installed:

    numpy 2.4.6 (very new)

    opencv-python 4.9.0.80 (compiled against NumPy 1.x)

So OpenCV fails with:

    AttributeError: _ARRAY_API not found

    ImportError: numpy.core.multiarray failed to import

This is a known NumPy 2.x compatibility break.
✅ Fix (Recommended): Downgrade NumPy

Inside your virtual environment:

pip uninstall -y numpy
pip install "numpy<2"

Then reinstall OpenCV cleanly:

pip uninstall -y opencv-python
pip install opencv-python==4.9.0.80

Now run:

python main.py

👍 Why this works

    opencv-python 4.9 was built for NumPy 1.x ABI

    NumPy 2.x introduced breaking changes (_ARRAY_API)

    Most Python ML/OpenCV stacks still expect numpy<2

🧠 Best Stable Combo (for your project)

Use this:

numpy<2
opencv-python==4.9.0.80
pillow==10.2.0
qrcode==7.4.2

🚀 If you want a clean reset (optional but best practice)

If things get messy:

deactivate
rm -rf venv

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install "numpy<2"
pip install -r requirements.txt

(But edit requirements.txt first to force numpy<2)
⚡ Quick Summary

Your issue is NOT Ubuntu or VMware.

It is:

    ❌ NumPy 2.x + OpenCV 4.9 incompatibility
    ✅ Fix = downgrade NumPy to <2


