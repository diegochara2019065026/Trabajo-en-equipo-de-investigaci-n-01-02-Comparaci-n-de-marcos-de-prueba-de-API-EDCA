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
+-- .github/
+   +-- workflows/
+       +-- api-tests.yml
+-- .gitignore
+-- pytest.ini
+-- README.md
+-- requirements.txt
+-- tests/
    +-- conftest.py
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

Ejecutar solo pruebas basicas:

```bash
pytest -m smoke
```

Ejecutar solo pruebas negativas:

```bash
pytest -m negative
```

## Que pruebas incluye

El archivo `tests/test_posts_api.py` contiene pruebas para:

- Consultar un post existente con `GET /posts/1`.
- Probar varios posts usando pruebas parametrizadas.
- Validar que la respuesta tenga codigo HTTP `200`.
- Validar que el JSON tenga campos como `id`, `userId`, `title` y `body`.
- Crear un post de prueba con `POST /posts`.
- Validar que la API responda con codigo HTTP `201`.
- Validar una respuesta de error para un recurso inexistente.

El archivo `tests/conftest.py` contiene fixtures reutilizables:

- `api_client`: sesion HTTP compartida para las pruebas.
- `post_payload`: datos de ejemplo para crear un recurso.

## Ejemplo de prueba

```python
import pytest

from conftest import BASE_URL, REQUEST_TIMEOUT

@pytest.mark.smoke
def test_get_post_by_id(api_client):
    response = api_client.get(f"{BASE_URL}/posts/1", timeout=REQUEST_TIMEOUT)

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
- Permite reutilizar configuracion con fixtures.
- Permite ejecutar grupos de pruebas con markers.
- Permite probar varios escenarios con parametrizacion.
- Se puede integrar en pipelines CI/CD.
- Sirve para validar APIs internas o publicas.
- Facilita la automatizacion de pruebas repetitivas.

## Integracion con GitHub Actions

El repositorio incluye un workflow en:

```text
.github/workflows/api-tests.yml
```

Este workflow instala las dependencias y ejecuta `pytest` automaticamente cuando se hace un `push` o un `pull request`.

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
