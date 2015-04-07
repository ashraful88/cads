from django.db import models

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
	image = models.ImageField(upload_to='')
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