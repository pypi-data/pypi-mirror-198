from setuptools import setup

setup(
    name='update_changelog',
    version='0.0.1',
    py_modules=['main'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'update_changelog=main:main'
        ]
    }
)
