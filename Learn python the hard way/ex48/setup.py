try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Praveen Balasundaram',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)