# -*- encoding: utf-8 -*-
from django import template
from newsletter.forms import SuscriptorForm

register = template.Library()


@register.assignment_tag
def get_newsletter_subscriptor_form():
    return SuscriptorForm()
