

### Get GGUF information 
from struct import unpack

filename = 'path_to_file.gguf'
with open(filename, mode='rb') as f:
    # 'GGUF' magic number
    magic_number = f.read(4).decode('utf-8')
    print(f'Magic number: {magic_number}')

    # GGUF version
    version, = unpack('<i', f.read(4))
    print(f'Version: {version}')

    # number of tensors
    tensor_count, = unpack('<Q', f.read(8))
    print(f'Tensor count: {tensor_count}')

    # number of metadata key-value pairs
    metadata_kv_count, = unpack('<Q', f.read(8))
    print(f'Metadata key-value count: {metadata_kv_count}')



### Get safetensor information 
from struct import unpack
from json import dumps, loads

with open('path_to_file..safetensors', mode='rb') as f:

    # reading first 8 bytes to get the size of the header
    size_bytes = f.read(8)
    size, = unpack('<Q', size_bytes)

    # the header is 9512 bytes long, reading it and printing a pretty JSON
    header_bytes = f.read(size)
    header_json = loads(header_bytes)
    header_pretty = dumps(header_json, indent=4)

    print(header_pretty)
