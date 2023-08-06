import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
 name='pysyn_data',
 version='0.3',
 author="Raghav_Ritesh",
 author_email="raghav.20.rb@gmail.com",
 description="This package is for generating synthetic data using 4 models i.e Conditional Genrative Adveserial Networks(CTGAN), Gaussian Mixture Model (GMM), Prinicipal Component Analysis (PCA) and Bayesian Network (BN). It also informs the user which model will work best based on the input data characterisitics."
 ,
 packages=setuptools.find_packages(),
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
 readme = "README.md",
 long_description=long_description,
 long_description_content_type="text/markdown",
 )