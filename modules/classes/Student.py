class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name 
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    @property
    def get_avg_grade(self):
        grades_sorted = []
        for grade in self.data_sheet.get_grades_as_list():
            if(grade == None):
                break
            else:
                grades_sorted.append(grade) 
        total_grade = sum(grades_sorted)
        if(total_grade == 0):
            return "No grades "
        return total_grade

    def __str__(self):
        return f'students info: name: {self.name}, gender: {self.gender}, image_url {self.image_url}, avarage grade: {self.get_avg_grade}'