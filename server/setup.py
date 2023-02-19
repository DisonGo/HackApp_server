from setuptools import setup, find_packages
if __name__ == '__main__':
    setup(
        # our custom class override
        name='my_package',
        py_modules=['__main__'],
        packages=find_packages(include=['sql', 'sql.crud', 'sql.models', 'sql.schemes'])
    )
