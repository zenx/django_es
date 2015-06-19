# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# 3rd. party imports
from sphinx.websupport.storage import StorageBackend
from sphinx.websupport.errors import DocumentNotFoundError

# app imports
from .models import Node


class ORMStorage(StorageBackend):
    """
    """

    def __init__(self):
        pass

    def pre_build(self):
        pass

    def has_node(self, id):
        try:
            node = Node.objects.get(pk=id)
        except Node.DoesNotExist:
            node = None
        return bool(node)

    def add_node(self, id, document, source):
        node = Node(pk=id, document=document, source=source)
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
            node = Node.objects.get(pk=node_id)
        except Node.DoesNotExist:
            raise DocumentNotFoundError()
        return {'source': node.source,
                'comments': []}

    def process_vote(self, comment_id, username, value):
        pass

    def update_username(self, old_username, new_username):
        pass

    def accept_comment(self, comment_id):
        pass

