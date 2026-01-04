from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    price = models.FloatField()
    duration = models.CharField(max_length=45)
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=45)
    nextOfKinName = models.CharField(max_length=45)
    nextOfKinRelationship = models.CharField(max_length=45)
    nextOfKinNumber = models.CharField(max_length=45)
    courseId = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    courseFee = models.FloatField()
    batch = models.CharField(max_length=45)
    classStatus = models.CharField(max_length=45, default="Active")
    programType = models.CharField(max_length=45, default="Career Course")
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstName


class Payment(models.Model):
    amount = models.FloatField()
    studentId = models.ForeignKey(Student, related_name='payment', on_delete=models.CASCADE)
    paymentDate = models.DateField(auto_now_add=True)


class PaymentTrack(models.Model):

    studentId = models.ForeignKey(Student, related_name='paymenttrack', on_delete=models.CASCADE)
    courseFee = models.FloatField()
    totalAmountPaid = models.FloatField()
    balanceToPay = models.FloatField()


class Staff(models.Model):

    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=45)
    role = models.CharField(max_length=45)
    qualification = models.CharField(max_length=45)
    skill = models.CharField(max_length=45)
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstName











