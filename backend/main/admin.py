from django.contrib import admin
from .models import Blog, Tag, Project, ProjectImage

# Constants
TITLE_FIELD_NAME = "title"
LINK_FIELD_NAME = "link"
DESCRIPTION_FIELD_NAME = "description"
TAGS_FIELD_NAME = "tags"
NAME_FIELD_NAME = "name"
ENTRY_FIELD_NAME = "entry"
CREATION_DATETIME_FIELD_NAME = "creationDateTime"
NUMBER_OF_IMAGES_TO_UPLOAD = 1

# Configures the admin view for image uploading
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = NUMBER_OF_IMAGES_TO_UPLOAD

# Configures the admin view for the project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = (TITLE_FIELD_NAME, LINK_FIELD_NAME)
    inlines = [ProjectImageInline]
    search_fields = (TITLE_FIELD_NAME, DESCRIPTION_FIELD_NAME)
    list_filter = (TAGS_FIELD_NAME,)

# Configures the admin view for the tag model
class TagAdmin(admin.ModelAdmin):
    list_display = (NAME_FIELD_NAME,)
    search_fields = (NAME_FIELD_NAME,)

# Configures the admin view for the blog model
class BlogAdmin(admin.ModelAdmin):
    list_display = (TITLE_FIELD_NAME, CREATION_DATETIME_FIELD_NAME)
    search_fields = (TITLE_FIELD_NAME, CREATION_DATETIME_FIELD_NAME, ENTRY_FIELD_NAME)

# Bind the models to corresponding admin configurations
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage) # Just renders the project image, as there is no customisation
admin.site.register(Blog, BlogAdmin)