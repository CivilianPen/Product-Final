
from django.db.models import Count

from .models import *

class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        return context