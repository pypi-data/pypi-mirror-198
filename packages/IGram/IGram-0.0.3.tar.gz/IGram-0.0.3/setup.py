from setuptools import setup,find_packages
import os
import codecs

desc_long=''' 
IGram is a Python package that allows you to fetch important information about any Instagram profile using the BeautifulSoup (bs4) and Requests modules. With IGRAM, you can easily retrieve the number of followers, following, and the total number of posts uploaded by any Instagram user.

Using IGram is simple and straightforward. First, you need to install the package using pip or any other package manager. Once installed, you can import the IGRAM package and use its functions to fetch the desired information.

The package provides the following functions:

Followers() - This function returns the number of followers of the corresponding Instagram profile.

Following() - This function returns the number of users that the corresponding Instagram profile is following.

Posts() - This function returns the total number of posts uploaded by the corresponding Instagram profile.

Name() - This function returns the name of corresponding Instagram profile.

Description() - This function returns the Bio-Data of corresponding Instagram profile
'''
setup(
    name="IGram",
    version="0.0.3",
    author="Vaibhav Pandey",
    author_email="pandey.vaibhav3110@gmail.com",
    description="InstaGram Scrapper",
    long_description_content_type="text/markdown",
    long_description=desc_long,
    packages=find_packages(),
    package_data={"my_package": ["./sample1.py"]},
    url="https://github.com/3110vaibhav2005/Igram/blob/main/sample1.py",
    install_requires=['requests','json','bs4'],
    keywords=['Instagram info','webscrapping','instagram id name',"IGram","insta scrapper",'webscrapper','beautifulsoup','vaibhavpandey module','vaibhav pandey python module','Instagram by pyhton'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)