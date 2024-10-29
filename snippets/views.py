from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.serializers import PersonSerializer
from .models import Person

# @api_view(['GET', 'POST'])
# def index(request):
#     courses = {
#         "course_name" : "rest framework",
#         "course_provider" : "scaler",
#         "frameworks" : ["flask", "django", "tornado"],
#         }

#     if request.method == 'GET':
#         data = request.GET.get('search')
#         print("$$$$$$$$$$$$")
#         print(data)
#         print("$$$$$$$$$$$$")
    
#         return Response(courses)
    
#     elif request.method == 'POST':
#         data = request.data
#         print("#############")
#         print(data["age"])
#         print("#############")

#         return Response(courses)
    
@api_view(["GET", "POST"])
def people(request):
    if request.method == "GET":
        obj = Person.objects.all()
        serializer = PersonSerializer(obj, many = True)
        return Response(serializer.data)
    
    else:
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data()
        
        else:
            return Response(serializer.errors)
