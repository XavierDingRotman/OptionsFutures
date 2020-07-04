
def binary_search(start, end, func, tol=0.0001, max_iter = 1000, num_iter=0):
    if func(start) == 0:
        return func(start)
    if func(end) == 0:
        return func(end)
    mid = (start + end) / 2
    if abs(func(mid)) < tol:
        return mid

    if func(start) > 0 and func(end) < 0:
        temp = end
        end = start
        start = temp

    if func(mid) > 0:
        end = mid
    elif func(start) < 0:
        start = mid
    num_iter += 1
    if num_iter > max_iter:
        print("Can not find the zero point")
        return mid
    return binary_search(start, end, func, tol, max_iter, num_iter)
