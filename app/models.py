from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)


class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=200)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.IntegerField()
    highsal=models.IntegerField()

class Bonus(models.Model):
    sal=models.IntegerField()
    grade=models.ForeignKey(Salgrade,on_delete=models.CASCADE)