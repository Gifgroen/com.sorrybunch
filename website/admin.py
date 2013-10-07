from django.contrib import admin

from website.models import Article, Gig, Video, Audio

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'placed', 'author')
	order_by = ('placed' )
	
	class Meta:
		verbose_name = 'article'
		verbose_name_plural = 'articles'

class GigAdmin(admin.ModelAdmin):
	list_display = ('name', 'place', 'link', 'date')

class VideoAdmin(admin.ModelAdmin):
	list_display = ('video_id', 'active', 'width', 'height', )

class AudioAdmin(admin.ModelAdmin):
	list_display = ('album_id', 'bandcamp_url', 'link',  'width', 'height',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Gig, GigAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)