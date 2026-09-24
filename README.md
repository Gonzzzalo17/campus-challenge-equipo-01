## Contribuciones - Sesión 03

| Integrante | Requisito trabajado | PR propio | PR revisado |
| :--- | :--- | :--- | :--- |
| **Andrea** | R-03 / R-04 | [PR #2](https://github.com/Gonzzzalo17/campus-challenge-equipo-01/pull/2) | [PR #1](https://github.com/Gonzzzalo17/campus-challenge-equipo-01/pull/1) |
| **Gonzalo** | R-05 / R-06 | [PR #1](https://github.com/Gonzzzalo17/campus-challenge-equipo-01/pull/1) | [PR #2](https://github.com/Gonzzzalo17/campus-challenge-equipo-01/pull/2) |


Preguntas individuales de salida
(Andrea)

- ¿Qué diferencia existe entre guardar, hacer commit y hacer push?

La diferencia es que guardar solo se refiere a salvar el archivo en nuestro Pycharm, Commit se refiere a guardar los puntos de control de mis cambios dentro del historial de git y finalmente el push sube los commits a GitHub y los compañeros pueden ver en la nube. 

-  ¿Qué cambia cuando un compañero fusiona su PR? ¿Qué debes hacer en tu computadora?

Cambia el main porque al hacer eso su codigo nuevo pasa a formar parte de el, en el proyecto GitHub. Lo que se debe es sincronizar y actualizar.

- ¿Qué requisito verifica tu prueba y qué comportamiento incorrecto detectaría?

normalize_answer: Limpia espacios en los extremos y unifica mayúsculas y acentos. Detectaría que el sistema rechace una respuesta correcta solo por un espacio al final o una letra mayúscula.

rotate_left: Maneja casos límite como listas vacías, giros negativos o pasos mayores a la lista. Detectaría errores de índice (IndexError) o fallos al procesar colecciones sin elementos.

- ¿Por qué una prueba nueva que pasa inmediatamente puede ser útil?.

Porque confirma que el código ya cumple con la regla y actúa como una alarma para el futuro