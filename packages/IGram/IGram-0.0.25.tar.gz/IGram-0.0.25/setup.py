from setuptools import setup,find_packages
import os
import codecs


setup(
    name="IGram",
    version="0.0.25",
    author="Vaibhav Pandey",
    author_email="pandey.vaibhav3110@gmail.com",
    description="InstaGram Scrapper",
    long_description_content_type="text/markdown",
    long_description="A webscrapper to Scrap some details from INSTAGRAM handle\nThis would basically gives the \nPosts(),Followers(),Following(),ProfileImage(),Name(),Description()",
    packages=find_packages(),
    package_data={"my_package": ["./sample1.py"]},
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