class DataSheet():
    
    def __init__(self, courses = None):
        self.courses = courses if courses else []

    def get_grades_as_list(self):
        return [course.grade for course in self.courses]