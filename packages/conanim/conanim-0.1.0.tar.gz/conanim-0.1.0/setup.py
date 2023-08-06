from setuptools import setup, find_packages

setup(
    name='conanim',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mypackage=mypackage.__main__:main'
        ]
    },
    author='breadlol64',
    author_email='breadlol64@gmail.com',
    description='A Python library for creating animation in console.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',
    # project_urls={
    #     'Bug Tracker': 'https://github.com/yourusername/mypackage/issues',
    #     'Documentation': 'https://yourusername.github.io/mypackage',
    #     'Source Code': 'https://github.com/yourusername/mypackage'
    # },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='console animation'
)
