def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        data = file.read()
        for line in data:
            location = line.readfile()
            print(f"Looked in {location}")
        print("\n\n...Done!")


def run():
    search('library.txt')


if __name__ == "__main__":
    run()
