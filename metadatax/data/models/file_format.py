from django.db import models


class FileFormat(models.Model):
    class Meta:
        db_table = "mx_data_fileformat"
        ordering = ("name",)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, help_text="Format of the file")
