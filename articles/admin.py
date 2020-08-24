from django.contrib import admin
from django.db import models
from django.forms import widgets

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tegs

#admin
#admin

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for item in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if item.cleaned_data:
                continue
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            else:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Tegs.scopes.through
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    inlines = [
        RelationshipInline,
    ]
    #
    # def get_formsets_with_inlines(self, request, obj=None):
    #     for inline in self.get_inline_instances(request, obj):
    #         # hide MyInline in the add view
    #         if isinstance(inline, RelationshipInline) and obj is None:
    #             continue
    #         yield inline.get_formset(request, obj), inline

    # formfield_overrides = {
    #     models.TextField: {'text': widgets.TextInput},
    # }

@admin.register(Tegs)
class TegsAdmin(admin.ModelAdmin):

    inlines = [
        RelationshipInline,
    ]
    #
    # def get_formsets_with_inlines(self, request, obj=None):
    #     for inline in self.get_inline_instances(request, obj):
    #         # hide MyInline in the add view
    #         if isinstance(inline, RelationshipInline) and obj is None:
    #             continue
    #         yield inline.get_formset(request, obj), inline

    # formfield_overrides = {
    #     models.CharField: {'Tegs.topic': widgets.RadioSelect},
    # }

