

def adivinhar(a, b, c):
    
    if a == 'vertebrado':

        if b == 'ave':
            if c == 'carnivoro':
                print('aguia')
            elif c == 'ornivoro':
                print('pomba')
            else:
                print('invalido')

        elif b == 'mamifero':
            if c == 'onivoro':
                print('homen')
            elif c == 'herbivoro':
                print('vaca')
            else:
                print('invalido')
        else:
            print('invalido')

    elif a == 'invertebrado':
        
        if b == 'inseto':
            if c == 'hematofago':
                print('pulga')
            elif c == 'herbivoro':
                print('lagarta')
            else:
                print('invalido')
        else:
                print('invalido')
                    

        
        if b == 'anelideo':
            if c == 'hematofago':
                print('sanguessuga')
            elif c == 'onivoro':
                print('minhoca')
            else:
                print('invalido')

    else:
        print('invalido')

    return a,b,c

adivinhar(input(), input(), input())


