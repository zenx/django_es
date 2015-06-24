# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django imports
from django.utils.translation import ugettext_lazy as _

# 3rd. party imports
from sphinx.websupport import WebSupport as BaseSupport


class WebSupport(BaseSupport):
    def get_search_results(self, q):
        """Perform a search for the query `q`, and create a set
        of search results. Then render the search results as html and
        return a context dict like the one created by
        :meth:`get_document`::

            document = support.get_search_results(q)

        :param q: the search query
        """
        results = self.search.query(q)
        ctx = {
            'q': q,
            'search_performed': True,
            'search_results': results,
            'docroot': '../{}/'.format(self.docroot),  # XXX
            '_': _,
        }
        document = {
            'body': self.results_template.render(ctx),
            'title': 'Search Results',
            'sidebar': '',
            'relbar': ''
        }
        return document


