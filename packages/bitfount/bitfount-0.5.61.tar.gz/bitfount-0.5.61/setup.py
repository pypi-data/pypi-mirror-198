"""This file enables the github repo to be packaged into a wheel using `setuptools`."""
import runpy
from typing import Dict, List

from setuptools import find_packages, setup

# Import version information into current namespace
file_globals = runpy.run_path("bitfount/__version__.py")

# Get direct constraints
with open("requirements/constraints-direct.txt") as f:
    direct_constraints = f.read().splitlines()

# Get security constraints
with open("requirements/constraints-security.txt") as f:
    security_constraints = f.read().splitlines()

# Get compatibility constraints
with open("requirements/constraints-compatibility.txt") as f:
    compat_constraints = f.read().splitlines()

# Get install requirements
with open("requirements/requirements.in") as f:
    install_reqs = f.read().splitlines()

# Add the security and compatibility constraints to the main requirements
# and get rid of unnecessary lines.
install_reqs.extend(direct_constraints)
install_reqs.extend(security_constraints)
install_reqs.extend(compat_constraints)
install_reqs = [
    line.split("#")[0].strip()
    for line in install_reqs
    if not line.startswith(("#", "-c", "-r")) and line != ""
]

# Find duplicated package names and their version constraints. These must be
# combined into a single line.
# Explicitly no '==' because '~=' should be used instead. The order of the
# operations is important because we want to check for "<=" before "< etc.
operations = ["<=", ">=", "<", ">", "~=", "!="]
all_package_names: Dict[str, str] = {}
duplicated_package_names: Dict[str, List[str]] = {}
for line in install_reqs:
    # Raise an error if the line doesn't contain any of the operations
    if not any(op in line for op in operations):
        raise ValueError(f"Unknown version constraint: {line}")
    # Skip platform-specific requirements
    if "platform_system" in line:
        # TODO: [BIT-2637] This should be removed once 'platform_system' is
        # removed from the requirements files.
        continue
    for op in operations:
        if op in line:
            pkg_split = line.split(op)
            # The line should just contain the package name and the version, split
            # by the operation
            if len(pkg_split) != 2:
                raise ValueError(f"Unknown version constraint: {line}")
            name, version = pkg_split
            # Add the package name and version constraint to all package names
            # if it's not already there. If it is, add it to the duplicated
            # package names (appending the version constraint if it already exists)
            if name not in all_package_names:
                all_package_names[name] = f"{op}{version}"
            elif name in duplicated_package_names:
                versions = duplicated_package_names[name]
                versions.append(f"{op}{version}")
                duplicated_package_names[name] = versions
            else:
                duplicated_package_names[name] = [
                    f"{op}{version}",
                    all_package_names[name],
                ]
            # Break out of the inner loop because we've found the operation
            break

# Remove the duplicated package names from the install requirements
install_reqs = [
    i for i in install_reqs if not any(pkg in i for pkg in duplicated_package_names)
]
# Add the package names we just removed to the install requirements but with
# the version constraints combined.
for i, values in duplicated_package_names.items():
    install_reqs.append(f"{i}{','.join(values)}")

# Sort the requirements
install_reqs = list(sorted(install_reqs))

# Get tutorial requirements
with open("requirements/requirements-tutorial.txt") as f:
    tutorial_reqs = f.read().splitlines()

# Get dp requirements
with open("requirements/requirements-dp.txt") as f:
    dp_reqs = f.read().splitlines()

# Get testing requirements
with open("requirements/requirements-test.txt") as f:
    tests_reqs = f.read().splitlines()

# Get dev requirements
with open("requirements/requirements-dev.txt") as f:
    dev_reqs = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    author=file_globals["__author__"],
    author_email=file_globals["__author_email__"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description=file_globals["__description__"],
    entry_points={
        "console_scripts": [
            "bitfount = scripts.script_runner:main",
        ]
    },
    extras_require={
        "tests": tests_reqs,
        "dev": dev_reqs,
        "tutorials": tutorial_reqs,
        "dp": dp_reqs,
    },
    install_requires=install_reqs,
    keywords=["federated learning", "privacy", "AI", "machine learning"],
    license="Apache License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name=file_globals["__title__"],
    packages=find_packages(),
    package_data={"bitfount": ["py.typed"]},
    project_urls={
        "Documentation": "https://docs.bitfount.com/",
        "Homepage": "https://bitfount.com",
        "Source Code": "https://github.com/bitfount/bitfount/",
        "Hub": "https://hub.bitfount.com",
    },
    python_requires=">=3.8,<3.10,!=3.9.7",
    url=file_globals["__url__"],
    version=file_globals["__version__"],
)
