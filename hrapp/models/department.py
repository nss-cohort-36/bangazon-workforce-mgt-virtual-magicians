from django.db import models

class Department(models.Model):

    dept_name = models.CharField(max_length=50)
    dept_budget = models.IntegerField()

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_details", kwargs={"pk": self.pk})

