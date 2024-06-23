import json


def attendances_into_json(data: list):
    #  @TODO if JSON would be needed
    header = ["id_student", "first_name", "last_name", "class", "meal_type", "date"]
    data = [
        [1, 'Adam', 'Nowak', '1a', 1, '2024-06-18'],
        [1, 'Adam', 'Nowak', '1a', 2, '2024-06-18'],
        [1, 'Adam', 'Nowak', '1a', 4, '2024-06-18'],
        [2, 'Robert', 'Rogacz', '2b', 1, '2024-06-18'],
        [2, 'Robert', 'Rogacz', '2b', 2, '2024-06-18'],
        [2, 'Robert', 'Rogacz', '2b', 3, '2024-06-18']
    ]

    # Create a dictionary to store student information
    students_dict = {}
    for row in data:
        student_id = row[0]
        if student_id not in students_dict:
            students_dict[student_id] = {
                header[i]: row[i] for i in range(len(header))
            }
            students_dict[student_id]["meal_type"] = [row[4]]
        else:
            students_dict[student_id]["meal_type"].append(row[4])

    # Convert the dictionary to a list of student records
    students_list = list(students_dict.values())

    # Convert the list of dictionaries to a JSON-formatted string
    json_output = json.dumps(students_list, indent=4)

    print(json_output)


def format_presence(person: list[list], ref: dict) -> list[str]:
    """
    Helper for changing ids of meal type into readable text
    :param person:
    :param ref: names of meal types connected with ids
    :return: list of text in csv format
    """
    presence = []
    for i in range(1, len(ref.keys())+1):
        presence.append('Obecny' if str(i) in person[3:] else 'Nie')

    return presence


def format_person(person: list[list], ref: dict) -> str:
    """
    Helper for converting SQL response into CSV text
    :param person:
    :param ref: names of meal types connected with ids
    :return: text in csv format
    """
    return ';'.join(person[:3] + format_presence(person, ref))
