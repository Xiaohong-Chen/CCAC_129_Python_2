# calculate a*b
# with exception handle
def noExceptionHandle():
	while True:
		A = int(input("Input the A value: "))
		B = int(input("Input the B value: "))
		C = A * B
		print(A, "*", B, "=", C)

# try/except Catch and recover from exceptions raised by Python, or by you.
def tryExceptSample():
	while True:
		try:
			A = int(input("Input the A value: "))
			B = int(input("Input the B value: "))
			C = A * B
			print(A,"*",B,"=",C)
		except ValueError:
			print("------Please input an int type value--------")

# try/finally finally block gets executed no matter if the try block raises any errors or not
def tryFinallySample():
	while True:
		try:
			A = int(input("Input the A value: "))
			B = int(input("Input the B value: "))
			C = A * B
			print(A,"*",B,"=",C)
		except ValueError:
			print("------Please input an int type value--------")
		finally:
			print("------Next calculation will begin!----------")

# creating an exception manually in your code.
def raiseSample():

	class myError(Exception): pass

	while True:
		try:
			A = int(input("Input the A value: "))
			B = int(input("Input the B value: "))
			C = A * B
			print(A,"*",B,"=",C)
			raise myError
		except ValueError:
			print("------Please input an int type value--------")
		except myError:
			print("------I catch myError")

# choose one method and test
def main():
	noExceptionHandle()
	#tryExceptSample()
	#tryFinallySample()
	#raiseSample()

main()
