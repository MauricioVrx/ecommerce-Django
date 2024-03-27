from django.contrib import admin
from .models import Tag, Supply, Product, Conection_Product_Supply, Color


class Conection_Product_SupplyInLine(admin.TabularInline):
    model = Product.supply_resource.through

class ColorLine(admin.TabularInline):
    model = Product.colors.through

class Product_admin(admin.ModelAdmin):
    list_display        = ('product_name' , 'category' , 'product_price', 'is_active') # , 'get_supply'
    prepopulated_fields = {'slug' : ('category','product_name',)}
    fields              = ["category","product_name", "product_price","product_image", "slug", "description", "tags", "limited",  "is_active"]
    inlines             = [ColorLine, Conection_Product_SupplyInLine]

    # def get_supply(self, obj):
    #     return [f"\n  {p.supply_name}" for p in obj.supply_resource.all()]


class Supply_admin(admin.ModelAdmin):
    list_display = ('id','supply_name' , 'category' ,'stock' , 'min_stock', 'is_active')
    prepopulated_fields = {'supply_name' : ('supply_type','color', 'size',)}


class Tag_admin(admin.ModelAdmin):
    list_display = ('id', 'tag_info', 'tag_container',  'tag_type')
  

class Conection_Product_Supply_admin(admin.ModelAdmin):
    list_display = ('product' , 'supply' , 'ps_stock', 'is_active')

class Color_admin(admin.ModelAdmin):
    list_display = ('color_name' , 'color_hex' , 'opp')


# Register your models here.
admin.site.register(Supply, Supply_admin)
admin.site.register(Tag, Tag_admin)
admin.site.register(Product, Product_admin)
admin.site.register(Conection_Product_Supply,Conection_Product_Supply_admin)
admin.site.register(Color, Color_admin)
