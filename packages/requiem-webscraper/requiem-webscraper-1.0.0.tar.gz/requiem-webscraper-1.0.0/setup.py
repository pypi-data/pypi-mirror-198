from setuptools import setup, find_packages

setup(
    name='requiem-webscraper',
    version='1.0.0',
    description='A web scraper built only using the requests library',
    author='Atharv Kulkarni',
    author_email='atharv4study@gmail.com',
    url='https://github.com/atharv4git/Requiem',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'requiem=requiem.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
