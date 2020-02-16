# -*- coding: utf-8 -*-
import sys
import os

comercial_res_col=[10, 12, 15, 18, 20, 22, 24, 27, 30, 33, 39, 47, 51, 56, 62, 68, 75, 82, 91, 100, 120, 150, 180, 200, 220, 240, 270, 300, 330, 390, 470, 510, 560, 620, 680, 750, 820, 910, 1000, 1200, 1500, 1800, 2000, 2200, 2400, 2700, 3000, 3300, 3900, 4700, 5100, 5600, 6200, 6800, 7500, 8200, 9100, 10000, 12000, 15000, 18000, 20000, 22000, 24000, 27000, 30000, 33000, 39000, 47000, 51000, 56000, 62000, 68000, 75000, 82000, 91000, 100000, 120000, 150000, 180000, 200000, 220000, 240000, 270000, 300000, 330000, 390000, 470000, 510000, 560000, 620000, 680000, 750000, 820000, 910000]

def start(func):
    def init ():

        os.system('cls')

        func()

        go_to=str(input('''
        ¿Desea regresar al inicio?

            [Y] Si
            [N] No

            ''')).lower()

        if go_to == 'y':
            run()

        elif go_to == 'n':
            sys.exit()

        else:
            print('Ingrese alguna opción válida')
    return init

@start
def amp_non_inv_basic():

    print('''
    A M P L I F I C A D O R  N O  I N V E R S O R
    ''')
    result= float(input('Ingrese el valor final de la amplificación:  '))
    itered_resul=result+500.1
    aux_amp_non=0.1

    util_range=len(comercial_res_col)


    for i in range(util_range):

        for j in range(util_range):

            aux_amp_non= 1+(comercial_res_col[i]/comercial_res_col[j])

            if abs(result-aux_amp_non)<abs(itered_resul-result):
                itered_resul=aux_amp_non
                R2=comercial_res_col[i]
                R1=comercial_res_col[j]

    error_percent=abs((result-itered_resul)/result)*100
    try:
        print('La mayor aproximaxión a {} es {}'.format(result,itered_resul))
        print('donde 1+({}/{})'.format(R2,R1))
        print('''
                     R2
                _____M_____
             R1 |         |
        .´|---M----|-\    |
                   |  \--------0Vout
          Vin 0----|  /
                   |+/

        ''')
        print('R1 = {}, R2 = {}'.format(R1,R2))
        print('''
        El porcentaje de error es {}%'''.format(error_percent))

    except:
        print('No hay una aproximación cercana factible')

@start
def amp_inv_basic():

    print('''
    A M P L I F I C A D O R  I N V E R S O R
    ''')
    result= float(input('Ingrese el factór de amplificación:  '))
    itered_resul=result+500.1
    aux_amp_inv=0.1

    util_range=len(comercial_res_col)

    for i in range(util_range):

        for j in range(util_range):

            aux_amp_inv= comercial_res_col[i]/comercial_res_col[j]

            if abs(result-aux_amp_inv)<abs(itered_resul-result):
                itered_resul=aux_amp_inv
                R2=comercial_res_col[i]
                R1=comercial_res_col[j]

    try:
        error_percent=abs((result-itered_resul)/result)*100
        print('La mayor aproximaxión a -{} es -{}'.format(result,itered_resul))
        print('donde {}/{}'.format(R2,R1))
        print('''
                     R2
                  _____M_____
               R1 |         |
        Vin 0---M----|-\    |
                     |  \--------0Vout
              .´|----|  /
                     |+/

        ''')
        print('R1 = {}, R2 = {}'.format(R1,R2))
        print('El porcentaje de error es {}%'.format(error_percent))
    except:
        print('No hay una aproximación cercana factible')

@start
def linealizer_resist():
    print('''
    C A L C U L A R   R E S I S T E N C I A   P A R A   L I N E A L I Z A C I Ó N   S E N S O R   R E S I S T I V O
    ''')
    R1= float(input('Ingrese el valor de Rt1 del sensor:  '))
    R2= float(input('Ingrese el valor de Rt2 del sensor:  '))
    R3= float(input('Ingrese el valor de Rt3 del sensor:  '))
    aux_lineal_res=0.1
    aux_lineal_res= (R2*(R1+R3)-(2*R1*R3))/(R1+R3-(2*R2))
    print(aux_lineal_res)
    itered_resul=aux_lineal_res+500.1

    util_range=len(comercial_res_col)

    for i in range(util_range):

        if abs(comercial_res_col[i]-aux_lineal_res)<abs(itered_resul-aux_lineal_res):

            itered_resul=comercial_res_col[i]

    try:
        error_percent=abs((aux_lineal_res-itered_resul)/aux_lineal_res)*100# cambiae
        #res_aprox=
        print('La resistencia {} y su valor comercial aproximado es {}'.format(aux_lineal_res, itered_resul))
        print('''
                0
                |__
                |  |
              RsZ  Z R1
                |__|
                |
                =

        ''')
        print('El porcentaje de error es {}%'.format(error_percent))
    except:
        print('No hay una aproximación cercana factible')

