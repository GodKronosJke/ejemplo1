def determinar_anemia(edad, sexo, nivel_hemoglobina):
    tiene_anemia = False
    
    if edad <= 1:
        if nivel_hemoglobina < 13 or nivel_hemoglobina > 26:
            tiene_anemia = True
    elif edad <= 6:
        if nivel_hemoglobina < 10 or nivel_hemoglobina > 18:
            tiene_anemia = True
    elif edad <= 12:
        if nivel_hemoglobina < 11 or nivel_hemoglobina > 15:
            tiene_anemia = True
    elif edad <= 60:  # >= 1 y <= 5 años, > 5 y <= 10 años, > 10 y <= 15 años
        if nivel_hemoglobina < 11.5 or nivel_hemoglobina > 15.5:
            tiene_anemia = True
    else:
        if sexo == 'M':
            if nivel_hemoglobina < 14 or nivel_hemoglobina > 18:
                tiene_anemia = True
        elif sexo == 'F':
            if nivel_hemoglobina < 12 or nivel_hemoglobina > 16:
                tiene_anemia = True
    
    return tiene_anemia

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplos de datos
    edad_paciente = 25  # años
    sexo_paciente = 'M'  # 'M' para masculino, 'F' para femenino
    nivel_hemoglobina_paciente = 13.5  # g%

    # Determinar si el paciente tiene anemia
    tiene_anemia = determinar_anemia(edad_paciente, sexo_paciente, nivel_hemoglobina_paciente)

    # Imprimir resultado
    if tiene_anemia:
        print("El paciente tiene anemia.")
    else:
        print("El paciente no tiene anemia.")
