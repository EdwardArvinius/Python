#!/usr/bin/python


#Edward Arvinius
#CS 270



ans=True
while ans:
    print("""
    1.Add line number
    2.Delete line number
    3.Change file name extension
    4.Backup file
    5.Reverse file
    6.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")

    if ans=="1":
      infile=open('line1.txt', 'r')
      lines=infile.readlines()
      infile.close()
      outtext = ['%d %s' % (i, line) for i, line in enumerate(lines)]
      outfile = open("line1.txt","w")
      outfile.writelines(str("".join(outtext)))
      outfile.close()
      
    elif ans=="2":
      import fileinput
      import string

      for line in fileinput.input("line1.txt", inplace=True):
          print line.translate(None, string.digits),

    elif ans=="3":
      print("\nOld file name:")
      print('file.cxx')
      print("\nNew file name:")
      import os
      print os.path.splitext('file.cxx')[0]+'.cpp'
	
    elif ans=="4":

#     
#	import os
	import shutil
#        backup = ".backup"
#    if not os.path.exists(backup):
#        os.makedirs(backup)
#
#    if os.path.exists(backup):
#        file_path = dir + file
#        
#        # move files into created directory
#        shutil.move(file_path, backup)

    elif ans=="5":
	print("\nBefore reverse")
	f = open('text1.txt', 'r')
	file_contents = f.read()
	print (file_contents)		
	print ("After reverse")		
	for line in reversed(open("text1.txt").readlines()):
    		print line.rstrip()
    elif ans=="6":
      print("\n Goodbye!") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
