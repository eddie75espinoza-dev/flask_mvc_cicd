# Patron MVC implementado con Flask y Click con integración de CI/CD de GitHub Actions.

Ejemplo simple de patron MCV implementado en Flask, PostgreSQL y Click, este ejemplo considera el uso de CI/CD.

### CLI

El **cli** solo retorna un saludo con el nombre que se ingrese.
```bash
python app/cli.p
```
o
```bash
python3.8 -m app.cli
```

### Data Base

Se crea una base de datos en _PostgreSQL_ 

### Front

A través del _cli_ se realiza el renderizado del layaout.html

### CI/CD

Se crea a través de GitHub Actions en cual actualiza el job con cada push al repositorio.
