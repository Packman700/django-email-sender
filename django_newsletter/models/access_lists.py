from django.db import models


class List(models.Model):
    """ For storing emails in white and black list """
    email_domain = models.CharField(max_length=255)

    class Meta:
        abstract = True

    @classmethod
    def contains(cls, domain):
        """Constrain is finding by simple string.endswith()"""
        objects = cls.objects.all()
        for obj in objects:
            if domain.endswith(obj.email_domain):
                return True
        return False

    def __str__(self):
        return self.email_domain


class WhiteList(List):
    pass


class BlackList(List):
    pass
