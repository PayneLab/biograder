# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import serialization


class Encryptor:

    def __init__(self):
        #Todo: read key from file
        self.public_key = self.getKey()
        pass

    def getKey(self):
        with open("public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
            return public_key

    def uploadToBox(self, raw_file):
        #need to parse out answers and encrypt them
        #create new file and push the encrypted answers (and hints to separate file unencrypted)

        pass

    def encrypt(self, raw_data):
        print(raw_data)
        #below posed as a possible alternative
        #pow(message, public.e, public.n)
        encrypted = self.public_key.encrypt(
            raw_data,
            padding.OAEP(
                #mgf=padding.MGF1(algorithm=hashes.SHA256()),
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted

    #only called once ever! don't want more than one set of keys
    def saveKey(self, public_key, private_key):
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open('public_key.pem', 'wb') as f:
            f.write(pem)

        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        with open('private_key.pem', 'wb') as f:
            f.write(pem)


