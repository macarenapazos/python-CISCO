###################################################################
#                 Pazos Macarena Lab 4.1.3.6                      #
###################################################################

#Un año bisiesto: escribiendo tus propias funciones

def isYearLeap(year):  #defino la función de año bisiesto
 if not year % 4 and (year % 100 or not year % 400):		#me fijo si es año bisiesto
  return True
 else:
  return False

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
