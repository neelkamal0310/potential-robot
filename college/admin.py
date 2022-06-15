from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    # Fields to display in the admin page
    list_display = [
        # "id",
        "full_name",
        "roll_number",
        "mobile_number",
        "batch",
        "major",
        "address",
        "city",
        "state",
        "guardian_name",
        "guardian_number",
    ]
    # Search fields
    search_fields = [
        "full_name",
        "roll_number",
        "mobile_number",
    ]
    # Filter results
    list_filter = [
        "batch",
        "major",
        "state",
    ]
    ordering = ['-created_at']

# Add model to the admin
admin.site.register(Student, StudentAdmin)

# Remove default models from admin
admin.site.unregister(User)
admin.site.unregister(Group)
