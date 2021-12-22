# Present info
Hi Petr, glad that you have discovered the hint. Here are the tools that will help you in cracking  the cipher. Use them wisely and be smart. David
# sha0
This is an implementation of the SHA-0 algorithm. Note that SHA-0 is a BROKEN
algorithm; this program has been created to verify old, broken signatures.

## Credits
The whole thing is based on RFC6234 (which contains a reference implementation
of SHA-1). It has been put into compilable code by Tom Szilagyi (@tomszilagyi)
[in his GitHub project](https://github.com/tomszilagyi/rfc6234). The hint of
what code changes turn SHA-1 into SHA-0 have been taken from StackExchange
fgrieu, who 
[did an excellent outline on the code differences](https://crypto.stackexchange.com/questions/62055/where-can-i-find-the-description-of-sha0-algorithm).
I'm basically just the monkey gluing pieces together :)

## Usage PYTHON
Navigate the python interface.py code for example call. There are two functions equal in result provided for testing. Build your code on top of that.
## Usage C
This code can be also compiled using makefile. You will get executable this way and can use the *get_hash_subprocess()* python function.
For faster option you will need to compile dynamic library yourself so the *get_hash_dll()* can be used.

## License
IETF license, see LICENSE file.
