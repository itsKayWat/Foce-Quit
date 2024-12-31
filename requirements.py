import subprocess
import sys

def install_requirements():
    print("Installing required packages...")
    requirements = ['psutil']
    
    for package in requirements:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    print("\nAll requirements installed successfully!")

if __name__ == "__main__":
    install_requirements()