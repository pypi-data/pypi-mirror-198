from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ocacaptcha',
  version='0.0.5',
  description='Solving TT capctha circle and 3D captcha (with the same shapes)',
  url='',  
  author='Nazarii',
  author_email='nazar.muxaulyk961@mail.ru',
  license='MIT', 
  classifiers=classifiers,
  keywords='tiktokcaptcha', 
  packages=find_packages(),
  install_requires=['json','time','requests','random','string','base64','urllib.request','hashlib'] 
)
