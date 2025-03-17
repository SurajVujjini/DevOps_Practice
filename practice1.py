def generate_ankit_file():
    """
    Generates a text file named "ankit.txt" and adds "fuckk off" and "fuck off in it" to it if it already exists.
    """
    try:
        with open("ankit.txt", "a") as f:
            f.write("fuckk off\n")
            f.write("fuck off in it\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_ankit_file()