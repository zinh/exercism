def append(xs, ys):
    return foldr(lambda x, memo: [x] + memo, xs, ys)

def concat(lists):
    return foldl(lambda memo, l: append(memo, l), lists, [])

def filter_clone(function, xs):
    return foldr(lambda x, memo: [x] + memo if function(x) else memo, xs, [])

def length(xs):
    return length_recur(xs, 0)

# tail recursive version
def length_recur(xs, n):
    if xs == []:
        return n
    return length_recur(xs[1:], n + 1)

def map_clone(function, xs):
    return map_clone_recur(function, xs, [])

# tail recursive version
def map_clone_recur(function, xs, memo):
    if xs == []:
        return memo
    else:
        return map_clone_recur(function, xs[1:], memo + [function(xs[0])] )

def foldl(function, xs, acc):
    if length(xs) == 0:
        return acc
    else:
        return foldl(function, xs[1:], function(acc, xs[0]))

def foldr(function, xs, acc):
    if length(xs) == 0:
        return acc
    else:
        return function(xs[0], foldr(function, xs[1:], acc))

def reverse(xs):
    return foldl(lambda memo, x: [x] + memo, xs, [])
