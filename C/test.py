import subprocess
 
cmd = "test.c"
print ("Hey this is Python Script Running\n")
subprocess.call(["gcc",cmd]) #For Compiling



somevalue = "100"

a = subprocess.call("test %s"%somevalue)
print(a)

