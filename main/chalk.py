def run(file_name):
    file = open(f"{file_name}", "r")
    for line in file:
        line.rstrip()
        word = line.split(' ', 1)
        print(word)