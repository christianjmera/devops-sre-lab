# DevOps & SRE Lab

## Objetivo
Construir un proyecto práctico para demostrar competencias en DevOps,
automatización, contenedores, CI/CD, Kubernetes, GitOps, observabilidad
y prácticas de Site Reliability Engineering (SRE).

## Entorno
- Windows con WSL2
- Ubuntu 26.04
- Git
- Docker Desktop integrado con WSL2
- Python 3.14

## Evolución del proyecto
- [x] Preparación del entorno local
- [x] Configuración de Git
- [x] Instalación y validación de Docker
- [ ] Desarrollo de una aplicación
- [ ] Contenerización con Docker
- [ ] Automatización CI/CD
- [ ] Despliegue en Kubernetes
- [ ] GitOps y observabilidad
- [ ] Prácticas SRE

## Nota
Proyecto personal de laboratorio. Las actividades documentadas reflejarán
únicamente las pruebas realizadas y verificadas.

## Pruebas automatizadas

Activar el entorno virtual e instalar las dependencias de desarrollo:

```bash
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

## Ejecutar las pruebas:

```bash
python -m pytest -v
```

# Docker
## Contruir la Imagen

```bash
docker build -t devops-sre-lab:0.1.0 .
```

## Iniciar el contenedor:
```bash
docker run -d --name devops-sre-api -p 8000:8000 devops-sre-lab:0.1.0
```

## Validar la API:
```bash
curl -i http://localhost:8000/health
curl -i http://localhost:8000/
```

## Comprobar el usuario de ejecución y los logs:

```bash
docker exec devops-sre-api id
docker logs devops-sre-api
```

## Detener y eliminar el contenedor:

```bash
docker rm -f devops-sre-api
```
