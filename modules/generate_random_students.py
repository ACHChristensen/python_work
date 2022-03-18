from asyncore import write
import pandas as pd 
import random
import csv
from classes.Course import Course
from classes.DataSheet import DataSheet
from classes.Student import Student

def get_list_names():
    file = '../navne.csv'
    col_list = ["Navn", "Drengenavn","Pigenavn"]
    df = pd.read_csv(file, usecols=col_list, encoding='latin1')
    return [name for name in df["Navn"].tolist() if name.isalpha()]

def get_random_student():
    names = get_list_names()
    genders = ["Female", "Male", "Other"]
    grades = [-3, 0, 2, 4, 7, 10, 12, None]
    courses = [Course("Math",1.23, "Sylvester Stalone", 5, grades[random.randrange(0, len(grades))]), Course("Magic",2.22, "Harry Potter", 15,grades[random.randrange(0, len(grades))]), Course("Data Science - Python",1.05, "Thomas Hartmann", 10, grades[random.randrange(0, len(grades))])]        
    
    rand_name = names[random.randrange(0,len(names))]
    rand_gender = genders[random.randrange(0,len(genders))]
    rand_courses = [course for course in courses[0:random.randrange(0,3)]]
    rand_data_sheet = DataSheet(rand_courses)
    image_url = "https://simplecode.dk/wp-content/uploads/2021/05/TrollFace-1024x790.jpeg"
    return Student(rand_name, rand_gender, rand_data_sheet, image_url)

def get_random_students_list(qnty):
    return [get_random_student() for i in range(0,qnty+1)]

def students_writer(students):
    file = "Random_Students"
    students_info = []
    students_info.append([{'stud_name': student.name, 'course_name': student.data_sheet.courses[0].name, 'teacher': student.data_sheet.courses[0].teacher, 'gender': student.gender, 'etcs': student.data_sheet.courses[0].etcs, 'classroom' : student.data_sheet.courses[0].classroom, 'grade':student.get_avg_grade, 'img_url':student.image_url}for student in students])
    with open(file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['stud_name', 'course_name', 'teacher', 'gender', 'etcs', 'classroom', 'grade', 'img_url'])
        writer.writeheader()
        writer.writerows(students_info)


if __name__ == '__main__':
    students_writer(get_random_students_list(20))