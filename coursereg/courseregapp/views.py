from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Course, Student, Payment, PaymentTrack
from datetime import datetime


def home(request):

    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']
        price = request.POST['price']
        duration = request.POST['duration']

        course = Course(name=name, description=desc, price=price, duration=duration )
        course.save()
        return redirect('courses')

    else:
        return render(request, 'coursereg.html')


def courses(request):

    courses = Course.objects.all()

    return render(request, 'allcourses.html', {"courses": courses})


def students(request):

    students = Student.objects.all()

    return render(request, 'allstudents.html', {"students": students})


def student(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        nokname = request.POST['nokname']
        nokrelation = request.POST['nokrelation']
        noknumber = request.POST['noknumber']
        course = request.POST['course']
        batch = request.POST['batch']
        status = request.POST['status']
        program = request.POST['program']

        course = get_object_or_404(Course, name=course)
        coursefee = course.price

        student = Student(firstName=fname, lastName=lname, age=age, email=email, gender=gender,
                             phoneNumber=phone, nextOfKinName=nokname, nextOfKinRelationship=nokrelation,
                          nextOfKinNumber=noknumber, courseId=course, batch=batch, courseFee=coursefee,
                          courseStatus=status, programType=program)
        student.save()



        # subject = f'Welcome To SoftCodeMath Solutions & Academy {fname}'
        # message = f'Your Student Id is Soft{datetime.year.now()}{student.id}'
        # recipient_list = [email]  # Replace with recipient email(s)
        #
        # send_mail(
        #     subject,
        #     message,
        #     'rilelaboye@gmail.com',  # From email (matches EMAIL_HOST_USER)
        #     recipient_list,
        #     fail_silently=False,  # Raise error if sending fails
        # )


        return redirect("students")

    else:
        courses = Course.objects.all()

        return render(request, 'studentreg.html', {"courses": courses})


def payment(request):

    students = Student.objects.all()

    if request.method == "POST":
        amount = float(request.POST['amount'])
        student = request.POST['student']

        student = get_object_or_404(Student, firstName=student)
        courseFee = student.courseFee



        # balance_to_pay =0
        # total_payment=0
        #
        # payments = Payment.objects.all()
        #
        # for p in payments:
        #     if p.studentId.firstName == student.firstName:
        #         total_payment += p.amount
        #
        # balance_to_pay = student.courseFee - total_payment

        payment = Payment(amount=amount, studentId=student)
        payment.save()

        if PaymentTrack.objects.filter(studentId=student).exists():

            ptrack = get_object_or_404(PaymentTrack, studentId=student)

            amount_total = ptrack.totalAmountPaid + amount
            ptrack.totalAmountPaid = amount_total

            ptrack.balanceToPay = ptrack.courseFee - amount_total
            ptrack.save()

            return redirect("payments")

        else:

            balance_to_pay = 0

            balance_to_pay = student.courseFee - amount

            payment_track = PaymentTrack(studentId=student, courseFee=courseFee, totalAmountPaid=amount,
                                         balanceToPay=balance_to_pay)
            payment_track.save()
            return redirect('payments')


    else:
        return render(request, 'payment.html', {"students": students})


def payments(request):

    payments = Payment.objects.all()

    return render(request, 'allpayments.html', {"payments": payments})


def payment_track(request):

    payment_tracks = PaymentTrack.objects.all()

    return render(request, 'allpaymenttracks.html', {"payment_tracks":  payment_tracks})



def search_payment(request):

    students = Student.objects.all()

    if request.method == "POST":

        student_name = request.POST['name']

        student_name = get_object_or_404(Student, firstName=student_name)

        payments = Payment.objects.filter(studentId__exact=student_name)

        return render(request, 'searchpayment.html', {"payments": payments, "students": students})

    return render(request, 'searchpayment.html', context={"students": students})
