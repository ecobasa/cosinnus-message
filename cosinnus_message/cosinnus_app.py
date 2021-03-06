# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def register():
    # Import here to prevent import side effects
    from django.utils.translation import ugettext_lazy as _

    from cosinnus.core.registries import app_registry, url_registry

    from cosinnus_message.urls import (cosinnus_group_patterns,
        cosinnus_root_patterns)

    app_registry.register('cosinnus_message', 'message', _('Message'))
    url_registry.register('cosinnus_message', cosinnus_root_patterns,
        cosinnus_group_patterns)
