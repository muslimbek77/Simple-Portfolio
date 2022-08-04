from django.contrib import admin

from portfolio.models import Home,About,Project,Services,Contact

# Register your models here.
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Services)