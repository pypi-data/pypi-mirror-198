from setuptools import setup, find_namespace_packages

setup(
    name='PADAWAN_help',
    version='1.0.6',
    description='Python Core project code',
    readme='README.md',
    url='https://github.com/MagdaVic/PADAWAN_helper',
    author='PADAWAN TEAM',
    author_email='',
    license='MIT',
    packages=find_namespace_packages(),
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=['colorama', 'prompt-toolkit==2.0.10'],
    entry_points={'console_scripts': ['PADAWAN=PADAWAN_helper.menu:main']})