from distutils.core import setup
setup(
  name = 'shyne',
  packages = ['Shyne'],
  version = '0.1',
  license='MIT',
  description = 'A highly customizable game engine with nodal programming powered by pyNDL',
  author = 'Louis Gambardella',
  author_email = 'louis.gambardella03@gmail.com',
  url = 'https://github.com/merwynnn/Shyne',
  download_url = 'https://github.com/merwynnn/Shyne/archive/refs/tags/v_01.tar.gz',
  keywords = ['Game' 'Engine', 'GameEngine', 'Nodal', 'Language', 'pyNDL', 'Blueprint'],
  install_requires=[
          'python-ndl',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
  package_dir={'Shyne': 'Shyne'},
  package_data={'Shyne': ['Prefabs/*.py', 'Assets/Images/*.png', 'Assets/Images/*.jpg']},

)