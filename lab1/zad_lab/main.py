from argparse import ArgumentError
from multiprocessing.sharedctypes import Value
from sys import argv


# courses_info - {courses_dict, max_courses, max_participants}
def add_participant(courses_info, course_name, name):
    if course_name not in courses_info["courses_list"]:
        raise ValueError("Invalid course name")
    if courses_info["max_participants"] <= len(courses_info):
        raise ValueError("Group is full")
    
    courses_info["courses_list"][course_name].append(name)


def remove_participant(courses_info, course_name, name):
    if course_name not in courses_info["courses_list"]:
        raise ValueError("Invalid course name")
    if name not in courses_info["courses_list"][course_name]:
        raise ValueError("Participant not in group")

    courses_info["courses_list"][course_name].remove(name)

def add_course(courses_info, course_name):
    if course_name in courses_info["courses_list"]:
        raise ValueError("Course already exists")
    if len(courses_info["courses_list"].keys()) >= courses_info["max_courses"]:
        raise ValueError("Too many courses")
    
    courses_info["courses_list"][course_name] = []

def remove_course(courses_info, course_name):
    if course_name not in courses_info["courses_list"]:
        raise ValueError("No such course")
    
    courses_info["courses_list"].pop(course_name)

def modify_course(courses_info, old_course_name, new_course_name):
    if old_course_name not in courses_info["courses_list"]:
        raise ValueError("No such course")
    if new_course_name in courses_info["courses_list"]:
        raise ValueError("Course already exists")
    courses_info["courses_list"][new_course_name] = courses_info["courses_list"].pop(old_course_name)


def run_query(courses_info, inp):
    args = inp.split()
    match args[0]:
        case "AP":
            if len(args) != 3:
                raise ArgumentError("Invalid number of arguments")
            add_participant(courses_info, args[1], args[2])
        case "RP":
            if len(args) != 3:
                raise ArgumentError("Invalid number of arguments")
            remove_participant(courses_info, args[1], args[2])
        case "AC":
            if len(args) != 2:
                raise ArgumentError("Invalid number of arguments")
            add_course(courses_info, args[1])
        case "RC":
            if len(args) != 2:
                raise ArgumentError("Invalid number of arguments")
            remove_course(courses_info, args[1])
        case "MC":
            if len(args) != 3:
                raise ArgumentError("Invalid number of arguments")
            modify_course(courses_info, args[1], args[2])


if __name__ == "__main__":
    if len(argv) <= 2:
        print("Invalid number of arguments")
        exit(1)
    
    courses_info = {}
    try:
        courses_info["max_courses"] = int(argv[1])
        courses_info["max_participants"] = int(argv[2])
    except ValueError:
        print("Invalid arguments")
        exit(1)

    # operation in the form of:
    # AP [course_name] [name] - add participant
    # RP [course_name] [name] - remove participant
    # AC [course_name] - add course
    # RC [course_name] - remove course
    # MC [course_name] - modify course name

    courses_info["courses_list"] = {}
    while True:
        try:
            inp = input()
        except EOFError:
            print(courses_info)
            exit(0)
        run_query(courses_info, inp)
