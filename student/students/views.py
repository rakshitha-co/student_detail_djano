from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Student

def student_list(request):
    # Read student details from the file (e.g., CSV, JSON)
    # Parse the file data and create Student objects

    # Get the queryset of all students
    queryset = Student.objects.all()

    # Paginate the queryset based on the requested page number
    page_number = request.GET.get('page')
    paginator = Paginator(queryset, 10)  # Assuming 10 students per page
    page_obj = paginator.get_page(page_number)

    # Prepare the response data
    students = []
    for student in page_obj:
        students.append({
            'id': student.id,
            'name': student.name,
            'total_marks': student.total_marks,
        })

    # Return the paginated data as a JSON response
    return JsonResponse({
        'students': students,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number,
    })

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Create your views here.
