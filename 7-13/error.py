# 推荐使用else的情况 即没有任何异常的情况下执行的语句
# 无论在任何情况下都会执行的清理行为


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


def divide_2(x, y):
    try:
        result = x / y
        print("result is", result)
    except ZeroDivisionError:
        print("division by zero!")
    finally:
        print("executing finally clause")


divide_2(2, 1)

divide_2(2, 0)

# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("test2.txt") as f:
    for line in f:
        print(line, end="")

# 当执行完毕后，文件会保持打开状态，并没有被关闭
for line in open("test2.txt"):
    print(line, end="")

print("\n");
# 定义函数
# 处理带有参数的异常的方法如下


def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print("参数没有包含数字\n", Argument)


# 调用函数
temp_convert("xyz");

