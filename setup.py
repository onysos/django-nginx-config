from distutils.core import setup
import os


setup(name='django-nginx-config',
      version='0.2',
      description='an easy to use nginx config generator for django project',
      author='Darius BERNARD',
      author_email='contact@onysos.fr',
      url='https://github.com/onysos/django-nginx-config',
      download_url='https://github.com/onysos/django-nginx-config/archive/master.zip',
      package_dir={'django_nginx': 'django_nginx'},
      packages=["django_nginx"],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )
