import numpy as np

data = []
# Streaming QR factorizations
for k in xrange(1000000):
    row = np.random.randn(4)
    data.append(row)
    if len(data) > 100:
        Q, R = np.linalg.qr(data)
        yield R
        data = []
