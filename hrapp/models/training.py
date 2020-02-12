from django.db import models

class Training(models.Model): 

    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()

    class Meta:
        verbose_name = ("Training")
        verbose_name_plural = ("Trainings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Training_detail", kwargs={"pk": self.pk})
