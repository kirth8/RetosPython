from ConexionAgentB import agente_b

def agente_a(pregunta):
    print("Agente A recibió la pregunta")
    respuesta_b = agente_b(pregunta)
    return f"Agente A procesa y responde → {respuesta_b}"

if __name__ == "__main__":
    resultado = agente_a("¿Cuál es el sentido de la vida?")
    print(resultado)

