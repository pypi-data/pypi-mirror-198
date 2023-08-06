from setuptools import setup, find_packages

setup(name="WaterMap",
      version="1.0.0",
      description="Water Mapping from Remote Sensing Images",
      author="Wiserli Pvt Ltd",
      packages=find_packages(),
      install_requires=[
            "numpy~=1.22.1",
            "tifffile~=2022.8.12",
            "matplotlib~=3.5.1",
            "gdown~=4.5.1",
            "tensorflow~=2.10.0",
      ],
      )


# from setuptools import setup
#
# setup(
#    name='WaterMap',
#    version='0.1.0',
#    author='Wiserli Pvt Ltd',
#    author_email='wiserli.in@gmail.com',
#    packages=['WaterMap'],
#    scripts=['bin/script1','bin/script2'],
#    # url='http://pypi.python.org/pypi/PackageName/',
#    license='LICENSE.txt',
#    description='Water Mapping from Remotesensing Images',
#    long_description=open('README.txt').read(),
#    install_requires=[
#        "tensorflow==2.6.2",
#       "opencv-python==4.5.5.64",
#       "numpy==1.19.5",
#    ],
# )
