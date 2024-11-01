from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from regiones.forms import DetalleUpdateForm
from .models import Comuna, Detalle, Provincia, Region



def RegionesCatalogo(request):
    # Obtiene todos los registros de la tabla `Regiones`
    Regiones = Region.objects.all()
    return render(request, 'templatesAppRegiones/catalogoRegiones.html', {'Regiones': Regiones})

def ComunasCatalogo(request):
    search_query = request.GET.get('search', '')  # Obtener el término de búsqueda
    
    # Obtener las comunas con filtrado por nombre si hay un término de búsqueda
    comunas = Comuna.objects.filter(comuna_nombre__icontains=search_query) if search_query else Comuna.objects.all()

    # Preparar los datos de comunas y regiones para JSON
    comunas_data = []
    for comuna in comunas:
        # Obtener la provincia y la región relacionadas manualmente
        try:
            provincia = Provincia.objects.get(provincia_id=comuna.provincia_id)
            region = Region.objects.get(region_id=provincia.region_id)
            region_nombre = region.region_nombre
        except (Provincia.DoesNotExist, Region.DoesNotExist):
            region_nombre = "Región no encontrada"

        comunas_data.append({
            'comuna_id': comuna.comuna_id,
            'comuna_nombre': comuna.comuna_nombre,
            'region_nombre': region_nombre
        })

    # Verificar si la solicitud es AJAX y devolver datos JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(comunas_data, safe=False)

    # Si no es AJAX, renderizar el template con los datos de las comunas
    return render(request, 'templatesAppRegiones/catalogoComunasTodas.html', {'comunas': comunas_data})



def detalle_comunas(request, region_id):
    # Obtiene la región por su ID
    region = get_object_or_404(Region, region_id=region_id)
    
    # Obtiene las provincias asociadas al ID de la región
    provincias = Provincia.objects.filter(region_id=region_id)
    
    # Obtiene las comunas relacionadas con las provincias de la región
    comunas = Comuna.objects.filter(provincia_id__in=[prov.provincia_id for prov in provincias])
    
    return render(request, 'templatesAppRegiones/catalogoComunas.html', {'region': region, 'comunas': comunas})



def detalle_comuna(request, comuna_id):
    detalle = get_object_or_404(Detalle, comuna_id=comuna_id)
    comuna = get_object_or_404(Comuna, comuna_id=detalle.comuna_id)
    provincia = get_object_or_404(Provincia, provincia_id=comuna.provincia_id)
    region = get_object_or_404(Region, region_id=provincia.region_id)

    if request.method == "POST":
        if "eliminar" in request.POST:
            comuna.delete()
            response_data = {
                "success": True,
                "message": "La comuna ha sido eliminada correctamente."
            }
            return JsonResponse(response_data)
        else:
            form = DetalleUpdateForm(request.POST, instance=detalle)
            if form.is_valid():
                form.save()
                response_data = {
                    "success": True,
                    "message": "Los cambios se guardaron correctamente."
                }
                return JsonResponse(response_data)
            else:
                response_data = {
                    "success": False,
                    "message": "Por favor, corrige los errores en el formulario."
                }
                return JsonResponse(response_data)
    else:
        form = DetalleUpdateForm(instance=detalle)

    return render(request, 'templatesAppRegiones/detalleComuna.html', {
        'comuna': comuna,
        'detalle': detalle,
        'provincia': provincia,
        'region': region,
        'form': form
    })




def eliminar_comuna(request, comuna_id):
    comuna = get_object_or_404(Comuna, pk=comuna_id)
    if request.method == "POST":
        comuna.delete()
        response_data = {
            "success": True,
            "message": "La comuna ha sido eliminada exitosamente."
        }
        return JsonResponse(response_data)
    else:
        return redirect('catalogo_comunas_todas')
