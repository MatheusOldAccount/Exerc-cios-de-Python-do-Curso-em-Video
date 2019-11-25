m = float(input('Uma distância em metros: '))
(m / 1000)
print('A medida de {}m corresponde a \n{}km'.format(m, (m / 1000)))
print('{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format((m / 100), (m / 10), (m * 10), (m * 100), (m * 1000)))



