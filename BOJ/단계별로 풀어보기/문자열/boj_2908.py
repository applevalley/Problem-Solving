x, y = map(str, input().split())
nx, ny = '', ''

for i in range(3):
    nx += x[-(1+i)]
    ny += y[-(1+i)]

if int(nx) > int(ny):
    print(nx)
else:
    print(ny)