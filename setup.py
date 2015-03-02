try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Rohit Rai',
    'url': 'url',
    'download_url': 'download_url',
    'author_email': 'rohitkrai03@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['grep'],
    'scripts': [],
    'name': 'grep'
}

setup(**config)
