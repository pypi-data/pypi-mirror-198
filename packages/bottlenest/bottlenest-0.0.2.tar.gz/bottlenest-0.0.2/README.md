# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

# Build and publish

rm -rf dist/
python3 -m build
python3 -m twine upload dist/*

# Install

pip install bottlenest
