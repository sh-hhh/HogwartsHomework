from setuptools import setup

setup(
    name='logger_plugin',
    url='https://github.com/xxx/logger_plugin',
    version='1.0',
    author="hong",
    author_email='418974188@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[  # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['logger_plugin'],
    keywords=[
        'pytest', 'py.test', 'logger_plugin',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 最关键的步骤，入口模块 或者入口函数
    entry_points={
        'pytest11': [
            # 会自动 加载这个包下的__init__.py文件
            'logger_plugin = logger_plugin',
        ]
    },
    # windows
    zip_safe=False
)
