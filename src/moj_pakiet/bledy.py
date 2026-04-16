def main():
    a = [1,2,3,4,0]
    z = 4
    try:
        x = 9 / a[z]
        open('asdasdasdasd')
    
    except ZeroDivisionError as e:
        print(f'Nie można dzielić przez zero: {e}, {a=}, {z=}')
        raise

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}, args: {e.args}')
        raise