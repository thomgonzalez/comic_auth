# Comics Auth User

En esta segunda parte se busca crear un microservicio capaz de administrar a los
usuarios, dicho microservicio deberá de registrar los usuarios en una base de datos
de MongoDB Atlas, deberá de cumplir con los siguientes criterios:

CA1: Los usuarios nuevos tendra la posibilidad de registrarse sin ningún
requisito.

CA2: Como usuario registrado, tengo la posibilidad de consultar mis datos
ingresando usuario y contraseña.

CA3: Al presentar mis credenciales correctas debo de recibir un Token único
que me identifique como usuario autenticado.

# SO - Ubuntu Linux

La aplicación fue probada en Ubuntu 20.04, instalar las siguientes dependencias.
    
Paso 1: Install Docker

Paso 2: Instalar Docker Compose

Paso 3: Instalar make

    ```sudo apt install make
    ```
    
# Getting Started with Create App on Docker

Paso 1: Contruir los contenedores, imagenes y volumenes.

    ```
    make build_dev
    ```
Paso 2: Ejecutar app en desarrollo corre en el puerto 8000.
    
    ```
    make run_dev
    ```

Extras:
  En caso de tener problemas con los permisos del directorio, correr el siguiente comando:
  ```
  sudo chown -R your-user:your-user /home/iamroot/repo/comic_auth/postgres_data
  ```
  
  Alternativa de correr migraciones manualmente. 
  ```
  docker exec -i comic_backend python manage.py makemigrations

  docker exec -i comic_backend python manage.py migrate
  ```
  
  
    
# Endpoints searchComics
 
POST User Register
```
curl --location --request POST 'http://localhost:8000/api/users/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "tomas",
    "password": "1234",
    "email": "tsantiago@gmail.com",
    "first_name": "Tomas",
    "age": 30
   
}'
```

POST Get Data the User 
```
curl --location --request POST 'http://localhost:8000/api/users/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "tomas",
    "password": "1234"
}'
```
