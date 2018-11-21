from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

# replace ____ with your answer
____ = 'undefined'


@csrf_exempt
def student_list(request):
    # two functions: GET the list of all students, or POST a new student
    if request.method == 'GET':
        # get all instances from Student, then serialize them into a json string
        data = serializers.serialize(____, Student.____)
        return HttpResponse(____, content_type=____)
    elif request.method == 'POST':
        # decode the request body into a json string
        data = request.____.decode('utf-8')
        # convert the json string to a dict
        dct = json.____(data)
        name = dct['name']
        college = dct['college']
        year = dct['year']
        courses = dct['courses']
        # create a new Student instance
        student = Student(____)
        # save the instance
        student.____()
        dct = {'success': 1}
        # wrapping dct into a json string, then return a HttpResponse
        return JsonResponse(dct)


# new student example #0
'''
{
  "name": "Pikachu",
  "college": "CAS",
  "year": 1,
  "courses": "[\"CAS PY 105\", \"CAS CH 101\", \"CAS BI 105\", \"CAS CS 111\"]"
}
'''

# new student example #1
'''
{
  "name": "Teemo",
  "college": "PDP",
  "year": 3,
  "courses": "[\"Blinding Dart\", \"Move Quick\", \"Toxic Shot\", \"Noxious Trap\"]"
}
'''

# new student example #2
'''
{
  "name": "Techies",
  "college": "ENG",
  "year": 5,
  "courses": "[\"Proximity Mines\", \"Stasis Trap\", \"Blast Off!\", \"Remote Mines\"]"
}
'''
