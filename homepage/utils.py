# __encoding=utf-8 __

import re
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def get_page(objs, page):
    """
    分页
    """
    paginator = Paginator(objs, settings.PER_PAGE)

    try:
        ret = paginator.page(page)
    except (EmptyPage, InvalidPage):
        ret = paginator.page(paginator.num_pages)

    return ret


def is_slug(slug):
    """
    is slug
    """
    return re.match(r'^[a-z0-9A-Z_\-]+$', slug)
