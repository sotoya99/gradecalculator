import os
import matplotlib.pyplot as plt
import math

class Assignment:
    def __init__(self, name, id, points):
        self.name = name
        self.id = int(id)
        self.points = int(points)
    
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = int(student_id)

class Submission:
    def __init__(self, student_id, assignment_id, score_percent):
        self.student_id = int(student_id)
        self.assignment_id = int(assignment_id)
        self.score_percent = int(score_percent)

def get_students():
    students = {}

    with open("data/data/students.txt", "r") as f:
        for line in f:
            # print("Name: ", line[3:].strip())
            # print("ID: ", line[:3])
            students[line[3:].strip()] = Student(line[3:].strip(), line[:3])

    return students

def get_assignments():
    #Line 1 = assignment name
    #line 2 = assignment id
    #line 3 = point value
    assignments = {}

    with open("data/data/assignments.txt", "r") as f:
        lines = f.readlines()

        for i in range(0, len(lines), 3):
            name = lines[i]
            id = lines[i+1]
            points = lines[i+2]
            assignments[name] = Assignment(name, id, points)

    return assignments

def get_submissions():
    submissions = []

    for filename in os.listdir("data/data/submissions"):
        with open(f"data/data/submissions/{filename}", "r") as f:
            student_id, assignment_id, percent_points = f.read().split("|")
            submissions.append(Submission(student_id, assignment_id, percent_points))

    return submissions

def main():
    students = get_students()
    assignments = get_assignments()
    submissions = get_submissions()

    menu = "1. Student grade\n2. Assignment statistics\n3. Assignment graph\n"
    print(menu)
    sel = int(input("Enter your selection: "))

    if sel == 1:
        name = input("What is the student's name: ")
        total_points = 0

        if name not in students:
            print("Student not found")
            return
        for student in students:
            if student == name:
                student_id = students[student].student_id
                for submission in submissions:
                    if submission.student_id == student_id:
                        for assignment_object in assignments.values():
                            if submission.assignment_id == assignment_object.id:
                                total_points += assignment_object.points * submission.score_percent
        print(f"{total_points/1000:.0f}%")
    elif sel == 2:
        points = []
        assignment_name = input("What is the assignment name: ")

        for assignment_object in assignments.values():
            if f"{assignment_name}\n" == assignment_object.name:
                for submission in submissions:
                    if submission.assignment_id == assignment_object.id:
                        points.append(submission.score_percent)

        min_score = min(points)
        max_score = max(points)
        average_score = sum(points) / len(points)
        print(f"Min: {min_score}%\nAvg: {math.trunc(average_score)}%\nMax: {max_score}%")
    elif sel == 3:
        scores = []
        assignment_name = input("What is the assignment name: ")

        for assignment_object in assignments.values():
            if f"{assignment_name}\n" == assignment_object.name:
                for submission in submissions:
                    if submission.assignment_id == assignment_object.id:
                        scores.append(submission.score_percent)
        plt.hist(scores, bins=[50, 60, 70, 80, 90, 100])
        plt.show()


if __name__ == "__main__":
    main()