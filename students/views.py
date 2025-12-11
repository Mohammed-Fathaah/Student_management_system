from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
# Create your views here.
def student_list(request):
    search=request.GET.get('search','')
    department=request.GET.get('department','')

    students=Student.objects.all()

    if search:
        students=students.filter(name__icontains=search) | students.filter(roll__icontains=search)

    if department:
        students=students.filter(department=department)

    departments=Student.objects.values_list('department',flat=True).distinct()

    return render(request,'student_list.html',{
      'students':students,
      'departments':departments,
      'search':search  
    })


def student_add(request):
    if request.method=='POST':
        roll=request.POST['roll']
        name=request.POST['name']
        age=request.POST['age']
        department=request.POST['department']
        mark=request.POST['mark']

        Student.objects.create(
            roll=roll,name=name,age=age,department=department,mark=mark
        )

        return redirect('student_list')
    
    return render(request,'student_form.html')

def student_edit(request,id):
    student=get_object_or_404(Student,id=id)

    if request.method=='POST':
        student.roll=request.POST['roll']
        student.name=request.POST['name']
        student.age=request.POST['age']
        student.department=request.POST['department']
        student.mark=request.POST['mark']
        student.save()
        return redirect('student_list')
    return render(request,'student_form.html',{'student':student})

def student_delete(request,id):
    student=get_object_or_404(Student,id=id)
    student.delete()
    return redirect('student_list')