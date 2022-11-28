#twine upload -r testpypi dist/* --verbose
echo "Building Source and Wheel (universal) distribution…"
python setup.py sdist bdist_wheel --universal
echo "Uploading the package to PyPI via Twine…"
twine upload dist/*
# echo Pushing git tags…
