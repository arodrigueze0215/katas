# Descripción de la kata #
El objetivo de esta kata es practicar cómo hacer una arquitectura modular dirigida por pruebas.

La funcionalidad va a consistir en implementar el funcionamiento básico de Twitter teniendo en cuenta una serie de restricciones para cada iteración.

## Restricciones
- Haz lo más simple que pueda funcionar.
- Escribe el mejor código que puedas.
- No hagas más de lo que pide la funcionalidad.
- No introduzcas infraestructura si la funcionalidad no lo pide explícitamente.
- No dependas de librerías si la funcionalidad no lo pide explícitamente.

### Iteración 1: 10 min

Un usuario puede registrarse con un nombre de usuario. Por ejemplo: “@veritran"

Si otra persona se ha registrado usando ese mismo nombre de usuario se produce un error.

### Iteración 2: 20 min

Un usuario puede seguir a otros usuarios. Para hacerlo basta con conocer el nickname del usuario al que se quiere seguir.

Cualquiera debe poder consultar a quién sigue un determinado usuario conociendo su nickname.

### Iteración 3: 15 min

Cubrir los siguientes casos borde:

  - Un usuario no se puede seguirse a si mismo
  - Un usuario no puede seguir a un usuario que no existe
  - Un usuario no puede seguir a un usuario que ya sigue

### Iteración 4: 30 min

Los usuarios deben almacenarse de forma durable.

##### Más restricciones para esta iteración:
- No se puede modificar el código escrito hasta ahora.
- Los tests deben de ejecutarse contra la implementación persistente.


### Iteración 5: 30 min

Crear una UI en Android que permita acceder a la funcionalidad desarrollada hasta ahora.

##### Más restricciones para esta iteración:
- Situar el código escrito hasta ahora dentro de un namespace llamado “core”
- Usar el código escrito hasta ahora como si fuera una librería externa.
- El código de esta iteración debe estar en un namespace diferente.
- Ese namespace puede tener una única dependencia del “core”.

### Iteración 6: 30 min

Un usuario puede publicar tweets. El resto de usuarios deben poder consultar todos los tweets que un usuario con un determinado “nickname” ha escrito.

### Iteración 7: 30 min

Crear otro mecanismo de entrega que permita acceder a la funcionalidad desarrollada hasta ahora desde una aplicación de línea de comandos.

##### Aplican las mismas restricciones que en la 4 iteración

### Iteración 7

Poner esta última funcionalidad disponible en los dos mecanismos de entrega y garantizar la durabilidad de los datos.
