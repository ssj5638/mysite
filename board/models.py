from django.db import models
from user.models import User

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=200)
    message = models.CharField(max_length=3000)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)     # CASCADE USER가 삭제되면 글도 지워짐

    def __str__(self):
        return 'Board(%s, %s, %d, %s, %d, %s)'% (self.title,
                                                 self.message,
                                                 self.hit,
                                                 str(self.regdate),
                                                 self.user.id,
                                                 self.user.name)