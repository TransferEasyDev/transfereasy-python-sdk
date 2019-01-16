# -*- coding: utf-8 -*-
import os


def test_api():
    for root, dirs, files in os.walk(".", topdown=False):
        if 'examples/api' in root:
            for name in files:
                if '__init__' not in name:
                    print '>>>>>>>>>>>>>>>>>>>>'
                    print ('python {file}'.format(file=os.path.join(root, name)))
                    os.system('python {file}'.format(file=os.path.join(root, name)))
