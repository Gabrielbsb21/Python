PI = 3.14159;
A,B,C = input().split(" ");
A = float(A);
B = float(B);
C = float(C);
triangulo = A * C / 2;
circulo = C * C;
circulo = PI * circulo;
trapezio = A + B;
trapezio = trapezio * C / 2;
quadrado = B * B;
retangulo = A * B;
print("TRIANGULO: %.3f" %triangulo);
print("CIRCULO: %.3f" %circulo);
print("TRAPEZIO: %.3f" %trapezio);
print("QUADRADO: %.3f" %quadrado);
print("RETANGULO: %.3f" %retangulo);
