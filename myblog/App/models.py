from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_text = models.CharField(max_length=5000)
    blog_date = models.DateTimeField('date published')

    def __str__(self):
        return self.blog_title

    def get_preview(self):
        x = 550 if len(self.blog_text) > 490 else len(self.blog_text)
        if(x == 550):
            while(self.blog_text[x:(x+1)] != ' '):
                x = x + 1
        return self.blog_text[:x] + (".." if self.blog_text[(x-1):x] == '.' else "...")
