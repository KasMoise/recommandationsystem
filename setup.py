from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System-using-Machine-Learning"
AUTHOR_USER_NAME = "Kambale Kasambya Moise"
SRC_REPO = "recommandationsystem"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name="recommandationsystem",
    version="0.0.1",
    author="Kambale Kasambya Moise",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KasMoise/recommandationsystem",
    author_email="kasambya1987@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
