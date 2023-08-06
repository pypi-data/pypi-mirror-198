from setuptools import setup

setup(
    name='apitest_harness',
    version=0.1,
    description='API Testing Framework',
    author='Bytes Arena Solution Pvt Ltd',
    packages=['apitest_harness'],
    install_requires = [
    'numpy',
    'pandas',
    'requests',
    'deepdiff',
    'openpyxl',
    'urllib3',
    'XlsxWriter'],
    include_package_data=True,
    zip_safe=False)
