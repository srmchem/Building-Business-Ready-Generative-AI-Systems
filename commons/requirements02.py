import subprocess
import sys

def run_command(command):
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(command)}\nError: {e}")
        sys.exit(1)

# Uninstall the 'pinecone-client' package
print("Uninstalling 'pinecone-client'...")
run_command([sys.executable, "-m", "pip", "uninstall", "-y", "pinecone-client"])

# Install the specific version of 'pinecone-client'
print("Installing 'pinecone-client' version 5.0.1...")
run_command([sys.executable, "-m", "pip", "install", "--force-reinstall", "pinecone-client==5.0.1"])

# Verify the installation
try:
    import pinecone
    print(f"'pinecone-client' version {pinecone.__version__} is installed.")
except ImportError:
    print("Failed to import the 'pinecone-client' library after installation.")
    sys.exit(1)