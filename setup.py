import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-datefilter',
    version='2.0.0a',
    license='MIT',
    author='Oriol Closa',
    author_email='oriol@5monkeys.se',
    description='Date filter for Django admin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/oriolclosa/django-daterfilter/tree/master',
    project_urls={
        'Source': 'https://github.com/oriolclosa/django-datefilter/',
        'Tracker': 'https://github.com/oriolclosa/django-datefilter/issues'
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
