from distutils.core import setup

from setuptools import find_packages

setup(
	name='mssh',
	version='0.1.1',
	packages=find_packages(),
	url='https://github.com/foofilers/mssh',
	license='GPLv3',
	author='Igor Maculan',
	author_email='n3wtron@gmail.com',
	description='ssh manager',
	keywords=['ssh','manager'],
	install_requires=['PyYAML'],
	scripts=['bin/mssh'],
	include_package_data=True,
	data_files=[
		('completions',['completions/zsh/_mssh']),
		('completions',['completions/bash/mssh'])
	]
)
