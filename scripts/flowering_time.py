#!/bin/env python
import sys
import datetime

if len(sys.argv) == 1:
    print('\n Usage:')
    print('   flowering_time [data inicial: dd/mm/yyyy] [semanas]\n')
    sys.exit(1)
else:
    date = sys.argv[1].split('/')
    weeks = 9
    if len(sys.argv) >= 3:
        weeks = int(sys.argv[2])


    start = datetime.datetime(year=2020, month=7, day=7)
    end = start + datetime.timedelta(weeks=weeks)

    print()
    print(' Início da floração: .... {}'.format(start.strftime('%d/%m/%Y')))
    print(' Período: ............... {} semanas'.format(weeks))
    print(' Fim da floração: ....... {}'.format(end.strftime('%d/%m/%Y')))
    print()

    for i in range(weeks + 1):
        
        _date = start + datetime.timedelta(weeks=i)

        if i == 0:
            print('   {} - início'.format(
                _date.strftime('%d/%m'),
                i,
            ))
        else:
            info = ''
            if i == weeks - 2:
                info = '(flush)'
            if i == weeks:
                info = '(colheita)'

            print('   {} - semana {} {}'.format(
                _date.strftime('%d/%m'),
                i,
                info
            ))

    print()
