from django.shortcuts import render, redirect,get_object_or_404
from .models import student


# CREATE — Add student
def addastudent(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        age = request.POST.get("age")
        marks = request.POST.get("marks")

        student.objects.create(
            name=name,
            email=email,
            department=department,
            age=age,
            marks=marks
        )

        return redirect("view")

    return render(request, "add.html")


# READ — View all students
def viewdata(request):

    students = student.objects.all()

    return render(request, "viewdata.html", {"students":students})


def update_student(request, id):

    st = get_object_or_404(student, id=id)

    if request.method == "POST":

        st.name = request.POST.get("name")
        st.email = request.POST.get("email")
        st.department = request.POST.get("department")
        st.age = request.POST.get("age")
        st.marks = request.POST.get("marks")

        st.save()

        return redirect("view")

    return render(request, 'update.html', {'st': st})


def deletemethod(request,id):
    st=get_object_or_404(student,id=id)
    st.delete()
    return redirect("view")


def python_student(request):
    m=student.objects.filter(department="python full stack developer")
    return render(request,"viewdata.html",{"students":m})



def high_marks(request):
    si=student.objects.filter(marks__gt=80)
    return render(request,"viewdata.html",{"students":si})



def total_students(request):
    s=student.objects.count()
    return render(request,"total.html",{"students":s})