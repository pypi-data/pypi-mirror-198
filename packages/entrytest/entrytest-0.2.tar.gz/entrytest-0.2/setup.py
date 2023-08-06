import setuptools

setuptools.setup(
        name="entrytest",
    version="0.2",
    license='MIT',
    author="FacerAin",
    author_email="syw5141@gmail.com",
    description="test pip entry point",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    entry_points={"console_scripts": ["entrytest = app:main"]},
    scripts=["bin/entrytest.cmd"]
)