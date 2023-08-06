from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

package_data = {
    '': ['*.png', '*.txt', '*.md', '*.py'],
    'Scripts': ['*.py'],
}

with open('README.md', 'r') as f:
    long_desctiption = f.read()

setup(
    name='BashMate',
    version='0.1',
    author='Kushagra Agarwal',
    author_email='kushagra.agarwal.2709@gmail.com',
    description='Developer focused Command Line Tools',
    long_description=long_desctiption,
    long_description_content_type='text/markdown',
    package_data= package_data,
    licence_files = ['LICENSE.txt'],
    scripts=['Scripts/workman.py', 'Scripts/wizard.py', 'post_install.py'],

    install_requires=['colorama', 'openai'],

    entry_points={
        'console_scripts': [
            'wm = workman:main',
            'wiz = wizard:main',
            'bashmate_config = post_install:post_install'
        ],
    }
)