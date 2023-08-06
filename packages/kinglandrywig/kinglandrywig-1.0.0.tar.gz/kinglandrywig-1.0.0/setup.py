from setuptools import setup, find_packages

setup(
    name='kinglandrywig',
    version='1.0.0',
    author='Landry M. King',
    author_email='landrymk@yourdomain.com',
    description='Custom autocomplete widget for Tkinter',
    packages=find_packages(),
    install_requires=[
        'tkinter'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
