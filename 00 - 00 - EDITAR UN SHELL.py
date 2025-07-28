import paramiko, time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="172.16.5.45",username="weblogic",password="adoimssdigital")

command = """
sed -i '/java/s/^java/#java/' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh
"""
stdin, stdout, stderr = ssh.exec_command(command)
command = """
sed -i '/UNI_HCR2/s/^#//' /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh
"""
stdin, stdout, stderr = ssh.exec_command(command)


# remote_file = "/PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS/kactualizaUNICOS.sh"  # Ruta completa del script en el servidor

# # Leer el contenido actual del archivo
# sftp = ssh.open_sftp()
# with sftp.open(remote_file, 'r') as f:
#     lines = f.readlines()
# sftp.close()

# new_lines = []
# for line in lines:
#     if "UNI_HCR2" in line and line.strip().startswith("#"):
#         # Descomentar la línea de UNI_HCR2
#         new_lines.append(line.lstrip("#"))
#     elif "UNI_HCR1" in line and not line.strip().startswith("#"):
#         # Comentar la línea de UNI_HCR1 (por si acaso)
#         new_lines.append(f"#{line}")
#     else:
#         # Mantener el resto sin cambios
#         new_lines.append(line)

# # Subir el archivo modificado
# with sftp.open(remote_file, 'w') as f:
#     f.writelines(new_lines)
# sftp.close()
# ssh.close()


# channel = ssh.invoke_shell()
# commands = [
#     "cd /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS",
#     "> kactualizaUNICOS.sh",
#     "vi kactualizaUNICOS",
#     "i",
#     "#!/bin/ksh",
#     "\n",
#     "export LD_LIBRARY_PATH=LD_LIBRARY_PATH:/usr/local/BerkeleyDB.5.3/lib",
#     "\n",
#     "cd /PROCESO/imssdigital",
#     chr(27),# ASCII para 'Esc' (sale del modo inserción)
#     ":wq!",
#     "\n"
#     ]

# for cmd in commands:
#     channel.send(cmd)
#     time.sleep(.5)  # Esperar a que el comando se ejecute
    #output = channel.recv(1024).decode()  # Capturar salida
    #print(output)


# # Abre un canal interactivo
# stdin, stdout, stderr = ssh.exec_command("cd /PROCESO/imssdigital/DB/UNICOS/ARGUMENTADOS "
# "&& ls -lrth && >kactualizaUNICOS.sh && vi kactualizaUNICOS.sh && 'i' "
# "&& '#!/bin/ksh\n\nexport LD_LIBRARY_PATH=LD_LIBRARY_PATH:/usr/local/BerkeleyDB.5.3/lib\n\ncd /PROCESO/imssdigital'")




# print (stdout.read().decode())

# channel = ssh.invoke_shell()

# # Envía las líneas una por una
# lines = ["aaa\n", "bbb\n", "ccc\n", "ddd\n"]
# for line in lines:
#     channel.send(line)
#     time.sleep(0.5)  # Espera entre comandos (opcional)

# # Cierra la conexión
# ssh.close()

# #kactualizaUNICOS.sh

# # Abrir shell interactivo
# channel = ssh.invoke_shell()

# # Navegar a la carpeta y ejecutar comandos
# commands = [
#     "cd /ruta/deseada\n",
#     "pwd\n",  # Verificar ruta actual
#     "ls\n"    # Listar archivos
# ]

# for cmd in commands:
#     channel.send(cmd)
#     time.sleep(1)  # Esperar a que el comando se ejecute
#     output = channel.recv(1024).decode()  # Capturar salida
#     print(output)

#     commands = [
#     f"vi {remote_file}",  # Abre el archivo con vi
#     "i",                  # Entra en modo inserción (INSERT)
#     nss,        # Texto que quieres agregar
#     chr(27),              # ASCII para 'Esc' (sale del modo inserción)
#     ":wq!",                # Guarda y sale
#     "\n"                  # Enter para confirmar
# ]
# stdin, stdout, stderr = ssh.exec_command(commands)