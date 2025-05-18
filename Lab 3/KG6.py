from Crypto.PublicKey import RSA

key = RSA.generate(3072)

private_key = key.export_key()

public_key = key.publickey().export_key()

with open("d.key", "wb") as f:
    f.write(private_key)

with open("e.key", "wb") as f:
    f.write(public_key)