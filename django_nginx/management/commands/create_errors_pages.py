#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 15 juil. 2014

@author: darius
"""
from __future__ import unicode_literals
import logging
from django.test.client import Client
import os
import codecs
logger = logging.getLogger(__name__)
from django.core.management.base import BaseCommand
from optparse import make_option


class Command(BaseCommand):
    args = 'error_code'
    help = 'create all 500 errors customized by the website.'
    option_list = BaseCommand.option_list + (
        make_option('-o', "--output",
            action='store',
            dest='output',
            default=None,
            help='dossier de destination des fichiers généré'),

        )
    def handle(self, *args, **options):
        client = Client()
        url = "/error/{code}.html"
        output = options["output"] or os.getcwd()
        for code in args:
            url_res = url.format(code=code)
            r = client.get(url_res)
            if r.status_code == 200:
                dest = os.path.join(output, "error{code}.html".format(code=code))
                # with codecs.open(dest, "w", encoding="utf-8") as f:
                with open(dest, "w") as f:
                    f.write(r.content)
                self.stdout.write("fichier %s créé" % dest)
            else:
                self.stderr.write("erreur %s sur le code %s (%s)" % (r.status_code, code, url_res))








def main():
    pass

if __name__ == "__main__":
    main()
