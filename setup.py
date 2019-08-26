from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    description='A Girder plugin showing a heatmap of geospatial data.',
    install_requires=[
        'girder>=3.0.2'
    ],
    license='Apache Software License 2.0',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='girder-plugin, geo_heatmap',
    name='geo_heatmap',
    packages=find_packages(exclude=['test', 'test.*']),
    url='https://github.com/girder/geo_heatmap',
    version='0.1.0',
    zip_safe=False,
    entry_points={
        'girder.plugin': [
            'geo_heatmap = geo_heatmap:GirderPlugin'
        ]
    }
)
