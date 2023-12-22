from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    like = models.IntegerField(default=0)

    def process_like(self, user_ip):
        existing_like = self.likes.filter(ip=user_ip).first()

        if existing_like:
            existing_like.delete()
            self.like -= 1
        else:
            self.like += 1
            Like.objects.create(profile=self, ip=user_ip)

        self.save()

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes')  # Указываем related_name
    ip = models.GenericIPAddressField()
