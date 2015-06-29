# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# python imports
import re

# django imports
from django.utils.html import strip_tags

# 3rd. party imports
from sphinx.websupport import WebSupport as BaseSupport


class WebSupport(BaseSupport):

    def get_document(self, docname, username='', moderator=False):
        result = super(WebSupport, self).get_document(docname, username,
                                                      moderator)
        return result

    def get_search_results(self, q):
        """Perform a search for the query `q`, and create a set
        of search results. Then render the search results as html and
        return a context dict like the one created by
        :meth:`get_document`::

            document = support.get_search_results(q)

        :param q: the search query
        """
        results = self.search.query(q)
        results = self._process_search_results(results, q)
        return results

    def _process_search_results(self, results, search_term):

        class Result:
            pass

        terms = '|'.join(search_term.split())
        regexp = re.compile(r'(?P<term>{})'.format(terms), re.IGNORECASE)
        for href, caption, context  in results:
            result = Result()
            result.href = href
            result.caption = strip_tags(unicode(caption, 'utf-8'))
            result.context = regexp.sub('<em>\g<term></em>', context)
            yield result

