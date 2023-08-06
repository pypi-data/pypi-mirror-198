import setuptools

setuptools.setup(
    name="pramod_test_utils",
    version="0.0.63",
    author="Utils Team",
    description="Reusable global utils",
    packages=setuptools.find_packages(),
    install_requires=[
        'PyJWT==1.7.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
