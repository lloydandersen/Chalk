import re
import toml as tml
working_list = []
working_string = ""
end_list = []

def lesson_objects():
    x = re.split("L\\[", working_string)
    x.pop(0)
    file_handle = open("speciall.on", "w")
    for i in x:
        file_handle.write(i)


def run(file_name):
    global working_string
    with open(f"{file_name}", "r") as file:
        for line in file:
            stripped_line = line.rstrip()
            working_list.append(stripped_line)
        for item in working_list:
            working_string += ' ' + item
        working_string = working_string.replace(" ", '')
        lesson_objects()
        file.close()

run("ddd.carb")





