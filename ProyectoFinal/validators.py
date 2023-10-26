import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _



class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("La contraseña debe tener al menos 1 mayúscula"),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe tener al menos 1 mayúscula"
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("La password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("La contraseña debe tener al menos 1 símbolo: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe tener al menos 1 símbolo: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
    
class DigitValidator(object):
    def validate(self, password, user=None):
        if not re.findall(r'[0-9]', password):
            raise ValidationError(
                _("La contraseña debe tener al menos 1 número:"),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe tener al menos 1 número: "
            
        )
            # Al menos un dígito
        # if not re.search(r'[0-9]', password):
        #     raise ValidationError(
        #         _("La contraseña debe contener al menos un dígito."),
        #         code="password_no_digit",
        #     )
