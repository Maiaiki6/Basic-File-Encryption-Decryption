# Basic File Encryption/Decryption

This Python script allows you to encrypt and decrypt text files using Fernet encryption from the cryptography library.

## Requirements

- Python 3.x
- cryptography library (install via `pip install -r requirements.txt`)

## Usage

Run the script with:

```bash
python encrypt_decrypt.py
```

### Encryption

1. Choose 'encrypt' when prompted.
2. Enter the path to the file you want to encrypt.
3. The script will generate a key, display it, and create an encrypted file with '.encrypted' extension.

**Important:** Save the key securely; you need it for decryption.

### Decryption

1. Choose 'decrypt' when prompted.
2. Enter the path to the encrypted file (usually ends with '.encrypted').
3. Enter the key when prompted.
4. The script will create a decrypted file with '.decrypted' extension.

## Example

Encrypting a file:

```
Enter mode (encrypt/decrypt): encrypt
Enter file path: test.txt
Generated key: abc123...
Encrypted file saved as: test.txt.encrypted
```

Decrypting:

```
Enter mode (encrypt/decrypt): decrypt
Enter file path: test.txt.encrypted
Enter key: abc123...
Decrypted file saved as: test.txt.encrypted.decrypted
```

## Troubleshooting

- Ensure the file path is correct and the file exists.
- For decryption, use the exact key generated during encryption.
- If decryption fails, check the key and file.