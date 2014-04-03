#! /usr/local/bin/python

import sys
import os
import json
import pdb

commands = {}	

class PhoneBook(object):


	def __init__(self, phonebook_name):
		self.phonebook_name = phonebook_name


	def __setitem__(self, person, mobile):
		with open(self.phonebook_name, "r") as open1:
			data = json.loads(open1.read())
		with open(self.phonebook_name, "w") as open2:
			data[person] = mobile
			open2.write(json.dumps(data))	
		return 	


	def __getitem__(self, person):
		with open(self.phonebook_name) as f:
			data = json.loads(f.read())
		if person in data:
			return person


	def __delitem__(self, person):
		with open(self.phonebook_name, "r") as open1:
			data = json.loads(open1.read())
			del data[person]
		with open(self.phonebook_name, "w") as open2:
			open2.write(json.dumps(data))
		return		


	def _phonebook_exists(self, phonebook_name):
		if phonebook_name[-3:] != ".pb":
			phonebook_name = phonebook_name + ".pb"
		path = os.listdir(sys.path[0])
		if phonebook_name in path:
			return True
		return False		


	def _create_phonebook(self):	
		phonebook_name = self.phonebook_name + ".pb"
		if not self._phonebook_exists(phonebook_name):
			with open(phonebook_name, 'w') as f:
				f.write(json.dumps({}))
			print "Created {0} in the current directory".format(self.phonebook_name)
		else:
			print "Phonebook exists moron!"
		return
		

def main():
	command = sys.argv[1:]
	action = sys.argv[1]
	phonebook_name = sys.argv[-1]
	if action in commands:
		phonebook = PhoneBook(phonebook_name)
		if action != "create":
			try:
				assert phonebook._phonebook_exists(phonebook.phonebook_name) == True
			except AssertionError: 
				print "Phonebook does not exist moron!"
				return	
		return commands[action](phonebook, command)		
	else:
		print "This is not a valid command"
		return


def create(phonebook, data):
	try:
		(action, phonebook_name) = data
	except ValueError:
		print "Command Incorrect. Should be in the following format -->  phonebook create hsphonebook"
		return
	phonebook._create_phonebook()
	return 


def add(phonebook, data):
	try:
		(action, person, mobile, b, phonebook_name) = data
	except ValueError:
		print "Command Incorrect. Should be in the following format -->  phonebook add 'John Michael' '123 456 4323' -b hsphonebook.pb"
		return
	if phonebook[person]:
		print "Error: {0} already in {1}".format(person, phonebook.phonebook_name)
	else:
		phonebook[person] = mobile
		print "{0} added to {1}".format(person, phonebook.phonebook_name)
	return 


def change(phonebook, data):
	try:
		(action, person, mobile, b, phonebook_name) = data
	except ValueError:
		print "Command Incorrect. Should be in the following format --> phonebook change 'John Michael' '234 521 2332' -b hsphonebook.pb"
		return
	if phonebook[person]:
		phonebook[person] = mobile
		print "PhoneBook Updated!"
	else:
		print "Error: {0} not in {1}".format(person, phonebook.phonebook_name)


def lookup(phonebook, data):
	try:
		(action, person, b, phonebook_name) = data
	except ValueError:
		print "Command Incorrect. Should be in the following format --> phonebook lookup 'John' -b hsphonebook.pb"
		return
	with open(phonebook_name) as f:
		phonebook_dict = json.loads(f.read())
		name_present = False
		for each, mobile in phonebook_dict.items():
			if each.startswith(person):
				name_present = True
				print each, phonebook_dict[each]
	if name_present:			
		return
	else:
		print "{0} not in {1}".format(person, phonebook.phonebook_name)
	return				


def reverse_lookup(phonebook, data):
	try:
		(action, mobile, b, phonebook_name) = data
	except ValueError:
		print "Command Incorrect. Should be in the following format --> phonebook reverse-lookup '312 432 5432' -b hsphonebook.pb"
		return
	with open(phonebook_name) as f:
		phonebook_dict = json.loads(f.read())
		name_present = False
		for person, each in phonebook_dict.items():
			if each == mobile:
				name_present = True
				print person, mobile
	if name_present:			
		return
	else:
		print "{0} not in {1}".format(mobile, phonebook.phonebook_name)
	return				


def remove(phonebook, data):
	try:
		[action, person, b, phonebook_name] = data
	except ValueError:
		print "Command Incorrect. Should be in the following format --> phonebook remove 'John Michael' -b hsphonebook.pb"
		return
	if phonebook[person]:
		del phonebook[person]
		print "{0} removed from {1}".format(person, phonebook.phonebook_name)
		return 
	else:	
		print "{0} not in {1}".format(person, phonebook.phonebook_name)	


commands["create"] = create
commands["add"] = add
commands["change"] = change
commands["lookup"] = lookup
commands["reverse-lookup"] = reverse_lookup
commands["remove"] = remove

if __name__ == '__main__':
	main()