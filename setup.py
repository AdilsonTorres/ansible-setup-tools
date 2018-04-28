from setuptools import setup

setup(
    name='ansible_tools',
    version='0.1',
    py_modules=['ansible_tools'],
    install_requires=[
        'Click',
        'ansible',
    ],
    entry_points='''
        [console_scripts]
        ansible_tools=ansible_tools:main
    ''',
)
