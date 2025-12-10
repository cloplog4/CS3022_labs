def make_memoized_fibo():
    fibo_lookup = {}      

    def fibo(n):
        if n in fibo_lookup:
            return fibo_lookup[n]

        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibo(n-1) + fibo(n-2)

        fibo_lookup[n] = result
        return result

    return fibo


def make_memoized_collatz_steps():
    collatz_lookup = {}   

    def collatz_steps(n):
        if n in collatz_lookup:
            return collatz_lookup[n]

        if n == 1:
            result = 0
        elif n % 2 == 0:
            result = 1 + collatz_steps(n // 2)
        else:
            result = 1 + collatz_steps(3*n + 1)

        collatz_lookup[n] = result
        return result

    return collatz_steps


fibo = make_memoized_fibo()
collatz_steps = make_memoized_collatz_steps()




def fibo_birthday_constant(month, day):
    return fibo(month), fibo(day)


def collatz_fibo_birthday(month, day, year):
    f1, f2 = fibo_birthday_constant(month, day)
    return (
        collatz_steps(f1),
        collatz_steps(f2),
        collatz_steps(year)
    )


def pease_number(month, day, year):
    c1, c2, c3 = collatz_fibo_birthday(month, day, year)
    return c1 + c2 + c3



def main():
    print("\nFind your Pease Number ")
    print("\nPlease enter your Birthday")

    month = int(input("Enter month (MM): "))
    day   = int(input("Enter day (DD): "))
    year  = int(input("Enter year (YYYY): "))

    p = pease_number(month, day, year)
    print(f"\nYour Pease Number is: {p}\n")

    return main()

main()
