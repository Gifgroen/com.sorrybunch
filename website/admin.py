from django.contrib import admin

from website.models import Article, Gig

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'placed', 'author')
	order_by = ('placed' )
	
	class Meta:
		verbose_name = 'article'
		verbose_name_plural = 'articles'

class GigAdmin(admin.ModelAdmin):
	list_display = ('name', 'place', 'link', 'date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Gig, GigAdmin)