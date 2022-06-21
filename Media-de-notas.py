n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda note: '))
media = (n1 + n2) /2
if media < 5:
    print('Tirando {:.1f} e {:.1} a media foi {:.1f} e o aluno esta Reprovado'.format(n1,n2,media))
elif 7 > media >= 5:
    print('Tirando {:.1f} e {:.1f} A media foi {:.1f} e O aluno está em recuperação'.format(n1,n2,media))
else:
    print('Tirando {:.1f} e {:.1f} A media foi {:.1f} e O Aluno foi aprovado'.format(n1,n2,media))