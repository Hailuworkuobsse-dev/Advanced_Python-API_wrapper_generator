from setuptools import setup, find_packages

setup(
    name='api_wrapper_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests', 'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'generate-api-wrapper = api_wrapper_generator.main:main',
        ],
    },
)