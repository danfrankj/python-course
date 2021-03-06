x = np.linspace(0, 10, 1000)
y = np.power(x, 2)
plt.plot(x, y)
plt.xlim((1, 5))
plt.ylim((0, 30))
plt.xlabel('my x label')
plt.ylabel('my y label')
plt.title('plot title, including $\Omega$')

plt.savefig('line_plot_plus.png')
