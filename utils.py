def each_cons(string, size):
    return [string[i:i+size] for i in range(len(string)-size+1)]
