#!/usr/bin/env python3

# PIP3 modules
from setuptools import setup


setup(
	name='oasa',
	version='0.15pre1',
	description="OASA is a free cheminformatics library written in Python",
	long_description="OASA is a free cheminformatics library written in Python",
	author="Beda Kosata",
	author_email="beda@zirael.org",
	maintainer="Reinis Danne",
	maintainer_email="rei4dan@gmail.com",
	url="http://bkchem.zirael.org/oasa_en.html",
	license="GPL-3.0-or-later",
	platforms=["Unix", "Windows", "other OSes able to run Python"],
	packages=['oasa', 'oasa.graph'],
	package_data={
		'oasa': [
			'*.txt',
			'*.txt.gz',
			'*.db',
		],
	},
	python_requires=">=3.10",
)
