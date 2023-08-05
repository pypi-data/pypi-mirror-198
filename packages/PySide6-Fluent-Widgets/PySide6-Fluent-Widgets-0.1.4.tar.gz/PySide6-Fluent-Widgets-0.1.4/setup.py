import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PySide6-Fluent-Widgets",
    version="0.1.4",
    keywords="pyside6 fluent widgets",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A fluent design widgets library based on PySide6",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6",
    packages=setuptools.find_packages(),
    install_requires=[
        "PySideSix-Frameless-Window",
        "darkdetect",
    ],
    extras_require = {
        'full': ['scipy', 'pillow', 'colorthief']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
