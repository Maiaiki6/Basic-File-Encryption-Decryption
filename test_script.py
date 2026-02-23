from encrypt_decrypt import generate_key, encrypt_file, decrypt_file
import filecmp

# Generate key
key = generate_key()

# Encrypt test.txt
encrypt_file('test.txt', key)

# Decrypt the encrypted file
decrypt_file('test.txt.encrypted', key)

# Check if decrypted matches original
if filecmp.cmp('test.txt', 'test.txt.encrypted.decrypted'):
    print("Test passed: Decrypted file matches original.")
else:
    print("Test failed: Decrypted file does not match original.")