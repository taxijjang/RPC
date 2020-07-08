
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('localhost',8000),
                        requestHandler=RequestHandler)as server:
    server.register_introspection_functions()



    server.serve_forever()