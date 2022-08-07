from setuptools import setup, find_packages
import os
import plot2svg

this_directory = os.path.abspath(os.path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(name='plot2svg',
      python_requires='>=3.5',
      version=plot2svg.__version__,
      description='A simple plot tool to generate small SVG files',
      long_description=read_file('README.md'),
      long_description_content_type="text/markdown",
      url='https://github.com/guofei9987/plot2svg',
      author='Guo Fei',
      author_email='guofei9987@foxmail.com',
      license='MIT',
      packages=find_packages(),
      platforms=['linux', 'windows', 'macos'],
      install_requires=[''],
      zip_safe=False)
