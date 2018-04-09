
# Anti-Duplicator  
  
This tool could help you to find all duplicated files in a specific folder. It scans the folder recursively by default.

### Usage example 

```bash
$ python3 duplicates.py -p ./test\ folder/
We have found next duplicates in the folder: ./test folder/
./test folder/12/3bz1ahdc
./test folder/12/sdfsdfsdf/3bz1ahdc
./test folder/12/newlogo-yinyang.png
./test folder/12/fdf434/34234/newlogo-yinyang.png
./test folder/asdfasd/newlogo-yinyang.png
./test folder/12/fdf434/1234345435345345/some_file.txt
./test folder/asdfasd/some_file.txt
./test folder/234234/some_file.txt

$ python3 duplicates.py -p ./empty_folder/
There are no duplicates in the folder ./empty_folder/
```
  
# Project Goals  
  
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)