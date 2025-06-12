## 🗓️ Weekly Breakdown & Problem Sets

## Week 0: Functions, Variables
- Topics:
  - Functions, return values
  - Variables, types, type conversion
  - `input`, `print`, `int`, `str`, `float`

##  Problem Sets: 0
- ####  Indoor Voice
  ```python
  #ask msg to the user
  message = input("what would you like to say ").lower() # lowercase the letters
  print(message)
  
- ####  Playback Speed
  ```python
  playback = input(" ") #get input from user

  #change whitespace to 3 dots
  print(playback.replace(" " , "..."))

- ####  Making Faces
  ```python
  def main():
    face = input("What's your input? ")
    converted_face = convert(face)
    print(converted_face)

  def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")
  main()

- ####  Einstein
  ```python
  M = int(input("Enter mass in kilograms: "))
  C = int(300000000)
  E = M*C**2

  print ("Energy:", 

- ####  Tip Calculator
  ```python
  def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")  #printing output

  #Converts a dollar string (eg. "$50") to a float (eg 50.0)
  def dollars_to_float(d):
    return float(d.replace("$", ""))
  #Converts a percentage string (eg. "15%") to a float (eg 0.15)
  def percent_to_float(p):
    return float(p.replace("%", ""))/100
  main()    
