from setuptools import setup, find_packages

setup(name='phi-ai-ask',
      version='0.0.2',
      description='phitrellis ai system',
      author='phitrellis',
      author_email='shofuengwei@phitrellis.com',
      packages=find_packages(),  # 系统自动从当前目录开始找包
      requires=['requests'],
      license="apache 3.0")
