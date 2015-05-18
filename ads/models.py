from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)
	
	def __str__(self):
		return self.slug

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	parent = models.IntegerField()
	
	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"
		ordering = ["parent"]

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=200)
	image = models.TextField()
	price = models.FloatField()
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	tags = models.ManyToManyField(Tag)
	category = models.ManyToManyField(Category)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Ad Entry"
		verbose_name_plural = "Ad Entries"
		ordering = ["-created"]
		
#User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
 
    def __str__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'
 
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
    
    def profile_image_url(self):
    	fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
 
    	if len(fb_uid):
        	return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])