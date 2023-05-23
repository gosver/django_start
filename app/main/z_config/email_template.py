from django.conf import settings as my_settings
from djoser import email
from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from djoser.conf import settings


class ActivationEmail(email.ActivationEmail):
    template_dir = my_settings.TEMPLATES[0]['DIRS'][0]
    template_name = template_dir+'/email/activation.html'
    domain = my_settings.BASE_DOMAIN

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)

        # change to main domain
        context["domain"] = self.domain

        return context
