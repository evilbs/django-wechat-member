import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-wechat-member',
    version = '0.2.3',
    packages = ['wechat_member'],
    install_requires = ['django-wechat-base>=0.4.4'],
    include_package_data = True,
    license = 'BSD License',
    description = 'add city to member list, change avatar_url name',
    long_description = README,
    url = 'https://github.com/ChanMo/django-wechat-member',
    author = 'ChanMo',
    author_email = 'chen.orange@aliyun.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
