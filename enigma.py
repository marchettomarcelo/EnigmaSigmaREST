import numpy as np

alf = 'abcdefghijklmnopqrstuvwxyz ,.ãé'
alfabeto_ident = np.identity(len(alf))

encoder = np.roll(alfabeto_ident,-5,1)

encoder2 = np.roll(alfabeto_ident,3,1)

def para_one_hot(msg):
    l = list()
    for a in msg:
        i = alf.index(a)
        l.append(alfabeto_ident[i])
    l = np.array(l)
    return l.transpose()

def para_string(array):
    saida = ''
    array = array.transpose()

    for l in array:
        saida += alf[ np.where(l == 1)[0][0] ]
        
    return saida

def cifrar(msg, P):
    msg = para_one_hot(msg)
    saida = np.dot(P,msg)
    return para_string(saida)

def de_cifrar(msg,P):
    return para_string(np.dot(np.linalg.inv(P),para_one_hot(msg)))

def enigma_simples(msg,P,E):
    msg = para_one_hot(msg)
    m_ = E@P@msg
    return para_string(m_)

def de_nigma_simples(msg,P,E):
    msg = para_one_hot(msg)
    m_ = np.linalg.inv(P)@np.linalg.inv(E)@msg
    return para_string(m_)

def enigma(msg,P,E):
    n = len(msg)
    msg = para_one_hot(msg)
    final = list()
    for i in range(n):
        l = msg[:,i].transpose()
        arr = P@l
        for _ in range(i+1):
            arr = E@arr
        final.append(arr)

    return para_string(np.array(final).transpose())

def de_nigma(msg,P,E):
    n = len(msg)
    msg = para_one_hot(msg)
    saida = list()
    e_ = np.linalg.inv(E)
    p_ = np.linalg.inv(P)
    for i in range(n):
        l = msg[:,i].transpose()
        for _ in range(i+1):
            l = e_@l
        arr = p_@l
        saida.append(arr)
    
    return para_string(np.array(saida).transpose())


x = enigma("barros", encoder, encoder2)
print(x)


print(de_nigma(x, encoder, encoder2))