from setuptools import setup

setup(
        name='ccw',
        version='0.0.6',
        description='CLI commands for HD wallet operations',
        author='Louis Holbrook',
        author_email='dev@holbrook.no',
        packages=[
            'ccw.runnable',
            'ccw.data',
            ],
        install_requires=[
            'bip_utils==1.4.0',
            ],
        #scripts=[
        #    'scripts/bip39gen',
        #    ],
        url='https://gitlab.com/nolash/cryptocurrency-cli-tools',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Topic :: Utilities',
            ],
        entry_points = {
            'console_scripts': [
                'ccwgen=ccw.runnable.gen:main',
                'ccweth=ccw.runnable.eth:main',
#                'btc=cryptocurrency_cli_tools.runnable.btc:main',
                ],
            },
        include_package_data=True,
        )
        

