#Mensaje de Introducción

def mensaje():
        Mensaje =    """       
    -------------------------------------------------------
                               (0 0) 
                       ---oOO-- (_) ----oOO---    
                  ╔══════════════════════════════╗ 
                      CALCULEMOS TU PESO IDEAL    
                         A PARTIR DE TU IMC       
                  ╚══════════════════════════════╝ 
                        -------------------
                              |__|__| 
                               || || 
                              ooO Ooo 
    ------------------------------------------------------- 
            """
        print(Mensaje)

#Cálculo de IMC con Funciones
def calcularIMC(peso,altura):
    peso = float(peso)
    altura = float(altura)
    peso = 0.45*peso;
    IMC = peso/(altura*altura)
    return IMC

def informe(elIMC):

        if elIMC < 18.5:
            print('Te encuentras en bajo peso.')
            print('Aliméntate con más carnes, legumbres, cereales, frutos secos y leche de la que consumes habitualmente, adapta estos alimentos a las 5 comidas diarias.')
        elif elIMC > 18.5 and elIMC < 24.4:
            print('Tu peso es normal actualmente.')
            print('Evita las porciones en distorsión, así no aumentarás de peso y consume alimentos de forma moderada, haz 5 comidas diarias.')
        elif elIMC > 25 and elIMC < 29.9:
            print('Te encuentras en sobrepeso.')
            print('Limita el consumo de calorías y realiza 30 minutos de actividad física diarios, así quemarás la grasa extra.')
        elif elIMC >= 30:
            print('Te encuentas en obesidad.')
            print('Intenta evitar por completo las gaseosas, comida rápida y consume legumbres, frutas, verduras y agua pura. Realiza 30 minutos de actividad física al día.')

#Lógica del Programa
mensaje ()

peso = input('Indica tu peso en lb: ') #lb
altura = input('Indica tu altura en mt: ') #mt

elIMC = calcularIMC(peso,altura)

informe(elIMC)