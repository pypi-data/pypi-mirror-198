# Build the package

The build files are located in <code>./dist</code>.

- <code>python3 -m build</code>

# Upload the package to [PyPi](https://test.pypi.org/account/login/?next=%2Fmanage%2Faccount%2F)

- Install twine if necessary <code>python3 -m pip install --upgrade twine</code>
- <code>python3 -m twine upload --repository pypi dist/*</code>
- User <code>__token__</code> as username and token with <code>pypi-</code> prefix.

# Install the package

- <code>pip install xfaas_core_python3</code>