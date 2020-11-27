import argparse
from DataLoader import load


class Handler:
    def __init__(self):
        pass


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_students', type=str, help='path to students.json')
    parser.add_argument('path_rooms', type=str, help='path to rooms.json')
    parser.add_argument('output_format', type=str, choices=['json', 'xml'], help='preferred output format')
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = args_parser()
    students = load(args.path_students)
    rooms = load(args.path_rooms)



