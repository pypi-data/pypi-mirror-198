from setuptools import setup
from setuptools import find_packages

setup(
    name='hoonpyutils',                             # How you named your package folder (hoonpyutils)
    packages=['hoonpyutils'],                       # Choose the same as "name".
    # packages=find_packages(exclude=[]),
    version='0.2',      # Start with a small number and increase it with every change you make.
    license='MIT',      # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Hoon Python Utilities',            # Give a short description about your library.
    author='NeoHoon',                               # Type in your name.
    author_email='hoon.paek@neoplatform.net',       # Type in your E-Mail.
    url='https://github.com/neohoon/hoonpyutils',   # Provide either the link to your github or to your website.
    download_url='https://github.com/neohoon/hoonpyutils/archive/master.zip',   # 배포하는 패키지의 다운로드 url을 적어줍니다.
    keywords=['hoon python utilities'],             # Keywords that define your package best.
    # 해당 패키지를 사용하기 위해 필요한 패키지를 적어줍니다. ex. install_requires= ['numpy', 'django']
    # 여기에 적어준 패키지는 현재 패키지를 install할때 함께 install됩니다.
    install_requires=[],
    python_requires='>=3',                  # 해당 package 를 사용하기 위해 필요한 파이썬 버전을 적는다.
    package_data={},                        # 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data 에 포함시켜야 합니다.
    zip_safe=False,                         # 위의 package_data 에 대한 설정을 했다면 zip_safe 설정도 해야 합니다.
    # PyPI에 등록될 메타 데이터를 설정합니다.
    # 이는 단순히 PyPI에 등록되는 메타 데이터일 뿐이고, 실제 빌드에는 영향을 주지 않습니다.
    classifiers=[
        'Development Status :: 3 - Alpha',          # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
                                                    # as the current state of your package.
        'Intended Audience :: Developers',          # Define your audience.
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',   # Pick a license.
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',      # Specify which python versions that you want to support.
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

'''
import setuptools
import shutil
import os

os.makedirs("temp")
shutil.move("smartxpyutils/.git", "temp")
shutil.move("smartxpyutils/.idea", "temp")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartxpyutils",
    version="0.2.0",
    author="HOON PAEK",
    author_email="hoon.paek@gmail.com",
    description="Smart X Python Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neohoon/smartxpyutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

shutil.move("temp/.git", "smartxpyutils")
shutil.move("temp/.idea", "smartxpyutils")
os.rmdir("temp")
'''
