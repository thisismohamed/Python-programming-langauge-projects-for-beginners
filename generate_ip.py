import random

def generate_ip():
  return ".".join(str(random.randint(10, 169)) for i in range(4))

if __name__ == "__main__":
  num_ip = 100
  ip_list = [generate_ip() for i in range(num_ip)]
  print(ip_list)
