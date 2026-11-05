Autor: Jordy Viscaino
Nrc: 36880
Aplicaciones distribuidas
--------------------------------------------------------
## Venta de entradas con Lock

Se simula una taquilla con cinco entradas y ocho clientes que intentan comprarlas al mismo tiempo.

El programa realiza dos pruebas:
Sin Lock varios hilos pueden leer y modificar la cantidad de entradas al mismo tiempo lo que termina en una condicion de carrera y genera datos falsos o inconsistentes.
Con Lock hace que solamente un hilo revise y actualice las entradas a la vez, esto hace que se vendan las 5 entradas y el resto de entradas se meustren como agotadas a los clientes

Ejecutar con Docker Compose:

```bash
docker compose -f docker-compose.extras.yml run --rm venta-entradas
```

Ejecutar sin Docker:

```bash
python 08_venta_entradas_lock.py
```

Al final de cada prueba se muestra el número de ventas, las entradas restantes
y los problemas si hay. 
