import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkinterdnd2-universal",
    version="1.7.3",
    author="petasis\\pmgagne\\eliav2\\blacklein",
    description="TkinterDnD2 is a python wrapper for George Petasis'' tkDnD Tk extension version 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blacklein/tkinterdnd2-universal",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        # Include tkdnd extension files.
        "tkinterdnd2": ["tkdnd/linux-x64/*.*", "tkdnd/linux-arm64/*.*", "tkdnd/osx-x64/*.*", "tkdnd/osx-arm64/*.*", "tkdnd/win-x64/*.*", "tkdnd/win-arm64/*.*"],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
