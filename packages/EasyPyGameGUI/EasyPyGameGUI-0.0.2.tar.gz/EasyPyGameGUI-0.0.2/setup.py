from setuptools import setup
from EasyPyGameGUI import PyGameSimpleGUI

setup(
    name='EasyPyGameGUI',
    version='0.0.2',    
    description='PyGame based module allowing for easy in-Pygame GUI',
    url='',
    author='WerronPL',
    author_email='paligaaleksander@gmail.com',
    license='MIT License',
    packages=['EasyPyGameGUI'],
    install_requires=['mpi4py>=3.1.4',
                      'pygame',                     
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.10',        
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)