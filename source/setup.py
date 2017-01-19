from setuptools import setup

setup(name='neurodesign',
      version='0.0.14',
      description='Package for design optimisation for fMRI experiments',
      author='Joke Durnez',
      author_email='joke.durnez@gmail.com',
      license='MIT',
      packages=['neurodesign'],
      package_dir={'neurodesign':'src'},
      package_data={'neurodesign':['media/NeuroDes.png']},
      install_required=[
      "numpy",
      "scipy",
      "collections",
      "pandas",
      "itertools",
      "json",
      "os",
      "sys",
      "zipfile",
      "StringIO",
      "shutil",
      "copy",
      "sklearn",
      "math",
      "pickle",
      "time",
      "matplotlib",
      "reportlab",
      "cStringIO",
      "seaborn",
      "pdfrw",
      "progressbar"
      ],
      zip_safe=False)
