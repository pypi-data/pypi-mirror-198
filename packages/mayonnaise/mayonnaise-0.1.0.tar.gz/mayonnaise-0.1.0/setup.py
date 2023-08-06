from setuptools import setup

with open('README.md', 'r', encoding = 'utf-8') as readme:
    long_description = readme.read()

setup(
    name = 'mayonnaise',
    version = '0.1.0',
    description = 'Youtube cli interface for downloading media',
    url = 'https://github.com/zeionara/maya',
    author = 'Zeio Nara',
    author_email = 'zeionara@gmail.com',
    packages = [
        'maya'
    ],
    install_requires = [
        'pytube @ git+https://github.com/duvu/pytube',
        'click',
        'tqdm'
    ],
    classifiers = [
        'Programming Language :: Python :: 3.10'
    ],
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)
