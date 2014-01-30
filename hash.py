#!/usr/bin/python
# Author : Thomas.roccia@gmail.com [@r1tch1e_]
# Date : 30/01/2014

import sys
import getopt
import hashlib

def usage():
	print '**********************************************************************'
	print '*          Calculate Hash | by R1tch1e (Thomas ROCCIA)               *'
	print '*                                                                    *' 
	print '*              Usage : hash.py [FILEPATH] [OPTIONS]                  *'
	print '*              -h or --help : Display the help                       *'
	print '*              -f or --filepath : Put your filename                  *' 
	print '*              -m or --md5 : Calculate a MD5 hash                    *'
	print '*              -s or --sha256 : Calculate a SHA256 hash              *'
	print '*              -x or --sha512 : Calculate a SHA512 hash              *'
	print '*	       -c or --compare : Compare two hashfile	 	     		*'
	print '*                                                                    *'
	print '*  Example : r1tch1e@forensic:~$ python hash.py -f /home/myfile -md5 *'
	print '*  Example : r1tch1e@forensic:~$ python hash.py -c file1 file2 -md5  *'
	print '**********************************************************************' 

def hashmd5(filename):
	fichier = open(filename, 'r')
	c = hashlib.md5()
	while 1:
		try:
			d = fichier.next()
			c.update(d)
		except: break
	fichier.close()
	return c.hexdigest()

def hashsha2(filename):
        fichier = open(filename, 'r')
        c = hashlib.sha256()
        while 1:
                try:
                        d = fichier.next()
                        c.update(d)
                except: break
        fichier.close()
        return c.hexdigest()

def hashsha5(filename):
        fichier = open(filename, 'r')
        c = hashlib.sha512()
        while 1:
                try:
                        d = fichier.next()
                        c.update(d)
                except: break
        fichier.close()
        return c.hexdigest()

def compare(file1, file2):
	if sys.argv[4] == "-m" or sys.argv[4] == "--md5":
		filename = file1
		hash1 = hashmd5(filename)
		filename = file2
		hash2 = hashmd5(filename)
	elif sys.argv[4] == "-s" or sys.argv[4] == "--sha256":
		filename = file1
		hash1 = hashsha2(filename)
		filename = file2
		hash2 = hashsha2(filename)	
	elif sys.argv[4] == "-x" or sys.argv[4] == "--sha512":
		filename = file1
		hash1 = hashsha5(filename)
		filename = file2
		hash2 = hashsha5(filename)
	else:
	        usage()
	        sys.exit(2)
	
	if hash1 == hash2:
		print "This is the same file ! :)" 
		print hash1, file1
		print hash2, file2 
	else:
		print "This is not the same file ! :("
		print hash1, file1
		print hash2, file2

try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:msxc", ["help", "filepath", "md5", "sha256", "sha512"])
except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

output = None
verbose = True

for o, a in opts:
        if o in ("-h", "--help"):
                usage()
                sys.exit()
	elif o in ("-f", "--filepath"):
                output = a
		filename = a        
	elif o in ("-m", "--md5"):
		print 'The MD5 hash is', hashmd5(filename)
	elif o in ("-s", "--sha256"):
		print 'The SHA256 hash is', hashsha2(filename)
	elif o in ("-x", "--sha512"):
		print 'The SHA512 hash is', hashsha5(filename)
	elif o in ("-c"):
		file1 = sys.argv[2]
		file2 = sys.argv[3]
		compare(file1, file2)
