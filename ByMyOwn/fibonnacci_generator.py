def fibonnaci_generator(limite):
    a, b = 0, 1

    while a < limite:
        yield a

        # essa linha só executa na próxima chamada next()
        a, b = b, a + b
        print(f"(Gerador retomado, próximos valores são a={a}, b={b})")


# criação de um objeto generator
fib = fibonnaci_generator(30)
print(f"Tipo do objeto criado: {type(fib)}\n")

print("Consumindo com next():")
print(f"Valor 1: {next(fib)}")
print(f"Valor 2: {next(fib)}")
print(f"Valor 3: {next(fib)}")
print("-" * 20)

print("Consumindo o restante com um laço for:")
for numero in fib:
    print(f"Valor: {numero}")
