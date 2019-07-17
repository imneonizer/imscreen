from distutils.core import setup
setup(
  name = 'imscreen',         # How you named your package folder (MyLib)
  packages = ['imscreen'],   # Chose the same as "name"
  version = '0.2.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This Library is used to Capture your \"Computer\'s Screen / Webcam\" with Ultra High FPS.',   # Give a short description about your library
  author = 'Nitin Rai',                   # Type in your name
  author_email = 'mneonizer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/imneonizer/imscreen',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/imneonizer/imscreen/archive/v0.2.1.tar.gz',    # I explain this later on
  keywords = ['Screen Shot', 'Screen Capture', 'Webcam Reading'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'mss',
          'numpy',
          'opencv-contrib-python',
          'screeninfo',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
