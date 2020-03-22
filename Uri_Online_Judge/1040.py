nota1,nota2,nota3,nota4 = input().split(" ");
nota1 = float(nota1);
nota2 = float(nota2);
nota3 = float(nota3);
nota4 = float(nota4);
nota1 = nota1 * 2;
nota2 = nota2 * 3;
nota3 = nota3 * 4;
nota4 = nota4 * 1;
media = nota1 + nota2 + nota3 + nota4;
media = media / 10;
if media >= 7.0:
  print("Media: %.1f" %media);
  print("Aluno aprovado.");
elif media < 5.0:
  print("Media: %.1f" %media);
  print("Aluno reprovado.");
elif media >= 5.0 or media <= 6.9:
  print("Media: %.1f" %media);
  print("Aluno em exame.");
  exame = float(input());
  nova_media = exame + media;
  nova_media = nova_media / 2;
  if nova_media >= 5.0:
    print("Nota do exame: %.1f" %exame);
    print("Aluno aprovado.");
    print("Media final: %.1f" %nova_media);
  elif nova_media <= 4.9:
    print("Nota do exame: %.1f" %exame);
    print("Aluno reprovado.");
    print("Media final: %.1f" %nova_media);
