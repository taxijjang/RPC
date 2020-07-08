from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('0.0.0.0',9000),
                        requestHandler=RequestHandler)as server:
    server.register_introspection_functions()

    def message(request):
        print("response {}".format(request))
        return "response {}".format(request)

    server.register_function(message,'message')
    server.serve_forever()