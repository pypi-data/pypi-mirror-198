from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


setup(name='phi-ai-ask',
      version='0.1.0',
      description='phitrellis ai system',
      author='phitrellis',
      author_email='shofuengwei@phitrellis.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(),  # 系统自动从当前目录开始找包
      requires=['requests'],
      license="apache 3.0")
