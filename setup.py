from setuptools import setup


setup(
    name="libeuler",
    packages=["libeuler"],
    package_dir={"libeuler": "libeuler"},  # directory "." contains package "libeuler"
    use_scm_version=False,
    description="Common functions for Project Euler solutions.",
    author="Iñaki Silanes Cristóbal",
    author_email="isilanes@gmail.com",
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
