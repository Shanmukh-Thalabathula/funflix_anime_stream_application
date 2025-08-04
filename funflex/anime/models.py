from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class AnimeTitle(models.Model):
    image = models.ImageField(upload_to='anime_images/')
    title = models.CharField(max_length=200, unique=True)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_categories(self):
        return ", ".join(category.name for category in self.category.all())

class Episode(models.Model):
    anime = models.ForeignKey(AnimeTitle, on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    episode_name = models.CharField(max_length=200, null=True, blank=True)
    episode_video = models.FileField(upload_to='anime_episodes/')
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('anime', 'episode_number')  # Prevent duplicate episodes

    def __str__(self):
        return self.episode_name if self.episode_name else f"Episode {self.episode_number} of {self.anime.title}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime_title = models.ForeignKey(AnimeTitle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'anime_title')  # Prevent duplicate favorites

    def __str__(self):
        return f"{self.user.username} - {self.anime_title.title}"  # Fixed __str__
