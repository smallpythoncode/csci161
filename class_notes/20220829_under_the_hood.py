"""
interpreters maintain objects as the program is running
python doesn't explicitly create objects
- other objects create them implicitly
will keep an object around as long as there is at least one reference
  to that object
- no reference? garbage collection removes it
- may keep the object if there is excess memory
  - no need to collect? no need to use those resources

every object has certain characteristics:
- type
  - determines mutability
- ID (memory location)

esoteric
- intended for or likely to be understood by only a small number of people
  with a specialized knowledge or interest
"""