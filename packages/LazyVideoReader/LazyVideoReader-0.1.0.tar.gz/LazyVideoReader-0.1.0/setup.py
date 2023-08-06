from setuptools import setup, find_packages


VERSION = "0.1.0"
DESCRIPTION = (
    "A lazy video loader for working with a huge amount of video frame as numpy array"
)
LONG_DESCRIPTION = "A package that allows to lazely load chunk of video in ndarray format for processing in computer vision"

# Setting up
setup(
    name="LazyVideoReader",
    version=VERSION,
    author="Slownite (Samuel Diop)",
    author_email="<snfdiop@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["opencv-python", "numpy"],
    keywords=["python", "video", "frames extraction", "lazy loading", "generator"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
