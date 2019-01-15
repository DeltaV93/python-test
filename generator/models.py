from django.db import models


class Dictionary(models.Model):
    word = models.CharField(max_length=200)
    word_value = models.IntegerField()

    def __str__(self):
        return self.word

    def word_color_value(self):
        # What is this for?
        return self.word_value

# Add complexity by adding a second model with a foriegn key.