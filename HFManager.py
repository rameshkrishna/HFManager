import platform;
if platform.system()=='Linux':

	print ("you are using Linux Machine");
	filename="/etc/hosts";
	fh =open(filename,"r");
	print ("\n Contents on host file \n");
	print fh.read();
	fh.close();
	fh =open(filename,"a");
	str = raw_input("Enter your input: ");
	print "Received input is : ", str
	fh.write("\n")
	fh.write(str);
	fh.close();
	fh =open(filename,"r");
	print fh.read();
	fh.close();
else:

	print "bye";