import setuptools


setuptools.setup(
    name="anachem",
    version="0.12",
    author="yangtao",
    description="errors and statistical treatment of analytical data",
    packages=setuptools.find_packages(),
    requires=["numpy", "pandas"],

)
