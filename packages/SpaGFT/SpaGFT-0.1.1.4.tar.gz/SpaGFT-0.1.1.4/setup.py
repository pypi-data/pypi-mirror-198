import setuptools

setuptools.setup(
    name="SpaGFT",
    version="0.1.1.4",
    author="Jixin Liu, Yi Jiang",
    packages=['SpaGFT'],
    author_email="frankliu210@163.com, jiang.2902@buckeyemail.osu.edu",
    description='''SpaGFT is a python package to analyze spatial transcriptomics.
                   It was designed to identify spatially variable genes, 
                   detect tissue modules, enhance gene expression.''',
    url="https://github.com/jxLiu-bio/SpaGFT",
    project_urls={
        "Bug Tracker": "https://github.com/jxLiu-bio/SpaGFT/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["kneed==0.7.0",
		      "louvain==0.7.1",
		      "matplotlib==3.5.2",
		      "networkx==2.8",
		      "numpy==1.21.5",
		      "pandas==1.4.2",
		      "plotnine==0.8.0",
		      "scanpy==1.9.1",
		      "scikit-learn==1.0.2",
		      "scipy==1.8.0",
		      "gseapy==0.10.8",
              	      "igraph==0.9.10"]
)
