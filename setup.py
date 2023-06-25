from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='micropython-uaioweb',
    version='0.0.3',
    description='Minimal asyncio web server for HTTP and Websocket.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/damiencorpataux/micropython-uaioweb',
    keywords='micropython, python, web, server, http, websocket, asyncio, uasyncio, lightweight, simple, minimalistic',
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: Implementation :: MicroPython",
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
    ],
    dependency_links=[
        'https://github.com/wybiral/micropython-aioweb'
    ],
    author='Davy Wybiral, Damien Corpataux (fork)',
    author_email='not-disclosed@example.com, d@mien.ch',
    license='MIT',
    packages=['uaioweb'],
    zip_safe=False
)
