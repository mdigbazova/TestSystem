from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from multiselectfield import MultiSelectField

#----------------------

# Create your models here.
STATE_CHOICES = (
    (1, 'TO BE DONE'),
    (2, 'PROCESSING'),
    (3, 'RESEARCHING'),
    (4, 'DONE!'),
    (5, 'FAILED'),
    (6, 'FIXED'),
)

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Todo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    state = MultiSelectField(choices=STATE_CHOICES, default=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    code = models.TextField(blank=True)
    linenos = models.BooleanField(default=True)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    def __str__(self):
        """A string representation of the model."""
        return f'{self.title} - on the state of {self.state}. Language {self.language}'


"""
Requests and Responses
Currently our API has no restrictions on who can edit or delete todos&code. In this section we will make sure that:

Todos are always associated with a creator
Only authenticated users may create todos
Only the creator of a todo may update or delete it
Unauthenticated requests should have full read-only access
"""
