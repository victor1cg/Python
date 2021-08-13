def notas(*n, sit=False):                # por padrão é falso
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    
    return r

a = notas(6,7,9,2.5)
print(a , sep='\n')
    