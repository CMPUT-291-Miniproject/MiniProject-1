class CheckInput:
	"""
	CheckInput allows for the checking of various inputs which various
	tests

	A module to be used in checking user input to consolidate these behaviors
	into one class.
	"""
	def checkLength(self, string, length, checkType = "same"):
		"""
		Checks if the string is of a certain length

		@params
			string: A String object containing the string
				to be checked
			length: A Integer object containing the value
				of the length to check against
			checkType: A String object containing the string
				   that tells the program what kind of check
				   to perform. less, greater and same are valid
				   checks to perform
		"""
		if (checkType == "less"):
			return len(string) <= length
		elif (checkType == "greater"):
			return len(string) >= length
		else:
			return len(string) == length
	def checkAlphaNumeric(self, string):
		"""

		"""
		return string.isalnum()

	def checkAlpha(self, string):
		"""
		Checks if the string contains only
		letters of the alphabet allowing for
		space character

		@params
			string: A String object containing the string
				to be checked
		@return
			Boolean representing whether the string contains
			only letters (and spaces) or not
		"""
		return string.replace(" ", "").isalpha()

	def checkEscape(self, string):
		"""
		Checks if a string is a type of escape character
		
		@params
			string: A String object containing the string
				to be checked
		@returns
			Boolean representing whether the string
			is an escape character or not
		"""
		return string.upper() == "EXIT" or string.upper() == "BACK"

if __name__ == "__main__":
	chkInp = CheckInput()
	print(chkInp.checkLength("Hello", 5))
	print(chkInp.checkLength("Hello", 6, "less"))
	print(chkInp.checkLength("Hello", 6, "greater"))
	
	print("------------------------")


	print(chkInp.checkAlpha("FirstName LastName"))
	print(chkInp.checkAlpha("Name1"))
	print(chkInp.checkAlpha("FirstName"))

	print("------------------------")
		
	print(chkInp.checkAlphaNumeric("asd123"))
	print(chkInp.checkAlphaNumeric("@"))

	print("------------------------")
	
	print(chkInp.checkEscape("ExIt"))
	print(chkInp.checkEscape("BaCk"))
	
	
