
def fiboncci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
      return fiboncci(n-1) + fiboncci(n-2)

print(fiboncci(15))
# for i in range(15):
#     print(fiboncci(i))