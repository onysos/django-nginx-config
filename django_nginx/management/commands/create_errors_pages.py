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
from django.template.loader import get_template
from django.template.context import RequestContext
from django.http.request import HttpRequest
from django.template.base import TemplateDoesNotExist
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

            dest = os.path.join(output, "error{code}.html".format(code=code))
            try:
                t = get_template("{code}.html".format(code=code))
                r = HttpRequest()
                res = t.render(RequestContext(r))
                # with codecs.open(dest, "w", encoding="utf-8") as f:
                with open(dest, "wb") as f:
                    f.write(res.encode("utf-8"))
                self.stdout.write("fichier %s créé" % dest)
            except TemplateDoesNotExist:
                self.stderr.write("pas de template %s.html" % code)








def main():
    pass

if __name__ == "__main__":
    main()
