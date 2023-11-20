from server.simple_server import server

from settings import HOST_NAME, PORT

if __name__ == "__main__":
    print("Server started at http://%s:%s" % (HOST_NAME, PORT))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped.")
