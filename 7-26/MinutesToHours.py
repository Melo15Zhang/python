import sys


def Hours(min):
	h = 0
	m = 0
	if min < 0:
		raise ValueError("Input number cannot be negative")
	else:
		h,m = divmod(min, 60)
		print("{} H, {} M".format(h, m))


if __name__ == '__main__':
    try:
        Hours(int(sys.argv[1]))
    except ValueError:
        print("ValueError: Input number cannot be negative")



