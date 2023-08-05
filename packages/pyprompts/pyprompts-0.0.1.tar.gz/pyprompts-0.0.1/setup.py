from setuptools import setup, find_packages

setup(
    name='pyprompts',
    version='0.0.1',
    license='MIT',
    description='A library for loading, transforming, managing and downloading LLM and diffusion prompts and prompt datasets',
    author='Ian Timmis',
    author_email='ianmtimmis@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/PyPrompts/PyPrompts',
    install_requires=[
        'PyYAML',
    ],
)
