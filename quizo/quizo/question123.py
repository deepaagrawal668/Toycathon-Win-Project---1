# class Question:

#     def __init__(self):
#         self.points = 0

#     def questioAttempt(self, marks):
#         self.points += marks

#     def result(self):
#         return self.points

from quizoApp.models import Question
def showFunction(token):
    set1 = set()
    query = Question.objects.filter(domain = token).first()
    print(query)
    #if query not in set1:

showFunction('Algebra')

