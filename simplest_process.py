""" Simple multi-process xmlrpc server

    No SSL (yet)
"""

import SocketServer
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

import fib

#functions going to be exposed
def fib_func(n):
  return fib.fib(n)

def fib_server(address = None):
  """ Start a xmlrpc server
  """

  class SimpleThreadXMLRPCServer(SocketServer.ForkingMixIn, SimpleXMLRPCServer):
    pass
  class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/TestSvc')

  if address is None:
    address = ("localhost", 8000)
  server = SimpleThreadXMLRPCServer(address,
                                    requestHandler=RequestHandler,
                                    logRequests=True,
                                    allow_none=True, )

  print "Listening at %s/%d..." % (address[0], address[1])

  server.register_function(fib_func, "fib")
  server.serve_forever()


fib_server()


### To use client side:
# import xmlrpclib
# proxy = xmlrpclib.ServerProxy("http://localhost:8000/TestSvc")
# proxy.fib(5)
