from setuptools import setup, find_packages
import setuptools

setup(name='newWhoisBobPkgs', # 패키지 명

version='1.0.0.11',

description='bob8gook',

author='bob8gook',

author_email='hyeok.jang@lotte.net',

url='https://github.com/woounnan',

license='MIT', # MIT에서 정한 표준 라이센스 따른다

#py_modules=['testbob8gook'], # 패키지에 포함되는 모듈
py_modules=['newWhoisBobPkgs', 'bobwhois'], # 패키지에 포함되는 모듈

python_requires='>=3',

#install_requires=['whois'], # 패키지 사용을 위해 필요한 추가 설치 패키지

packages=setuptools.find_packages() # 패키지가 들어있는 폴더들

)