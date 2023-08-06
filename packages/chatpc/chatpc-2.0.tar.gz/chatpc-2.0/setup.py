from setuptools import setup, find_packages

setup(
    name='chatpc',
    version='2.0',
    description='A conversational bot module',
    author='Braden Spears',
    author_email='obamaslayer0909@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pyyaml'
    ],
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
