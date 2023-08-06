# mnzipcodes
mnzipcodes is a simple library for querying Mongolian zip codes.

### Examples
```python
>>> import mnzipcode
>>> 

>>> mnzipcode.isReal(11000)
True
>>> 

>>> mnzipcode.getProvince(85237)
'Ачит'
>>> 

>>> mnzipcode.getZipCode('Улаанбаатар')
[11000]
>>>
```