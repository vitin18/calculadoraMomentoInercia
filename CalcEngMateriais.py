
import math
import time


def animacao(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


apresentacao = (
    "Bem-vindo à Calculadora de Engenharia Estrutural!\n"
    "Essa calculadora determinará a área de uma figura (baseando-se nos formatos regulares como, quadrado, triângulo, círculo e semicírculo\n"
    "Junto ao seu momento estático e centro de gravidade\n"
    "Não se preocupe, tudo que você precisará fazer é inserir valores da forma correta\n"
    "Pois assim faremos a conta para você.\n"
)

animacao(apresentacao)
print("\n Dessa forma, vamos calcular a área, o momento estático e o centro de gravidade de várias figuras !!!")

while True:
    area_formas = 0
    menos_area_formas = 0
    momento_estatico_add_y = 0
    momento_estatico_remov_y = 0
    momento_estatico_add_x = 0
    momento_estatico_remov_x = 0

    figuras_add = int(
        input("Quantas figuras você irá adicionar (ex: Vejo 3 quadrados e 2 triangulos, logo 5 no total)?\n"))
    figuras_remov = int(input("Quantas iremos remover (Segue o mesmo principio anterior)?\n"))

    # Adição
    for i in range(0, figuras_add):
        tipo_figura = int(input(f"Qual o tipo de figura está sendo adicionada? (Figura {i + 1})\n"
                                "1- quadrado ou retângulo\n"
                                "2- triângulo\n"
                                "3- círculo\n"
                                "4- semicírculo\n"))

        # Quadrado ou Triângulo
        if tipo_figura == 1 or tipo_figura == 2:
            base = str(input("Quais as coordenadas em X da base? (separar por vírgula)\n")).split(",")
            base_conta = int(base[1]) - int(base[0])
            altura = str(input("Quais as coordenadas em Y da altura? (separar por vírgula)\n")).split(",")
            altura_conta = int(altura[1]) - int(altura[0])
            area = base_conta * altura_conta

            # Quadrado
            if tipo_figura == 1:
                centro_gx = (base_conta / 2) + int(base[0])
                centro_gy = (altura_conta / 2) + int(altura[0])
            # Triângulo
            else:
                area = area / 2
                angulo_reto = str(input("Quais as coordenadas do ângulo reto? (separar por vírgula)\n")).split(",")
                if angulo_reto[0] > base[0]:
                    centro_gx = (-base_conta / 3) + int(angulo_reto[0])
                else:
                    centro_gx = (base_conta / 3) + int(angulo_reto[0])
                if angulo_reto[1] > altura[0]:
                    centro_gy = (-altura_conta / 3) + int(angulo_reto[1])
                else:
                    centro_gy = (altura_conta / 3) + int(angulo_reto[1])

            momento_estatico_add_x += centro_gx * area
            momento_estatico_add_y += centro_gy * area
            area_formas += area

        # Círculo e Derivados
        elif tipo_figura == 3 or tipo_figura == 4 or tipo_figura == 5:
            centro_circulo = str(input("Quais as coordenadas do centro da figura? (separar por vírgula)\n")).split(",")
            raio = int(input("Qual o raio da figura?\n"))
            area = math.pi * (raio ** 2)

            if tipo_figura == 3:
                centro_gx = float(centro_circulo[0])
                centro_gy = float(centro_circulo[1])
            elif tipo_figura == 4:
                area = area / 2
                direction = int(input("Para qual direção está o semicírculo?\n"
                                      "1 - esquerda\n"
                                      "2 - baixo\n"
                                      "3 - direita\n"
                                      "4 - cima\n"))
                if direction == 1 or direction == 3:
                    centro_gy = int(centro_circulo[1])
                    if direction == 1:
                        center_x = -4 * raio / (3 * math.pi)
                    else:
                        center_x = 4 * raio / (3 * math.pi)
                    centro_gx = int(centro_circulo[0]) + center_x
                else:
                    centro_gx = int(centro_circulo[0])
                    if direction == 2:
                        center_y = -4 * raio / (3 * math.pi)
                    else:
                        center_y = 4 * raio / (3 * math.pi)
                    centro_gy = int(centro_circulo[1]) + center_y
            else:
                area = area / 4
                direction = int(input("Em qual quadrante está o ¼ de círculo?\n"
                                      "1 - primeiro\n"
                                      "2 - segundo\n"
                                      "3 - terceiro\n"
                                      "4 - quarto\n"))
                if direction == 1 or direction == 2:
                    centro_gy = int(centro_circulo[1]) + (4 * raio / (3 * math.pi))
                    if direction == 1:
                        center_x = 4 * raio / (3 * math.pi)
                    else:
                        center_x = -4 * raio * (3 * math.pi)
                    centro_gx = int(centro_circulo[0]) + center_x
                elif direction == 3 or direction == 4:
                    centro_gy = int(centro_circulo[1]) - (4 * raio / (3 * math.pi))
                    if direction == 3:
                        center_x = -4 * raio / (3 * math.pi)
                    else:
                        center_x = 4 * raio / (3 * math.pi)
                    centro_gx = int(centro_circulo[0]) + center_x

            momento_estatico_add_x += centro_gx * area
            momento_estatico_add_y += centro_gy * area
            area_formas += area

    # Subtração
    for i in range(0, figuras_add):
        tipo_figura = int(input(f"Qual o tipo de figura está sendo adicionada? (Figura {i + 1})\n"
                                "1- quadrado ou retângulo\n"
                                "2- triângulo\n"
                                "3- círculo\n"
                                "4- semicírculo\n"))

        if tipo_figura == 1 or tipo_figura == 2:
            base = str(input("Quais as coordenadas em X da base? (separar por vírgula)\n")).split(",")
            base_conta = int(base[1]) - int(base[0])
            altura = str(input("Quais as coordenadas em Y da altura? (separar por vírgula)\n")).split(",")
            altura_conta = int(altura[1]) - int(altura[0])
            area = base_conta * altura_conta

            # Quadrado
            if tipo_figura == 1:
                centro_gx = (base_conta / 2) + int(base[0])
                centro_gy = (altura_conta / 2) + int(altura[0])
            else:
                area = area / 2
                angulo_reto = str(input("Quais as coordenadas do ângulo reto? (separar por vírgula)\n")).split(",")
                if angulo_reto[0] > base[0]:
                    centro_gx = (-base_conta / 3) + int(angulo_reto[0])
                else:
                    centro_gx = (base_conta / 3) + int(angulo_reto[0])
                if angulo_reto[1] > altura[0]:
                    centro_gy = (-altura_conta / 3) + int(angulo_reto[1])
                else:
                    centro_gy = (altura_conta / 3) + int(angulo_reto[1])
            momento_estatico_remov_x += centro_gx * area
            momento_estatico_remov_y += centro_gy * area
            menos_area_formas += area
        elif tipo_figura == 3 or tipo_figura == 4 or tipo_figura == 5:
            centro_circulo = str(input("Quais as coordenadas do centro da figura? (separar por vírgula)\n")).split(",")
            raio = int(input("Qual o raio da figura?\n"))
            area = math.pi * (raio ** 2)
            if tipo_figura == 3:
                centro_gx = float(centro_circulo[0])
                centro_gy = float(centro_circulo[1])
            elif tipo_figura == 4:
                area = area / 2
                direction = int(input("Para qual direção está o semicírculo?\n"
                                      "1 - esquerda\n"
                                      "2 - baixo\n"
                                      "3 - direita\n"
                                      "4 - cima\n"))
                if direction == 1 or direction == 3:
                    centro_gy = int(centro_circulo[1])
                    if direction == 1:
                        center_x = -4 * raio / (3 * math.pi)
                    else:
                        center_x = 4 * raio / (3 * math.pi)
                    centro_gx = int(centro_circulo[0]) + center_x
                else:
                    centro_gx = int(centro_circulo[0])
                    if direction == 2:
                        center_y = -4 * raio / (3 * math.pi)
                    else:
                        center_y = 4 * raio / (3 * math.pi)
                    centro_gy = int(centro_circulo[1]) + center_y
            else:
                area = area / 4
                direction = int(input("Em qual quadrante está o ¼ de círculo?\n"
                                      "1 - primeiro\n"
                                      "2 - segundo\n"
                                      "3 - terceiro\n"
                                      "4 - quarto\n"))
                if direction == 1 or direction == 2:
                    centro_gy = int(centro_circulo[1]) + (4 * raio / (3 * math.pi))
                    if direction == 1:
                        center_x = 4 * raio / (3 * math.pi)
                    else:
                        center_x = -4 * raio * (3 * math.pi)
                    centro_gx = int(centro_circulo[0]) + center_x
                elif direction == 3 or direction == 4:
                    centro_gy = int(centro_circulo[1]) - (4 * raio / (3 * math.pi))
                    if direction == 3:
                        center_x = -4 * raio / (3 * math.pi)
                    else:
                        center_x = 4 * raio / (3 * math.pi)
                    centro_gx = int(centro_circulo[0]) + center_x

            momento_estatico_remov_x += centro_gx * area
            momento_estatico_remov_y += centro_gy * area
            menos_area_formas += area

    area_total = (area_formas - menos_area_formas)
    momento_estatico_total = momento_estatico_add_y - momento_estatico_remov_y

    print(area_total)
    print(momento_estatico_total)

    centro_gy_final = momento_estatico_total / area_total
    print(centro_gy_final)

    sair = input("Digite 'SAIR' para parar ou pressione ENTER↵ para continuar: ")

    if sair == 'SAIR':
        break