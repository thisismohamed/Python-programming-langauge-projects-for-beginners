import hashlib

def generate_hash(data, algorithms):
    hasher = hashlib.new(algorithm)
    data_bytes = data.encode('UTF-8')
    hasher.update(data_bytes)
    hash_digest = hasher.hexdigest()
    return hash_digest

data = input("Enter data to hash: ")

print("1. MD5")
print("2. SHA1")
print("3. SHA224")
print("4. SHA256")
print("5. SHA384")
print("6. SHA512")
print("7. BLAKE2B")
print("8. BLAKE2S")
print("9. SHA3_224")
print("10. SHA3_256")
print("11. SHA3_384")
print("12. SHA3_512")
# print("13. SHAKE_128")
# print("14. SHAKE_256")
choice = input("Enter your choice (1-12): ")

algorithm_map = {
        "1": "md5",
        "2": "sha1",
        "3": "sha224",
        "4": "sha256",
        "5": "sha384",
        "6": "sha512",
        "7": "blake2b",
        "8": "blake2s",
        "9": "sha3_224",
        "10": "sha3_256",
        "11": "sha3_384",
        "12": "sha3_512"
        }

algorithm = algorithm_map.get(choice)
if algorithm:
    hash_result = generate_hash(data, algorithm)
    print("Hash:",hash_result)
else:
    print("Invalid choice")
