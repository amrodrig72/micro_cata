import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='micro_cata',
    version='0.0.1',
    author='Andres Rodriguez and Adiel Perez',
    author_email='amrodrig@caltech.edu and afperez@caltech.edu',
    description='Package that will help us analyze microtuble catastrophe data.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    install_requires=["numpy","pandas", "bokeh>=1.4.0", "warnings", "bebi103", "math", "scipy", "numba", "tqdm", "iqplot", "colorcet"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)