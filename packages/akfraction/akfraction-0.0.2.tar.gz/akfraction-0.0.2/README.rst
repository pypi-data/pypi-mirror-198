Package_name
============

akfraction is a Python library for dealing with arithmetic operation.

Installation
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`__ to
install akfraction.

.. code:: bash

   pip install akfraction

Usage
-----

.. code:: python

   from akfraction import Fraction

   a,b,c,d = [int(e) for e in input().split()]
   fraction1 = Fraction(a,b)
   fraction2 = Fraction(c,d)
   print(f"fraction1 = {fraction1}")
   print(f"fraction2 = {fraction2}")
   print(f"fraction1+fraction2 = {fraction1+fraction2}")
   print(f"fraction1-fraction2 = {fraction1-fraction2}")
   print(f"fraction1*fraction2 = {fraction1*fraction2}")
   print(f"fraction1/fraction2 = {fraction1/fraction2}")

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

Author
------

Adisak Karnbanjong

License
-------

`MIT <https://choosealicense.com/licenses/mit/>`__
