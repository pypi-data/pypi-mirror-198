
import subprocess
from pathlib import Path


from setuptools import setup

__version__ = "0.0.1"
HERE = Path(__file__).resolve().parent

# install planner binaries
subprocess.check_call(
    ["./build.py"], cwd=(HERE / "src/state_space_generator/scorpion")
)

def compute_files(subdir):
    print(subdir)
    return [str(p.resolve()) for p in subdir.rglob('*')]

# Add Fast-Downward files to be copied
files = []
files.append(str(Path("src/state_space_generator/scorpion/fast-downward.py").resolve()))
files.extend(compute_files(Path("src/state_space_generator/scorpion/builds/release/bin")))
files.extend(compute_files(Path("src/state_space_generator/scorpion/driver")))

print(files)
# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
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
    package_data={'': files},
    include_package_data=True,
    zip_safe=False,
)
