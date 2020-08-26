from django.contrib import admin
from django.db import models
from django.forms import widgets

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tegs, Relationship

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
    model = Relationship
    formset = RelationshipInlineFormset
    # radio_fields = {'main_teg': admin.VERTICAL}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    inlines = [
        RelationshipInline,
    ]


@admin.register(Tegs)
class TegsAdmin(admin.ModelAdmin):

    inlines = [
        RelationshipInline,
    ]
    # radio_fields = {'Tegs.relationship_set.main_teg': admin.VERTICAL}
