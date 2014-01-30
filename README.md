hash.py
=======

hash.py is a python script that calculates a fingerprint (MD5, SHA256, SHA512). The script also allows you to compare two fingerprints to check if it is consistent. It can be used in digital forensics.

Example : 

  r1tch1e@forensic:~$ python hash.py -f /home/myfile -md5
  
  r1tch1e@forensic:~$ python hash.py -f /home/myfile -msx
  
  r1tch1e@forensic:~$ python hash.py -c file1 file2 -md5
  
  r1tch1e@forensic:~$ python hash.py -c file1 file2 -msx


thomas.roccia@gmail.com

@r1tch1e_
