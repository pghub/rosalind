m=5
k=3

def numbRabbitsPairs(n,k):
    if(n > 2):
        return numbRabbitsPairs(n-2, k) * k + numbRabbitsPairs(n-1, k)
    else:
        return 1

