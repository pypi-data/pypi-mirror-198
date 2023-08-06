
from setuptools import setup
import setuptools

# python setup.py sdist
# twine upload dist/*
# twine upload --skip-existing dist/*

setup(
    name='textanalyze4sc',     # 包名字
    version='2.0',   # 包版本
    description='文本分析库，可对文本进行词频统计、词典扩充、情绪分析等',   # 简单描述
    author='bqw',  # 作者
    author_email='beerbull@126.com',  # 邮箱
    url='https://github.com/martin6336/textanalyze4sc',      # 包的主页
    packages=setuptools.find_packages(),
    install_requires=['jieba', 'numpy', 'scikit-learn', 'numpy', 'matplotlib', 'pyecharts', 'shifterator','gensim','wordcloud','pyLDAvis','seaborn', 'hanlp','pandas','networkx','cnsenti','ltp'],
    #python_requires='>=3.5',
    license="MIT",
    keywords=['text mining','sentiment analysis', 'natural language processing', 'text similarity'],
    long_description=open('README.md').read(), # 读取的Readme文档内容
    long_description_content_type="text/markdown")  # 指定包文档格式为markdown
    #py_modules = ['eventextraction.py']
    
    
