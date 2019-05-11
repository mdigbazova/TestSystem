from django.db import models

from pygments import highlight # for highlighted code
from pygments.formatters.html import HtmlFormatter # for HTML representation of code
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

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
    #owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE, null=True) # related_name creates an reverse relationship
    highlighted = models.TextField(blank=True, default='')

    """
    Requests and Responses
    Currently our API has no restrictions on who can edit or delete todos&code. In this section we will make sure that:

    Todos are always associated with a creator
    Only authenticated users may create todos
    Only the creator of a todo may update or delete it
    Unauthenticated requests should have full read-only access
    """

    class Meta:
        ordering = ('state',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name (self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter (style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight (self.code, lexer, formatter)
        super(Todo, self).save(*args, **kwargs)


    def __str__(self):
        """A string representation of the model."""
        return f'{self.title} - on the state of {self.state}. Language {self.language}'




