
(n,m) = map(int,input().split())
M = list(map(int,input().split()))
C = list(map(int,input().split()))

N = []

A = [[0] * (m+1) for _ in range(n+1)]

# максимальная стоимость рюкзака вместимостью q и если используется p предметов
# равна максимуму из максимальной стоимости рюкзака с такойже вместимостью и если используется p-1 предмет(если с предметом p сумарная масса превышает лимит)
# и (максимальной стоимости рюкзака с вместимостью меньшей на массу p-ого предмета и если используется p-1 предмет) + ценности p-ого предмета 

for p in range(1,n+1):
    for q in range(1,m+1):
        A[p][q] = A[p-1][q]
        if M[p-1] <= q and (A[p-1][q-M[p-1]]+C[p-1] > A[p][q]):
            A[p][q] = A[p-1][q-M[p-1]]+C[p-1]
            

# начинаем с максимальной стоимости рюкзака и смотрим
# если максимальная стоимость с данной вместимостью такая же как и без последнего предмета то последни предмет не берем
# иначе берем и продолжаем с максимальной стоимости без этого предмета и вместимостью меньшей на массу этого предмета
def foo(p, q):
    if A[p][q] == 0:
        return 0
    if A[p-1][q] == A[p][q]:
        foo(p-1,q)
    else:
        N.append(p)
        foo(p-1,q-M[p-1])
        
foo(n,m)

print(len(N))
print(*N)


    