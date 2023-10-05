# type: ignore

import subprocess

import setuptools

with open('README.md', encoding="utf8") as fh:
    long_description = fh.read().replace('](', '](https://raw.githubusercontent.com/FarisHijazi/PrivateGitHubCopilot/master/')
with open('requirements.txt', encoding="utf8") as fh:
    rqeuirements = fh.readlines()

version = subprocess.Popen('git describe --abbrev=0 --tags', shell=True, stdout=subprocess.PIPE).stdout.read().decode().strip().lstrip('v')

setuptools.setup(
    name='PrivateGitHubCopilot',
    version=version,
    description='An OSS drop-in replacement for GitHub Copilot using oobabooga',
    long_description=long_description,
    url='https://github.com/FarisHijazi/PrivateGitHubCopilot',
    author='Faris Hijazi',
    author_email='theefaris@gmail.com',
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=rqeuirements,
    keywords='',
    entry_points={
        'console_scripts': [
            'PrivateGitHubCopilot=middleware:main',
        ]
    },
)