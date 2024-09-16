import pdb
def add(a, b):
    return a + b

def main():
    x = 5
    y = 10; pdb.set_trace()  # 在此处设置断点
    result = add(x, y)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()