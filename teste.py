from armas import armas

arma = armas(10, 15, 5, 3, 4)

arma.definir_efeito('queimadura')

print(arma.efeito.tempo)

