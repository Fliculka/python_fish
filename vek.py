
vek = int(input('Kolik ti je let? (zadej číslici)'))

if vek >= 100:
  print('Dobrý den chodící Fosílie, jak sakra vidíš?!?')

elif vek >= 18:
  print('jsi dospělý')

elif vek == -5:
  print('Mám pro tebe dobré informace, za 5 let se narodíš :)')

elif vek <0:
  print('jsi sus, podle dat ti je mene než 0, ZMIZ!')

else:
  print('jsi nezletily')



vek_za_5_let = vek + 5
print('Za 5 let ti bude', vek_za_5_let, 'let.')
