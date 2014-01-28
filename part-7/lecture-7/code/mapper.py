def mapper(key, value):
    # value is ignored, key is a line of text
    for k in key.split():
        yield k.strip(), 1
