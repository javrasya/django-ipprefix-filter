from setuptools import setup, find_packages

setup(
    name='django-ip-filter',
    version='0.1.2',
    description='Allow to filter by a prefix fields as ip and mask as seperated.',
    long_description=open('README').read(-1),
    author='Ahmet DAL',
    author_email='ceahmetdal@gmail.com',
    url='https://github.com/javrasya/django-ipprefix-filter.git',
    keywords=[
        'django admin',
        'django ipprefix filter',
    ],
    install_requires=[
        "Django",
        "South",
    ],
    packages=['ip_filter'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Environment :: Web Environment',
        'Operating System :: OS Independent'
    ],
    license='License :: OSI Approved :: BSD License',
)
