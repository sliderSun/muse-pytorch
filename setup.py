from setuptools import setup, find_packages

setup(
  name = 'muse-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'MUSE - Text-to-Image Generation via Masked Generative Transformers, in Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/muse-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'text-to-image'
  ],
  install_requires=[
    'einops>=0.6',
    'torch>=1.6',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
