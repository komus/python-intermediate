# Serialization

Serialization is the process of converting strutured data to a format that allows for storage or sharing. Save as flat or nested data

- file especially csv - flat
- pickle - nested
- JSON - nested - JavaScript Object Notation
- numpy array - flat
- YAML - nested


# Pickle
This is a native serialization module in python. Pickling is the process whereby a python object hierarchy is converted into a byte stream. 

pickle not secure against erroneous or malicious constructed data. NEVER unpickle data received from an untrusted or unauthenticated source

# JSON
Way to store and transmit text data. It is most popular for creating and using Restful Web APIs