@start
def voltage_divition():

    print('''
    D I V I S O R   D E   V O L T A J E
    ''')
    Vin =float(input('Ingrese el voltaje de alimentación  '))
    result= float(input('Ingrese el valor final del voltaje  '))

    itered_resul=result+500.1
    Vout=0.1

    util_range=len(comercial_res_col)


    for i in range(util_range):

        for j in range(util_range):

            Vout= (Vin*comercial_res_col[i])/(comercial_res_col[i]+comercial_res_col[j])

            if abs(result-Vout)<abs(itered_resul-result):
                itered_resul=Vout
                R2=comercial_res_col[i]
                R1=comercial_res_col[j]

    error_percent=abs((result-itered_resul)/result)*100
    try:
        print('La mayor aproximaxión a {} es {}'.format(result,itered_resul))
        print('donde Vout=({}*{})/{}+{}'.format(Vin, R2, R2, R1))
        print('''
                   Vin
                    o
                    |
                    |
                    Z R1
                    |_____o Vout
                    |
                    z R2
                    |
                    |
                   ___
                    _

        ''')
        print('R1 = {}, R2 = {}'.format(R1,R2))
        print('''
        El porcentaje de error es {}%'''.format(error_percent))

    except:
        print('No hay una aproximación cercana factible')

@start
def paralel_calculate():

    print('''
    R E S I S T E N C I A S   E N   P A R A L E L O
    ''')
    R1= float(input('Ingrese el valor de R1:  '))
    R2= float(input('Ingrese el valor de R2:  '))

    paralel_result=1/((1/R1)+(1/R2))
    aux_amp_inv=0.1
    itered_resul=paralel_result+500.1

    util_range=len(comercial_res_col)

    for i in range(util_range):

        if abs(comercial_res_col[i]-paralel_result)<abs(itered_resul-paralel_result):

            itered_resul=comercial_res_col[i]
    try:
        error_percent=abs((paralel_result-itered_resul)/paralel_result)*100# cambiae
        #res_aprox=
        print('La resistencia {} y su valor comercial aproximado es {}'.format(paralel_result, itered_resul))
        print('''
                0
                |__
                |  |
             R2 Z  Z R1
                |__|
                |
                =

        ''')
        print('El porcentaje de error es {}%'.format(error_percent))
    except:
        print('No hay una aproximación cercana factible')

@start
def paralel_fabricate():

    print('''
    A M P L I F I C A D O R  I N V E R S O R
    ''')
    result= float(input('Ingrese La resistencia a conseguir:  '))
    itered_resul=result+500.1
    res_final=0.1

    util_range=len(comercial_res_col)

    for i in range(util_range):

        for j in range(util_range):

            res_final= 1/((1/comercial_res_col[i])+(1/comercial_res_col[j]))

            if abs(result-res_final)<abs(itered_resul-result):
                itered_resul=res_final
                R2=comercial_res_col[i]
                R1=comercial_res_col[j]

    try:
        error_percent=abs((result-itered_resul)/result)*100
        print('La mayor aproximaxión a {} es {}'.format(result,itered_resul))
        print('donde {}||{}'.format(R2,R1))
        print('''
                0
                |__
                |  |
             R2 Z  Z R1
                |__|
                |
                =

        ''')
        print('R1 = {}, R2 = {}'.format(R1,R2))
        print('El porcentaje de error es {}%'.format(error_percent))

    except:
        print('No hay una aproximación cercana factible')

def run():

    os.system('cls')

    print('C A L C U L O S   R Á P I D O S   D E   E L E C T R Ó N I C A' )
    option=str(input('''

        [A] Amplificador no inversor

        [B] Amplificador inversor

        [C] Divisor de tensión

        [D] Resistencia para linealizar

        [E] Fabricación resitencias paralelo

        [F] Calcular paralelo de resistencias

        [S] salir del programa

    ''')).lower()

    if option == 'a':
        amp_non_inv_basic()

    elif option == 'b':
        amp_inv_basic()

    elif option == 'c':
        voltage_divition()

    elif option == 'd':
        linealizer_resist()

    elif option == 'e':
        paralel_fabricate()

    elif option == 'f':
        paralel_calculate()

    elif option == 's':
        sys.exit()

    else:
        print('Ingrese alguna opción válida')
        run()

if __name__=='__main__':
    run()
