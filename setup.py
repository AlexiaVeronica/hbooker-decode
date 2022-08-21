from setuptools import setup

setup(
    name='decode',
    version='1.0',
    packages=['decode'],
    include_package_data=True,  # 自动打包文件夹内所有数据
    url='',
    license='MIT License',
    author='Alexia',
    author_email='',
    entry_points={"console_scripts": ["hbooker = decode.__init__:main"]},
    description='decode hbooker data',
    zip_safe=True
)
