import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eeg-sleep-analysis",
    version="1.0.4",
    author="Isaac J. Perron",
    author_email="ijperron@gmail.com",
    description="Package to analyze EEG-scored sleep",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ijperron/EEGAnalysis",
    packages=["code", "full_run"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "eeg-sleep-analysis=EEGAnalysis.full_run.run_main:main"
        ]
    },
)