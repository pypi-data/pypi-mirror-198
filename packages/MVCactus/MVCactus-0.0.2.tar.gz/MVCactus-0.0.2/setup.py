from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'MVCactus is a lightweight, open-source web framework for building small web applications in Python.'

# Setting up
setup(
    name="MVCactus",
    version=VERSION,
    author="Dekel Cohen",
    author_email="<dcohen52@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=['Jinja2'],
    keywords=['python', 'web', 'framework', 'desktop', 'html', 'javascript', 'styles', 'js', 'API', 'microservices',
              'REST'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
