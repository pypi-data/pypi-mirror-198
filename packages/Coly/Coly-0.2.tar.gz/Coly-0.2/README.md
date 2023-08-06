# Coly
##### Core Output and Encoding Library.
***
### Commands and Usage:
##### Encoding:
If you wish to only import this part use ```from Coly import encryption```
* twoKey(message) - Encodes a string two times and returns the string then two keys
* decrypt(encoded_message, key1, key2) - Decodes the string using the encoded string and the two given keys
#### Color:
If you only wish to import this part then use : ```from Coly import COL```
* Options:
  * black
  * red 
  * green 
  * yellow 
  * blue 
  * magenta 
  * cyan 
  * white 
  * reset 
  * BOLD 

To use this you use a normal print function like this:
``print(COL.red "example")`` Be sure to change the "red" part to a option of your choosing.