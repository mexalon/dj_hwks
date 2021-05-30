from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, Topic


class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        no_main = True
        one_main = False
        for form in self.forms:
            if not form.cleaned_data.get('is_main'):
                continue
            else:
                if one_main:
                    raise ValidationError('Может быть только одна главная тема')
                else:
                    one_main = True
                    no_main = False

        if no_main:
            raise ValidationError('Не задана главная тема')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopesInline(admin.TabularInline):
    model = Scopes
    extra = 1
    formset = ScopesInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ScopesInline,)


@admin.register(Topic)
class ScopeAdmin(admin.ModelAdmin):
    pass

