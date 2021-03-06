from django.db import models
from django.core.urlresolvers import reverse


class Paste(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=20)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
    