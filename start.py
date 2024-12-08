import base64

def run_base64_script(encoded_file):
    # Membaca file yang diencode
    with open(encoded_file, 'rb') as file:
        encoded_code = file.read()
    # Decode kembali ke Python asli
    decoded_code = base64.b64decode(encoded_code)
    # Eksekusi kode Python
    exec(decoded_code.decode())
run_base64_script('run.py.b64')