import sys, heapq

 

n = int(sys.stdin.readline().strip())

a = [int(sys.stdin.readline().strip()) for i in xrange(n)]

 

smallest = [float('inf')] * a[0]

smallest[0] = 0

queue = [(0, 0)]

while queue:

    total, modulo = heapq.heappop(queue)

    for i in xrange(1, n):

        x1, x2 = smallest[modulo] + a[i], (modulo + a[i]) % a[0]

        if x1 < smallest[x2]:

            smallest[x2] = x1

            heapq.heappush(queue, (x1, x2))

 

k = int(sys.stdin.readline().strip())

b = [int(sys.stdin.readline().strip()) for i in xrange(k)]

 

output = ['NIE' if b[i] < smallest[b[i] % a[0]] else 'TAK' for i in xrange(k)]

sys.stdout.write('\n'.join(output))