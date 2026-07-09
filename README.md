# API Testing Framework Example - Pytest + Requests

Este repositorio contiene un ejemplo practico de pruebas de API REST usando **Pytest** y **Requests**.

El objetivo es mostrar como aplicar un marco de prueba de API con ejemplos de codigo reales, validando respuestas HTTP, datos JSON y creacion de recursos.

## Herramientas utilizadas

- **Python**: lenguaje de programacion.
- **Pytest**: framework de pruebas.
- **Requests**: libreria para enviar solicitudes HTTP.
- **JSONPlaceholder**: API publica usada para pruebas.

API usada:

```text
https://jsonplaceholder.typicode.com
```

## Estructura del proyecto

```text
.
+-- README.md
+-- requirements.txt
+-- tests/
    +-- test_posts_api.py
```

## Instalacion

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar pruebas

Ejecutar todas las pruebas:

```bash
pytest
```

Ejecutar con salida detallada:

```bash
pytest -v
```

## Que pruebas incluye

El archivo `tests/test_posts_api.py` contiene pruebas para:

- Consultar un post existente con `GET /posts/1`.
- Validar que la respuesta tenga codigo HTTP `200`.
- Validar que el JSON tenga campos como `id`, `userId`, `title` y `body`.
- Crear un post de prueba con `POST /posts`.
- Validar que la API responda con codigo HTTP `201`.
- Validar una respuesta de error para un recurso inexistente.

## Ejemplo de prueba

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
```

## Por que usar Pytest + Requests

Pytest + Requests es una buena opcion para pruebas de API porque:

- Es facil de instalar.
- Permite escribir pruebas claras y cortas.
- Se puede integrar en pipelines CI/CD.
- Sirve para validar APIs internas o publicas.
- Facilita la automatizacion de pruebas repetitivas.

## Resultado esperado

Al ejecutar `pytest -v`, se espera que todas las pruebas pasen correctamente.

Ejemplo:

```text
tests/test_posts_api.py::test_get_post_by_id PASSED
tests/test_posts_api.py::test_get_posts_list PASSED
tests/test_posts_api.py::test_create_post PASSED
tests/test_posts_api.py::test_get_missing_post_returns_404 PASSED
```

## Conclusion

Este ejemplo demuestra como un marco de pruebas de API puede ayudar a verificar que los endpoints respondan correctamente, que los datos tengan la estructura esperada y que los errores sean manejados de forma adecuada.

En proyectos reales, este tipo de pruebas ayuda a mejorar la calidad del software y reduce errores antes de publicar cambios en produccion.
