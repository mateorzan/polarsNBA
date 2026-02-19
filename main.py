import subprocess
import sys
import os


def setup_kernel():
    kernel_name = "polarsnba"
    kernel_path = os.path.expanduser(f"~/.local/share/jupyter/kernels/{kernel_name}")

    if not os.path.exists(kernel_path):
        print(f"Installing Jupyter kernel '{kernel_name}'...")
        subprocess.run([
            sys.executable, "-m", "ipykernel", "install",
            "--user", "--name", kernel_name,
            "--display-name", "Python (polarsnba)"
        ])
        print("Kernel installed!")
    else:
        print("Kernel already exists.")


def main():
    setup_kernel()
    print("Hello from polarsnba!")


if __name__ == "__main__":
    main()
