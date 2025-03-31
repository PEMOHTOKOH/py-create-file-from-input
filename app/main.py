def main():
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.writelines(f"{line}\n")

if __name__ == "__main__":
    main()
