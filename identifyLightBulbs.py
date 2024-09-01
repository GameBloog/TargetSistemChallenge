import time

def identificar_lampadas():
    lampadas = {"L1": {"estado": "desligada", "temperatura": "fria"},
                "L2": {"estado": "desligada", "temperatura": "fria"},
                "L3": {"estado": "desligada", "temperatura": "fria"}}
    
   
    lampadas["L1"]["estado"] = "ligada"
    time.sleep(2)  
    lampadas["L1"]["temperatura"] = "quente"  
    
 
    lampadas["L1"]["estado"] = "desligada"
    lampadas["L2"]["estado"] = "ligada"
    

    estado_das_lampadas = {}
    for lampada, propriedades in lampadas.items():
        if propriedades["estado"] == "ligada":
            estado_das_lampadas["Interruptor B"] = lampada
        elif propriedades["temperatura"] == "quente":
            estado_das_lampadas["Interruptor A"] = lampada
        else:
            estado_das_lampadas["Interruptor C"] = lampada
    
    return estado_das_lampadas


resultado = identificar_lampadas()
print("\nMapeamento final dos interruptores para as lâmpadas:")
for interruptor, lampada in resultado.items():
    print(f"{interruptor} controla {lampada}.")
