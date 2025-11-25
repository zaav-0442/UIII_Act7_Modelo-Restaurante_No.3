from django.db import models

# ================================
#           PLATOS
# ================================
class Plato(models.Model):
    nombre_plato = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")
    ingredientes = models.TextField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_plato


# ================================
#            MESAS
# ================================
class Mesa(models.Model):
    numero_mesa = models.IntegerField(unique=True)
    capacidad = models.IntegerField()
    estado_mesa = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    es_reservable = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Mesa {self.numero_mesa}"


# ================================
#         EMPLEADOS
# ================================
class EmpleadoRestaurante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cargo})"


# ================================
#            PEDIDOS
# ================================
class Pedido(models.Model):
    fecha_pedido = models.DateTimeField()
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    empleado = models.ForeignKey(EmpleadoRestaurante, on_delete=models.SET_NULL, null=True)
    estado_pedido = models.CharField(max_length=50)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pedido = models.CharField(max_length=50, help_text="Ej: en mesa, para llevar")
    hora_pedido = models.TimeField()

    def __str__(self):
        return f"Pedido {self.id} - Mesa {self.mesa.numero_mesa}"


# ================================
#       DETALLE DEL PEDIDO
# ================================
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="detalles")
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    notas_plato = models.TextField(blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento_item = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cantidad} x {self.plato.nombre_plato} (Pedido {self.pedido.id})"


# ================================
#           CLIENTES
# ================================
class ClienteRestaurante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_registro = models.DateField()
    preferencias_alimentarias = models.TextField(blank=True)
    puntos_fidelidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ================================
#           RESERVAS
# ================================
class Reserva(models.Model):
    cliente = models.ForeignKey(ClienteRestaurante, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    num_personas = models.IntegerField()
    estado_reserva = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Reserva {self.id} - Mesa {self.mesa.numero_mesa}"

