from django.db import models

## LUEGO DE REALIZAR UNA MODIFICACION EN EL MODELO CORRER:
#  python manage.py makemigrations myapp
#  python manage.py migrate

class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "Profesores"
        ## METADATOS PARA DALRE NOMBRE EN PANEL ADMINISTRADOR
        
    def __str__(self):
        return self.nombre
        # DEVUELVE EL NOMBRE EN PANEL ADMINISTRADOR
    
    
class Curso(models.Model):
    nombre = models.CharField("NOMBRE", max_length=128)
    inscriptos = models.IntegerField("INSCRIPTOS")
    turnos = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"))
    turno = models.PositiveIntegerField("TURNOS", choices=turnos, null=True)

    profesor = models.ForeignKey(
        Profesor, on_delete=models.SET_NULL, null=True, related_name = "cursos")
    ## RELATED NAME HACE REFERENCIA A COMO QUEREMOS LLAMAR AL ATRIBURO DENTRO DE LA TABLA Y ASI TRAER SUS DATOS
    
    def __str__(self):
        return self.nombre
    # DEVUELVE EL NOMBRE EN PANEL ADMINISTRADOR
