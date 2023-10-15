from django.contrib import admin
from .models import Article, Articles_tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tag_count += 1

        if main_tag_count == 0:
            raise ValidationError('Должен быть выбран хотя бы один основной тег')
        elif main_tag_count > 1:
            raise ValidationError('Может быть только один основной тег')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image', ]
    inlines = [ScopeInline, ]


@admin.register(Articles_tag)
class Articles_tagAdmin(admin.ModelAdmin):
    list_display = ['name', ]
