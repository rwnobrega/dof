from setuptools import setup, find_packages

_long_description = '''
**dof** is a minimalist document finder inspired by [Xfce4 Application Finder](http://docs.xfce.org/xfce/xfce4-appfinder/start). It is written in [Python3](http://www.python.org/) and uses [PyQt5](http://www.riverbankcomputing.com/software/pyqt/). Currently Linux only.
'''

setup(
    name='dof',
    version='0.0.0',
    description='A minimalist document finder inspired by Xfce4 Application Finder.',
    long_description=_long_description,
    url='https://github.com/rwnobrega/dof/',
    author='Roberto W. Nobrega',
    author_email='rwnobrega@gmail.com',
    license='GPL',
    project_urls={
        'Source': 'https://github.com/rwnobrega/dof/',
    },
    packages=find_packages('dof'),
    scripts=['dof/dof'],
    install_requires=['pyqt5', 'braceexpand'],
    python_requires='>=3.6',
)
