from setuptools import setup, find_packages

setup(
    name='ChatGPTonWhatsApp',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',
        'openai',
        'bs4'
    ],
    description="The following is a Python Package [ChatGPTonWhatsApp] that uses the Selenium and OpenAI libraries to create a chatbot for WhatsApp. The chatbot listens to incoming messages, processes them using OpenAI's GPT-3 language model, and replies with a generated response.",
    author='Danish Ali',
    author_email='help@masterprograming.com',
    license='MIT',
    url='https://github.com/masterprogramingdotcom/chatgptonwhatsapp',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
