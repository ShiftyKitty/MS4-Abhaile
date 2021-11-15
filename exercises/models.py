from django.db import models
from elements.models import Element

# Create your models here.

class Breathwork(models.Model):
    element = models.ForeignKey(Element, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    how_to = models.TextField()
    benefits = models.TextField()
    inhale_1 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    exhale_1 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    inhale_2 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    exhale_2 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    inhale_3 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    exhale_3 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    inhale_4 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    exhale_4 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    post_inhale_ht = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    post_exhale_ht = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    post_reps_breath_hold = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    recovery_inhale = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    recovery_exhale = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    recovery_bh = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    inhale_reps = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    exhale_reps = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    breath_reps = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    youtube_link = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name