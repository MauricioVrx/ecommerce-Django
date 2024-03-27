from django.db import models
from category.models import Category
from django.urls import reverse   

# Gamas de colores básicos disponibles en admin Supply
s_color = (
    ("Ninguno", "Ninguno"),
    ('Transparente', 'Transparente'),
    ('Blanco' , 'Blanco'),
    ('Negro' , 'Negro'),
    ('Gris' , 'Gris'),
    ('Rojo' , 'Rojo'),
    ('Azul' , 'Azul'),
    ('Verde' , 'Verde'),
    ('Morado' , 'Morado'),
    ('Celeste' , 'Celeste'),
    ('Amarillo' , 'Amarillo'),
)

# Variedad comunes de distintos tipos de productos disponible en admin Supply
s_size = (
    ("Ninguno", "Ninguno"),
    ("XS" , "XS"),
    ("S" , "S"),
    ("M" , "M"),
    ("L" , "L"),
    ("XL" , "XL"),
    ("XXL" , "XXL"),
    ("XXXL" , "XXXL"),
    ("11 Oz" , "11 Oz"),
    ("15 Oz" , "15 Oz"),
    ("12x24 cm" , "12x24 cm"), #MousePad Pequeño
    ("30x60 cm" , "30x60 cm"), #MousePad Grande
)

# Clasificación de tipo de tag para diferencialos al momento de crearlos de manera recursiva
t_type = (
    ("Categoría","Categoría"),
    ("Contenedor","Contenedor"),
    ("Información","Información"),
)


### ---  Create your models here.


# Color
class Color(models.Model):
    color_name      = models.CharField(max_length=50)
    color_hex       = models.CharField(max_length=10)
    opp             = models.CharField(max_length=10)

    def __str__ (self):
        return self.color_name 


# Insumo con su tamaño, color, stock, etc - Ejemplo: Polera(FK), Color Rojo, talla XL, stock: 30
class Supply(models.Model):
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    supply_type     = models.CharField(max_length=50)
    size            = models.CharField(max_length=30, choices=s_size)
    color           = models.ForeignKey(Color, on_delete=models.CASCADE)
    supply_name     = models.CharField(max_length=250, unique = True) # Ver str()
    stock           = models.PositiveIntegerField()
    min_stock       = models.PositiveIntegerField()
    active_stock    = models.PositiveIntegerField()
    cost            = models.PositiveIntegerField()
    min_price       = models.PositiveIntegerField()
    price           = models.PositiveIntegerField()
    weight          = models.FloatField()
    is_active       = models.BooleanField(default = False)
    description     = models.CharField(max_length = 255, blank = True)

    created_date    = models.DateTimeField(auto_now_add = True)
    modified_date   = models.DateTimeField(auto_now     = True)

    class Meta: 
        verbose_name = 'supply' 
        verbose_name_plural = 'supplies' 

    def __str__ (self):
        return self.supply_name 


# class SupplyForm(ModelForm):
#     class Meta:
#         model = Supply
#         fields = ['active_stock', 'category', 'color', 'cost', 'description', 'is_active', 'min_price', 'min_stock', 'price', 'size', 'stock', 'supply_name', 'supply_type', 'weight', 'category', 'supply_slug']



# Estos Tags vinculados a los productos nos ayudará a catalogar, ordenar, filtrar y mostrar mejores resultados
# Tabla recursiva que nos permite por información relevante , contenedores e informacion  que tendrán dicho contenerdor  
class Tag(models.Model):
    tag_container   = models.ForeignKey(
        "self",
        on_delete=models.CASCADE, 
        blank = True, 
        null = True
    )
    tag_info        = models.CharField(max_length = 50)
    tag_type        = models.CharField(max_length = 50, choices = t_type) 

    def __str__ (self):
        return f"{self.tag_info} - {self.tag_type}"



# Producto visible en la tienda antes de ser visualizada - Ejemplo: Polera(FK), Ilustración NewbieType,
class Product(models.Model):
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name    = models.CharField(max_length = 255) 
    product_price   = models.PositiveIntegerField(blank = True)
    product_image   = models.ImageField(upload_to = f'photos/products/main', blank = True)
    description     = models.TextField(max_length = 700)
    is_active       = models.BooleanField(default = False)
    limited         = models.IntegerField(default = -1)
    tags            = models.ManyToManyField(Tag)
    supply_resource = models.ManyToManyField(Supply, through="Conection_Product_Supply" )
    colors          = models.ManyToManyField(Color,  through="Product_Color_Img" )
    slug            = models.CharField(max_length = 200, blank = True) # PENDIENTE - str(product_name) 
    created_date    = models.DateTimeField(auto_now_add = True)
    modified_date   = models.DateTimeField(auto_now     = True)

    def __str__ (self):
        return f"{self.product_name}"

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

# # Tabla rompimiento muchos-a-muchos entre Supply y Productos que vincularizará el stock de los productos disponibles junto a la ilustración
# # Habrá multiple intancias ya que cada producto tendra varios colores y tamaños
class Conection_Product_Supply(models.Model):
    supply          = models.ForeignKey(Supply,   on_delete=models.CASCADE)
    product         = models.ForeignKey(Product,  on_delete=models.CASCADE)
    ps_stock        = models.PositiveIntegerField(default = 0, blank = True)
    is_active       = models.BooleanField(default = False, blank = True)

    created_date    = models.DateTimeField(auto_now_add = True)
    modified_date   = models.DateTimeField(auto_now     = True)

    class Meta: 
        verbose_name = 'Product supply' 
        verbose_name_plural = 'Product supplies' 

    def __str__ (self):
        return f"{self.product} - {self.supply}"
    

class Product_Color_Img(models.Model):
    product         = models.ForeignKey(Product,  on_delete=models.CASCADE)
    color           = models.ForeignKey(Color,  on_delete=models.CASCADE)
    product_images  = models.ImageField(upload_to = f'photos/products/colors', blank = True)
    is_active       = models.BooleanField(default = False, blank = True)

    created_date    = models.DateTimeField(auto_now_add = True)
    modified_date   = models.DateTimeField(auto_now     = True)

    def __str__ (self):
        return f"{self.product} - {self.color}"