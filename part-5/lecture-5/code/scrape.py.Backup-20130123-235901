import mechanize
import numpy as np
import matplotlib.pyplot as plt
from BeautifulSoup import BeautifulSoup
import scipy

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6; en-us) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9')]

res = br.open("http://en.wikipedia.org/wiki/Anscombe's_quartet")
soup = BeautifulSoup(res.read())

tbl = soup.find(lambda tag: (tag.name == 'caption') and tag.text == "Anscombe's quartet").parent
arr_list = []
for row in tbl.findAll('tr'):
    elements = row.findAll('td')
    if len(elements) != 0:
        try:
            np.float(elements[0].string)
        except:
            continue
        arr = np.array([np.float(elem.string) for elem in elements])
        arr_list.append(arr)

data = np.vstack(arr_list)

grid = np.linspace(2, 20, 100)
for i in xrange(4):
    x = data[:, 2 * i]
    y = data[:, 2 * i + 1]
    a, b = scipy.polyfit(x, y, 1)
    plt.subplot(2, 2, i + 1)
    plt.plot(grid, a * grid + b, 'b-', x, y, 'mo')
    plt.xlabel("$x_" + str(i + 1) + "$")
    plt.ylabel("$y_" + str(i + 1) + "$")
    plt.xlim((2, 20))
    plt.ylim((2, 14))

plt.suptitle("CME 193: Anscombe's quartet by Daniel Frank")
plt.savefig('quartet.png')
