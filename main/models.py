from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(default=False)
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name="Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"

class Fan(models.Model):
    nom = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish,on_delete=models.SET_NULL, null=True)
    asosiy = models.BooleanField(default=False)
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name="Fan"
        verbose_name_plural = "Fanlar"

class Ustoz(models.Model):
    ism = models.CharField(max_length=50)
    yosh  = models.PositiveSmallIntegerField()
    jinsi = models.CharField(max_length=50,choices=(('erkak','erkak'),('ayol','ayol')))
    daraja = models.CharField(max_length=50,choices=(('Bakalav','Bakalav'),('Magistr','Magistr')))
    fan =  models.ForeignKey(Fan,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.ism
    class Meta:
        verbose_name="Ustoz"
        verbose_name_plural = "Ustozlar"

