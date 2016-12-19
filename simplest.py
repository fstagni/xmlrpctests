""" This is the simplest possible.

    As it is now it is not equipped with Threads/Processes/coroutines whatever so it can also serve one call at a time
"""

from SimpleXMLRPCServer import SimpleXMLRPCServer

import fib

def is_even(n):
  return n % 2 == 0

def fib_func(n):
  return fib.fib(n)

server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(is_even, "is_even")
server.register_function(fib_func, "fib")
server.serve_forever()
