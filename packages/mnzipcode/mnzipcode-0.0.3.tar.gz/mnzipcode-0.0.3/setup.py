import setuptools 

setuptools.setup(
  name='mnzipcode',
  version='0.0.3',
  author='Bekkage',
  description='mnzipcodes is a simple library for querying Mongolian zip codes.',
  long_description="""
mnzipcodes is a simple library for querying Mongolian zip codes.

import mnzipcode
mnzipcode.isReal(11000)
mnzipcode.getProvince(85237)
mnzipcode.getZipCode('Улаанбаатар')
  """,
  package=['mnzipcodes']
)