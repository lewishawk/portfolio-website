from django.db import models

# Constants
TITLE_MAX_CHARACTER_LENGTH = 200
LINK_URL_MAX_CHARACTER_LENGTH = 400
TAG_NAME_MAX_CHARACTER_LENGTH = 100
PROJECTS_FOREIGN_KEY_NAME = "projects" # The foreign key field inside of the 'Tags' table
IMAGES_FOREIGN_KEY_NAME = "images"
IMAGE_UPLOAD_DIRECTORY = "project_images/"
PROJECT_IMAGE_STRING_FORMAT = "{0} Image"

# A model for a blog entries
class Blog(models.Model):
    creationDateTime = models.DateTimeField(auto_now = False, auto_now_add = True, blank = True) # Automatically updates to the time of creation
    lastModifiedDateTime = models.DateTimeField(auto_now = True, auto_now_add = False, blank = True) # Automatically updates to the time 
    title = models.CharField(max_length = TITLE_MAX_CHARACTER_LENGTH)
    entry = models.TextField()
    
    # Returns the title of the blog entry as a string
    def __str__(self):
        return self.title

# A model for tag entries
class Tag(models.Model):
    name = models.CharField(max_length = TAG_NAME_MAX_CHARACTER_LENGTH, unique = True)
    
    # Returns the name of the tag as a string
    def __str__(self):
        return self.name

# A model for project entries
class Project(models.Model):
    title = models.CharField(max_length = TITLE_MAX_CHARACTER_LENGTH)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name = PROJECTS_FOREIGN_KEY_NAME)
    link = models.URLField(max_length = LINK_URL_MAX_CHARACTER_LENGTH, blank = True)
    
    # Returns the title of the project entry as a string
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name = IMAGES_FOREIGN_KEY_NAME, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = IMAGE_UPLOAD_DIRECTORY)
    
    # Returns the title of the project along with the suffix "Image"
    def __str__(self):
        return str.format(PROJECT_IMAGE_STRING_FORMAT, self.project.title)