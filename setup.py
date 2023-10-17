import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name='cleverbot-free',
    version='1.0.0',
    description='An Unofficial Cleverbot to Chat  for free,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    author='moezilla',
    author_email='pranavajay74@gmail.com',
    url='https://github.com/moezilla/cleverbot-free.git',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["hashlib", "requests", "time"],
    python_requires='>=3.6'
)
