import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="aiossechat",
  version="0.0.2",
  author="92MING",
  author_email="yashin.sd123@yahoo.com.hk",
  description="A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/92MING/aiossechat",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)