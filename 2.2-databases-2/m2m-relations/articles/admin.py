from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, Tags


class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            count += 1 if form.cleaned_data.get('is_main') else 0
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        elif count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class ScopesInline(admin.TabularInline):
    model = Scopes
    formset = ScopesInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopesInline]


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    pass