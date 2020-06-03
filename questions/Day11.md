python | Intermediate | 11

Day 11: Double fold.
Part I:

Given a list of tokens (strings, integers or a combination) and a dictionary from token to token, write a function named  resolve to resolve each token and return a list of the resolved tokens in the same order. Resolving a token means repeatedly searching for it as a key in the dictionary and replacing it with the associated value until it cannot be found in the dictionary as a key. If there is an infinite loop of values or it is not in the dictionary, you should resolve a token to itself.

For example, if the dictionary is d = {'a': 'b', 'b': 'c', 'p': 'q', 'q': 'p'}, we resolve a to c, b to c, p to p, q to q, and z to z.

resolve(d, ['a','b','p','q','z']) returns ['c', 'c', 'p', 'q', 'z']

Explanation:

'a' maps to 'b' which maps to 'c' in the dictionary. c doesnt map to anything(i.e is not a key so it maps to itself)

'b' maps to 'c' which maps to itself

'p' maps to 'q' which maps to 'p' which maps to 'q' and it keeps going infinite;y. Hence we map 'p' to itself

'q' maps to 'q' just like p described above

'z' maps to itself as it isnt a key in the dictionary

Another example

d={'a':'b','b':'c','c':b}

resolve(d,['a','b']) returns ['b'.'b']

explantion is a maps to 'b' which maps to 'c' which maps to 'b' which maps to c(infinitely) so the answer is b

for the reason described above b maps to b also.

last example

d={'a':'b','b:'c','c':'a'}

resolve(d,['a']) will return ['a'] 

a maps to b which maps to c which maps back to a and the loop continues.

 

All keys should be alphabetic and integers positive.