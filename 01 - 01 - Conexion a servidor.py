# #  -   *****    -    ESTABLECIMIENTO DE LA CONEXION   -   *****    -
import paramiko, time

nss=str("54745811304")
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

# # Cierra la conexión
# time.sleep(1)  # Espera final

stdin, stdout, stderr = ssh.exec_command("/PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/localizaUnicos.sh NSS_UNICOS.txt")
respuesta=(stdout.read().decode())
print(respuesta)

# stdin, stdout, stderr = ssh.exec_command("time java -Djava.library.path=/home/weblogic/db-5.3.21/build_unix/.libs -jar PruebaCalculoCoreProd.jar 30825200600")
# print(stdout.read().decode())

# 6. Cerrar la conexión
ssh.close()

''''''
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