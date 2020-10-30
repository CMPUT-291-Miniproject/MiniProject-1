class CheckInput:
	def checkLength(self, string, length, checkType = "same"):
		if (checkType == "less"):
			return len(string) <= length
		elif (checkType == "greater"):
			return len(string) >= length
		else:
			return len(string) == length
	def checkAlphaNumeric(self, string):
		return string.isalnum()

	def checkAlpha(self, string):
		return string.replace(" ", "").isalpha()

	def checkEscape(self, string):
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
	
	
