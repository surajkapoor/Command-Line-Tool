Command-Line-Tool
=================

The command line tool operates a phonebook allowing users basic operations, such as add, remove, lookup, modify and delete entries in a phonebook. 

-- to create a new phonebook --
```
$ python clinetool.py create hsphonebook.pb
```

-- to lookup a name --
```
$ python clinetool.py lookup John -b hsphonebook.pb 
```

-- to add an entry --
```
$ python clinetool.py add 'John Michael' '123 456 4323' -b hsphonebook.pb
```

-- to change an entry --
```
$ python clinetool.py change 'John Michael' '234 521 2332' -b hsphonebook.pb
```

-- to remove an entry --
```
$ python clinetool.py remove 'John Michael' -b hsphonebook.pb # error message on not exist
```

-- to lookup by number --
```
$ python clinetool.py reverse-lookup '312 432 5432'
```
