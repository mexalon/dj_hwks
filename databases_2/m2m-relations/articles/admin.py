from django.contrib import admin

from .models import Article, Scopes, Topic


class ScopesInline(admin.TabularInline):
    model = Scopes
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ScopesInline, )


@admin.register(Topic)
class ScopeAdmin(admin.ModelAdmin):
    inlines = (ScopesInline, )
