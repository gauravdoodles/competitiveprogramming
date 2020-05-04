# Python program to illustrate 
# Append vs write mode 
if __name__ == '__main__':

	file1 = open("C:/Windows/System32/drivers/etc/hosts", "a") 
	L = ["216.239.38.120 www.google.com \n", "204.79.197.220 www.bing.com \n"] 
	file1.writelines(L) 
	file1.close() 


