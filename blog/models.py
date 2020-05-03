from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_text = models.TextField()
    blog_image = models.ImageField()
    pub_date = models.DateTimeField()

    def __str__(self):
        pass
        return self.blog_title
