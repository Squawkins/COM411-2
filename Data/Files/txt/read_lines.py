def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        data = file.readline()
        location = file.readlines()
        print(f"Looked in {location}")
    print("...Done")


def run():
    search('library.txt')


if __name__ == "__main__":
    run()
