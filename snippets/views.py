from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def index(request):
    courses = {
        "course_name" : "rest framework",
        "course_provider" : "scaler",
        "frameworks" : ["flask", "django", "tornado"],
        }

    if request.method == 'GET':
        data = request.GET.get('search')
        print("$$$$$$$$$$$$")
        print(data)
        print("$$$$$$$$$$$$")
    
        return Response(courses)
    
    elif request.method == 'POST':
        data = request.data
        print("#############")
        print(data["age"])
        print("#############")

        return Response(courses)