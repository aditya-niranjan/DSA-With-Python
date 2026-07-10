
from shlex import join

from numpy import char


strs = ["Hello","World"]


def encode(strs):

  strs = '#'.join(strs)

  return strs





def decode(encoded(strs)):
      
    decodetext = ",".join(strs)

    return strs



print(decode(encode(strs)))