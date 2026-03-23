from i18nfield.forms import I18nModelForm

from .models import SingleSignOnSettings


class SignleSignOnSettingsForm(I18nModelForm):

    def __init__(self, *args, event=None, **kwargs):
        self.instance, _ = SingleSignOnSettings.objects.get_or_create(event=event)
        super().__init__(*args, **kwargs, instance=self.instance, locales=event.locales)

    class Meta:
        model = SingleSignOnSettings
        fields = ("some_setting",)
        widgets = {}
