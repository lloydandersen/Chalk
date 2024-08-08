import re

lesson_list = []
question_dict = {}
answer_dict = {}

def get_lesson_list(file):
    for line in file:
        # word = line.split(' ', 1)
        x = re.findall("L", line)
        if x != []:
            lesson_list.append(line.rstrip())
    return lesson_list

def split_lessons(file):
    sentence = ""
    for line in file:
        print(line)



def run(file_name):
    file = open(f"{file_name}", "r")
    lessons = get_lesson_list(file)
    splits = split_lessons(file)
    print(splits)

    file.close()


run("ddd.carb")

