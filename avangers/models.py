from django.db import models as m

# Create your models here.


class Comments(m.Model):
    title = m.CharField(max_length=200)
    description = m.TextField()
    created_at = m.DateTimeField(auto_now_add=True)
    user=m.ManyToManyField('users.User',related_name='comments')
    technique=m.ManyToManyField('app.Technique',related_name='comments')

    def __str__(self):
        return self.title

class Applicaion(m.Model):
    user=m.ManyToManyField('users.User',related_name='applications')
    technique=m.ManyToManyField('app.Technique',related_name='applications')
    created_at = m.DateTimeField(auto_now_add=True)
    status=[('pending','pending'),('approved','approved'),('rejected','rejected')]
    status=m.CharField(max_length=10,choices=status,default='pending')
    date_of_beging=m.DateField()
    date_of_end=m.DateField()

    def __str__(self):
        return self.status