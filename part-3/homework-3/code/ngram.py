"""
Compute the k most frequently occuring n-grams of a text file.

n specifies that we want to compute the n-grams
k specifies that we want the k most frequently occuring n grams
  (breaking ties arbitrarily)
document is a text file

The return value is a dictionary, where each key is the n-gram string and
the value is the number of times that n-gram occurred in the text.

Remember that the n-grams are consecutive words in a text, and we will
only consider n-grams contained entirely on one line of the text.
"""
def ngram(n, k, document):
  # IMPLEMENT THIS

  # REMOVE THIS
  return {}


"""
Test functions. Try out your code.
"""
def test1():
  print ngram(2, 3, 'course_description.txt')
  print ngram(3, 5, 'course_description.txt')
  print ngram(5, 1, 'course_description.txt')
  print ngram(1, 15, 'course_description.txt')


if __name__ == '__main__':
  print 'running test 1...'
  test1()
