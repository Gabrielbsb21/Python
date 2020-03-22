num1 = 1;
num2 = 0;
while num1 != num2:
  num1, num2 = input(). split(" ");
  num1 = int(num1);
  num2 = int(num2);
  if num1 > num2:
    print("Decrescente");
  elif num1 < num2:
    print("Crescente");
