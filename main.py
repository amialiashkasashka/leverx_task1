import json
import re

url_students = 'students.json'
url_rooms = 'rooms.json'

def get_json(url_rooms, url_students):
    with open(url_rooms) as rooms_json:
        rooms = json.loads(rooms_json.read())
    with open(url_students) as students_json:
        students = json.loads(students_json.read())

    check(rooms, students)

def check(rooms, students):

    for i in range(len(students)):
        room_name = re.search(r'#(\w+)', rooms[i].get('name'))
        if students[i].get('room') ==  room_name.group(1):
            pass

get_json(url_rooms, url_students)

