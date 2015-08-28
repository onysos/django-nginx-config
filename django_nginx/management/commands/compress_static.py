# -*- coding: utf-8 -*-
"""
Created on 24 juil. 2013

@author: darius
"""
from __future__ import unicode_literals
import logging
import glob
from django.conf import settings
import os
from django.core.management.base import BaseCommand
import gzip
from optparse import make_option
import itertools
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    args = ''
    help = 'compress all static files to allow nginx to serve them already gziped'
    option_list = BaseCommand.option_list + (
        make_option('--clear',
            action='store_true',
            dest='clear',
            default=False,
            help='clear all gziped file instead of creating them.'),
        make_option('--extra_path',
            action='append',
            dest='path',
            default=[],
            help='compress all js/css files in this dirrectory too (can be repeated)'),
        )

    def handle(self, *args, **options):
        logger.debug("starting compress of %s" % settings.STATIC_ROOT)
        if not os.access(settings.STATIC_ROOT, os.W_OK):
            logger.warning("STATIC_ROOT is not writable or don't exists")
        for dirpath in itertools.chain([settings.STATIC_ROOT], options["path"]):
            for root, _, files in os.walk(dirpath):
                logger.debug("in dir : %s" % root)
                for filename in files:
                    filename = filename.decode("utf-8")
                    try:
                        fullpath = os.path.join(root, filename)
                        if not options["clear"]:
                            if filename.endswith(".css") or filename.endswith(".js"):
                                try:
                                    with open(fullpath) as file_in, gzip.open("%s.gz" % fullpath, "wb") as file_gz:
                                        file_gz.write(file_in.read())
                                        logger.debug("compressing %s" % fullpath)
                                except OSError, e:
                                    logger.warning("impossible to compress %s : %s " % (filename, e))
                        else:
                            if filename.endswith(".gz"):
                                try:
                                    logger.debug("removing %s" % filename)
                                    os.remove(fullpath)
                                except:
                                    logger.warning("impossible to delete gziped file %s" % fullpath)
                    except:
                        msg = "error durring compressing file %r" % filename
                        logger.exception(msg)
                        self.stderr.write(msg)
                        raise

