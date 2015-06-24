# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# 3rd. party imports
from sphinx.websupport.storage import StorageBackend
from sphinx.websupport.errors import DocumentNotFoundError


class ORMStorage(StorageBackend):
    """
    """

    def __init__(self, manager):
        self._manager = manager

    def pre_build(self):
        pass

    def has_node(self, id):
        try:
            node = self._manager.get(pk=id)
        except self._manager.model.DoesNotExist:
            node = None
        return bool(node)

    def add_node(self, id, document, source):
        node = self._manager.model(pk=id, document=document, source=source)
        node.save()

    def post_build(self):
        pass

    def add_comment(self, text, displayed, username, time,
                    proposal, node_id, parent_id, moderator):
        pass

    def delete_comment(self, comment_id, username, moderator):
        pass

    def get_metadata(self, docname, moderator):
        pass

    def get_data(self, node_id, username=None, moderator=False):
        try:
            node = self._manager.get(pk=node_id)
        except self._manager.model.DoesNotExist:
            raise DocumentNotFoundError()
        return {'source': node.source,
                'comments': []}

    def process_vote(self, comment_id, username, value):
        pass

    def update_username(self, old_username, new_username):
        pass

    def accept_comment(self, comment_id):
        pass

