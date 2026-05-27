# tower_of_hanoi.py : Program to solve Tower of Hanoi problem using recursion.

def tofh(ndisk, source, temp, dest):
	if ndisk == 1:
		print(f"Move Disk {ndisk} from {source}-->{dest}")
		return

	tofh(ndisk-1, source, dest, temp)
	print(f"Move Disk {ndisk} from {source}-->{dest}")
	tofh(ndisk-1, temp, source, dest)

if __name__ == '__main__':
	source='A'
	temp='B'
	dest='C'

	ndisk = 3

	print("Sequence is :")
	tofh(ndisk, source, temp, dest)
