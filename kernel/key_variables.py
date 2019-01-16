# -*- coding: utf-8 -*-


class KeyVariables(object):
    def __init__(self, **kwargs):
        self.params = kwargs.get('params')
        self.url = kwargs.get('url')
        self.method = kwargs.get('method')
        self.files = kwargs.get('files')
