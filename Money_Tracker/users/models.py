from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

"""
CREATE TABLE "users_profile" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "image" varchar(100) NOT NULL, 
    "user_id" integer NOT NULL UNIQUE REFERENCES 
    "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
    );
COMMIT;
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # this will create a folder named 'profile_pics' where they will be uploaded.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        # parent class save
        super(Profile,self).save(*args, **kwargs)
        # open current image
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            # resize
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
