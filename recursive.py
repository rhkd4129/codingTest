def recursive_funcciton(i):
    print("재귀함수호출")
    if i == 5:
        return
    print(f"{i}번쨰 재귀 함수에서 {i+1}번째 재귀함수호출")
    recursive_funcciton(i+1)
    print(f"{i}번째 재귀함수를 종료")

# recursive_funcciton(1)

def factoral_iterative(n):
    result = 1
    for x in range(1,n+1):
        result *= x
    return result

def factoral_recursive(n):
    if n <=1:
        return
    return n * factoral_recursive(n-1)

print(factoral_iterative(5))
print(factoral_recursive(5))