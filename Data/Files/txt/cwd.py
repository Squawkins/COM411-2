import os


def cwd():
    path = os.getcwd()
    print(f"Current working directory: {path}")
    print(f"\n\nThe directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():
    print(f"Processing...\n\n\n")
    cwd()


run()
