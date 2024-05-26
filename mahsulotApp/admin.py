from django.contrib import admin
from django.utils.html import format_html
from .models import Katalog, SubKatalog, Mahsulot, Rasm, Xususiyat, Rate

class RasmInline(admin.TabularInline):
    model = Rasm
    extra = 1

    def get_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.rasm.url))
    get_image.short_description = 'Image'
    readonly_fields = ('get_image',)

class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('nom', 'narx', 'chegirma', 'miqdor', 'baho', 'rasmlar')
    inlines = [RasmInline]

    def rasmlar(self, obj):
        images = Rasm.objects.filter(mahsulot=obj)
        image_html = ''
        for image in images:
            image_html += format_html('<img src="{}" width="50" height="50" style="margin-right: 5px;" />'.format(image.rasm.url))
        return format_html(image_html)
    rasmlar.short_description = 'Rasmlar'

class KatalogAdmin(admin.ModelAdmin):
    list_display = ('sarlavha', 'get_image')

    def get_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.rasm.url))
    get_image.short_description = 'Rasm'
    readonly_fields = ('get_image',)

class SubKatalogAdmin(admin.ModelAdmin):
    list_display = ('sarlavha', 'get_image', 'katalog')

    def get_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.rasm.url))
    get_image.short_description = 'Rasm'
    readonly_fields = ('get_image',)

class XususiyatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'qiymat', 'mahsulot')

class RateAdmin(admin.ModelAdmin):
    list_display = ('baho', 'izoh', 'mahsulot', 'profil')

admin.site.register(Katalog, KatalogAdmin)
admin.site.register(SubKatalog, SubKatalogAdmin)
admin.site.register(Mahsulot, MahsulotAdmin)
admin.site.register(Xususiyat, XususiyatAdmin)
admin.site.register(Rate, RateAdmin)
