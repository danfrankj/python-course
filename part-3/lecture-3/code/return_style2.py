def nchoosek(n, k):
    val1 = fact(n)
    val2 = fact(n - k)
    val3 = fact(k)
    return_value = val1 / (val2 * val3)
    return return_value

def nchoosek(n, k):
    return fact(n) / (fact(n - k) * fact(k))
