This is my own implementation of the RSA public/private key encryption algorithm.
It is in no way usable, but rather a practical way of showing you how the algorithm works.

It decrypts letter by letter and is really really slow. It is all done in software and as Python is
notoriously slow in it self compared to compiled languages, this is a very bad implementation of the RSA encryption.

To add to the wound.. It only uses 3 digit prime numbers (again, any higher and you would be sitting there all day long).
Yes, that is another red flag because when you connect to an encrypted website you are using primes with hundreds of digitsfor the RSA handshake.


Anyways, I hope you learn something from it.
Here is a great video demonstration of the algorithm. https://www.youtube.com/watch?v=4zahvcJ9glg
