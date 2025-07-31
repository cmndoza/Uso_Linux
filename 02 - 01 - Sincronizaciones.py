import paramiko, time
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nss=str("49906345969")
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
proc=str("false")
# Archivo a editar
remote_file = "/PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/NSS_UNICOS.txt"

# 1. Crear el cliente SSH (esto no establece la conexión aún)
ssh = paramiko.SSHClient()
# 2. Configurar políticas de autenticación (ej: aceptar claves desconocidas)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 3. Conectar al servidor
ssh.connect(hostname="172.16.5.45",username="weblogic",password="adoimssdigital")
# 4. Ejecutar un comando remoto
stdin, stdout, stderr = ssh.exec_command("> /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/NSS_UNICOS.txt")
ssh.exec_command(f"echo '{nss}' > {remote_file}")
stdin, stdout, stderr = ssh.exec_command("/PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/klocalizaUnicos.sh NSS_UNICOS.txt")
respuesta_verificacion=(stdout.read().decode())
lineas_respuesta = respuesta_verificacion.split('\n')
for i, linea in enumerate(lineas_respuesta):
    if "Los registros para actualizar son:" in linea:
        ciz_a_corregir = lineas_respuesta[i + 1].strip()
        break

#Para que se comenten todas la líneas
stdin, stdout, stderr = ssh.exec_command("sed -i '/java/s/^java -jar/#java -jar/' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh")

if ciz_a_corregir == "PROCESO TERMINADO":
    print("Inconsistenica NO localizada WÁCHALE BIEN")
    proc=("false")
#Ediciones para CI en CIZ 1
elif ciz_a_corregir == "SSCI_CUENTA_INDIV_REG1_UNICOS.txt":
    stdin, stdout, stderr = ssh.exec_command("sed -i '/UNI_CIR1/s/^#//' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh")
    proc=("true")
#Ediciones para CI en CIZ 2
elif ciz_a_corregir == "SSCI_CUENTA_INDIV_REG2_UNICOS.txt":
    stdin, stdout, stderr = ssh.exec_command("sed -i '/UNI_CIR2/s/^#//' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh")
    proc=("true")
#Ediciones para CI en CIZ 3
elif ciz_a_corregir == "SSCI_CUENTA_INDIV_REG3_UNICOS.txt":
    stdin, stdout, stderr = ssh.exec_command("sed -i '/UNI_CIR3/s/^#//' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh")
    proc=("true")
#Ediciones para HIST de CI en CIZ 1
elif ciz_a_corregir == "SSHC_HIST_CUENTA_REG1_UNICOS.txt":
    stdin, stdout, stderr = ssh.exec_command("sed -i '/UNI_HCR1/s/^#//' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh")
    proc=("true")
#Ediciones para HIST de CI en CIZ 2
elif ciz_a_corregir == "SSHC_HIST_CUENTA_REG2_UNICOS.txt":
    stdin, stdout, stderr = ssh.exec_command("sed -i '/UNI_HCR2/s/^#//' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh")
    proc=("true")
#Ediciones para HIST de CI en CIZ 3
elif ciz_a_corregir == "SSHC_HIST_CUENTA_REG3_UNICOS.txt":
    stdin, stdout, stderr = ssh.exec_command("sed -i '/UNI_HCR3/s/^#//' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh")
    proc=("true")
else:
    print("COMBINACIÓN NO MAPEADA, CORRECCIÓN MÚLTIPLE")
    proc=("false")

if proc=="true":
    time.sleep(1)
    stdin, stdout, stderr = ssh.exec_command("nohup /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh &")
    proc=("true")
    print("SINCRONIZACIÓN COMPLETADA *(^o^)*")




ssh.close()


#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
#''''''
# import paramiko
# import time

# # Configuración de la conexión SSH
# host = "172.16.5.45"
# port = 22
# username = "weblogic"
# password = "adoimssdigital"  # O usa clave SSH
# nss=str("54745811304")

# # Archivo a editar
# remote_file = "/PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/NSS_UNICOS.txt"

# # Comandos para editar con 'vi' (simulando interacción humana)
# commands = [
#     f"vi {remote_file}",  # Abre el archivo con vi
#     "i",                  # Entra en modo inserción (INSERT)
#     nss,                  # Texto que quieres agregar
#     chr(27),              # ASCII para 'Esc' (sale del modo inserción)
#     ":wq!",                # Guarda y sale
#     "\n"                  # Enter para confirmar
# ]

# # Conexión SSH
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(host, port, username, password)

# # Abre un canal interactivo (shell)
# shell = ssh.invoke_shell()

# # Envía los comandos uno por uno con delays (para sincronización)
# for cmd in commands:
#     shell.send(cmd)
#     time.sleep(0.5)  # Espera entre comandos (ajusta según necesidad)

# # Cierra la conexión
# time.sleep(1)  # Espera final
# ssh.close()

# print("Archivo editado exitosamente.")

# Comandos para editar con 'vi'
# commands = [
#     f"vi {remote_file}",  # Abre el archivo con vi
#     "i",                  # Entra en modo inserción (INSERT)
#     nss,        # Texto que quieres agregar
#     chr(27),              # ASCII para 'Esc' (sale del modo inserción)
#     ":wq!",                # Guarda y sale
#     "\n"                  # Enter para confirmar
# ]
# # Abre un canal interactivo (shell)
# shell = ssh.invoke_shell() 
# #A diferencia de exec_command() (que ejecuta comandos individuales sin contexto interactivo), invoke_shell() simula una terminal real, 
# # permitiendo el envío de múltiples comandos en secuencia (como si estuvieras escribiendo en una consola).

# # # Envía los comandos uno por uno con delays (para sincronización)
# for cmd in commands:
#     shell.send(cmd)
#     time.sleep(1.0)  # Espera entre comandos (ajusta según necesidad)