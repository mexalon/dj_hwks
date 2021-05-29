from django.contrib import admin

from .models import Article, Scope, Scope_Article


class Scope_ArticleInline(admin.TabularInline):
    model = Scope_Article
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (Scope_ArticleInline, )


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = (Scope_ArticleInline, )
