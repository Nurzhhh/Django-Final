from django.db import models

# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'base'
        verbose_name_plural = 'bases'

    def __str__(self):
        return self.name

class Book(models.Model):
    base = models.ManyToManyField(BookJournalBase, related_name='books')
    num_pages = models.PositiveIntegerField()
    genre = models.CharField(max_length=150, unique=True, null=False, blank=False)

    def __str__(self):
        return self.genre

class Journal(models.Model):
    choises = (
        ('Bullet', 'Bullet'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Sport', 'Sport'),
    )
    base = models.ManyToManyField(BookJournalBase, related_name='journals')
    type = models.CharField(max_length=10, choices=choises)
    publisher = models.CharField(max_length=150, unique=True, null=False, blank=False)

    def __str__(self):
        return self.publisher