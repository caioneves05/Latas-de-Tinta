larg= float(input('Largura da parede: '))
alt= float(input('Altura da parede: '))
area= larg*alt
tinta= area/2
print('Sua parede tem dimensão de {} x {} e sua área é de {}m².'.format(larg, alt, area))
print('Você precisara de {} latas de tinta para pintar a sua parede'.format(tinta))
