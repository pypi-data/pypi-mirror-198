from setuptools import setup

description_long = ""

with open('README.md','r') as readme:
    content = readme.readlines()
    description_long = ''.join(content)    

print(description_long)


setup(
    name='pypleski',
    version='0.0.7',    
    description='Simplified API to access the PLESK XML API',    
    url='https://codingcow.de/pypleski',
    author='Uli Toll',
    author_email='pypleski@codingcow.de',
    packages=['pypleski'],
    py_modules=[
    'pypleski.core',
    'pypleski.customer',
    'pypleski.database',
    'pypleski.nodejs',
    'pypleski.ip',
    'pypleski.ftp_user',
    'pypleski.git',
    'pypleski.db_server',
    'pypleski.dns',
    'pypleski.extension',
    'pypleski.session',
    'pypleski.secret_key',
    'pypleski.mail',
    'pypleski.webspace',

    ],
    install_requires=['xmltodict',                                           
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',  
        'Operating System :: POSIX :: Linux',   
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],    
    long_description=description_long,
    long_description_content_type="text/markdown",
    
)

