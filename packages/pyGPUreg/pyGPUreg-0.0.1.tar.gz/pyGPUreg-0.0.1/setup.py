from setuptools import setup, find_packages

setup(
    name='pyGPUreg',
    version='0.0.1',
    license='GPLv3',
    author="Mart G.F. Last",
    author_email='m.g.f.last@lumc.nl',
    description='GPU-accelerated image registration.\ngithub.com/bionanopatterning/pyGPUfit',
    packages=find_packages(),
    package_data={'': ['*.glsl']},
    include_package_data=False,
    install_requires=[
        "numpy>=1.24.2",
        "PyOpenGL>=3.1.6",
        "glfw>=2.5.7"
      ],
)