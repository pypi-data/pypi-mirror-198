import subprocess
from pathlib import Path

from setuptools import setup
from setuptools.command.install import install


__version__ = "0.0.6"
HERE = Path(__file__).resolve().parent


class CustomInstallCommand(install):
    """Customized setuptools install command - installs the planner first."""
    def run(self):
        install.run(self)
        subprocess.check_call(["./src/state_space_generator/scorpion/build.py"])

setup(
    name="state_space_generator",
    version=__version__,
    license='GNU',
    author="Dominik Drexler, Jendrik Seipp",
    author_email="dominik.drexler@liu.se, jendrik.seipp@liu.se",
    url="https://github.com/drexlerd/state-space-generator",
    description="A tool for state space exploration of PDDL files",
    long_description="",
    packages=['state_space_generator'],
    package_dir={'state_space_generator': 'src/state_space_generator'},
    zip_safe=False,
    cmdclass={
        'install': CustomInstallCommand,
    },
)
