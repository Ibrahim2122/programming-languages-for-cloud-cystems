# S3_LAM_01.py

square = lambda n: n * n
is_odd = lambda n: n % 2 == 1
greet = lambda name: f"Hello, {name}!"


def main():
    print("square tests:", square(2), square(0), square(-3))
    print("is_odd tests:", is_odd(1), is_odd(2), is_odd(99))
    print("greet tests:", greet("Ola"), greet("Ala"), greet("Zenek"))


if __name__ == "__main__":
    main()
