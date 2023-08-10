import requests

equation = input("Enter your Equation: ")
result = 'https://newton.vercel.app/api/v2/simplify' + equation
data = requests.get(result).json()
print('operations for the given Equation:', data['operation'])
print("Expression of the given equation", data['expression'])
print("result of given Equation", data['result'])