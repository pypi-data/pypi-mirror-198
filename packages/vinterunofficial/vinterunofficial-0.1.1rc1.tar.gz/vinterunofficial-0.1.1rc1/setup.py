from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(
	name="vinterunofficial",
	version="0.1.1rc1",
	description="This is a unofficial wrapper for Vinter.co API",
	long_description=long_description,
	long_description_content_type='text/markdown',
	install_requires=["httpx==0.23.3"],
	author="Rahul Mistri",
	author_email="rahulmistri1997@gmail.com",
	packages=find_packages(),
)
