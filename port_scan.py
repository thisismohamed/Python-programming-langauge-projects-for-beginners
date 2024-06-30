import socket

def scan_port(host, port):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    r = sock.connect_ex((host, port))
    if r == 0:
      print("Port %d is open" % port)
    else:
      print("Port %d is close" % port, end='\r')
    sock.close()
  except socket.error as error:
    raise socket.error("Error: %s" % error)

def main():
  host = '127.0.0.1'
  for port in range(1, 65535):
    scan_port(host, port)
main()
