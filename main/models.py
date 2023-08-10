from django.db import models

class Main(models.Model):
    name = models.CharField("Nomi", max_length=100)
    title = models.TextField("Ma'lumot")
    info = models.TextField("Footer uchun ma'lumot")
    img = models.ImageField("Rasm", upload_to="image/")
    tel = models.CharField("TelRaqam", max_length=13)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bosh sahifa"
        verbose_name_plural = "Bosh sahifa"


class Services(models.Model):
    name = models.CharField("Servis nomi", max_length=100)
    title = models.CharField("Qisqacha ma'lumot", max_length=250)
    img = models.ImageField("svg rasm", upload_to="image/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xizmatlar"
        verbose_name_plural = "Xizmatlar"


class About(models.Model):
    title = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Biz xaqimizda"
        verbose_name_plural = "Biz xaqimizda"


class Testimonial(models.Model):
    name = models.CharField("Nomi", max_length=100)
    info = models.CharField("Mutaxasisligi", max_length=100)
    title = models.TextField("Ma'lumot")
    img = models.ImageField("Rasm", upload_to="image/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fikirlar"
        verbose_name_plural = "Fikirlar"



