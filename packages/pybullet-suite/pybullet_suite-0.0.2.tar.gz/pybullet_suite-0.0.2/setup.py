from setuptools import setup, find_packages

setup(
   name='pybullet_suite',
   version='0.0.2',
   description='Pybullet wrapper for easy use',
   author='Kanghyun Kim',
   author_email='kh11kim@kaist.ac.kr',
   install_requires=[
      "numpy",
      "scipy",
      "pybullet",
      "trimesh"
   ],
   packages=find_packages(),  #same as name
)

# python setup.py sdist bdist_wheel
# twine upload dist/*
