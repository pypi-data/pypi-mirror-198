from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    reqs = fh.read().splitlines()


def local_scheme(version):
    return ""


def version_scheme(version):
    return version.tag.base_version


setup(
    name="ql",
    author="Louis Maddox",
    author_email="louismmx@gmail.com",
    description="spin.systems generator and driver",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spin-systems/quill/",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
    include_package_data=True,
    use_scm_version={
        "write_to": "version.py",
        "version_scheme": version_scheme,
        "local_scheme": local_scheme,
    },
    setup_requires=["setuptools_scm"],
    entry_points={
        "console_scripts": [
            "ql = quill.fold.cli:standup_cli",
            "cyl = quill.fold.cli:cyl_cli",
        ],
    },
    install_requires=reqs,
    python_requires=">=3",
)
