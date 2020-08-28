from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tegs, Relationship

#admin
#admin

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for item in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if item.cleaned_data:
               if item.cleaned_data['main_teg']:
                    count += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if count != 1:
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 3
    formset = RelationshipInlineFormset


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
