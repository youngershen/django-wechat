# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    :
# AUTHOR       : younger shen

from setuptools import setup, find_packages

version = '0.1a1'

setup(name='django-wechat',
      version=version,
      description="apis for you can use wechat in django",
      long_description="""\
      apis for you can use wechat in django

      """,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   ],
      keywords='django-ueditor-plugin, django, ueditor',
      author='younger shen',
      author_email='younger.x.shen@gmail.com',
      url='https://github.com/youngershen/django-wechat',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'Django >= 1.6',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
