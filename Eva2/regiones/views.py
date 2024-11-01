from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import DetalleUpdateForm
from .models import Comuna, Detalle, Provincia, Region

from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegistroForm
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

# Vistas protegidas con @login_required
@login_required
def RegionesCatalogo(request):
    # Obtiene todos los registros de la tabla `Regiones`
    Regiones = Region.objects.all()
    return render(request, 'templatesAppRegiones/catalogoRegiones.html', {'Regiones': Regiones})

@login_required
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

@login_required
def detalle_comunas(request, region_id):
    # Obtiene la región por su ID
    region = get_object_or_404(Region, region_id=region_id)

    # Obtiene las provincias asociadas al ID de la región
    provincias = Provincia.objects.filter(region_id=region_id)

    # Obtiene las comunas relacionadas con las provincias de la región
    comunas = Comuna.objects.filter(provincia_id__in=[prov.provincia_id for prov in provincias])

    # Manejo de la búsqueda dinámica por nombre de comuna
    search_query = request.GET.get('search', None)
    if search_query:
        comunas = comunas.filter(comuna_nombre__icontains=search_query)

    # Si la solicitud es AJAX, devolver un JSON con los resultados
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        comunas_list = [
            {
                'comuna_id': comuna.comuna_id,
                'comuna_nombre': comuna.comuna_nombre,
                'region_nombre': region.region_nombre
            } for comuna in comunas
        ]
        return JsonResponse(comunas_list, safe=False)

    # Si no es una solicitud AJAX, renderiza la página normalmente
    return render(request, 'templatesAppRegiones/catalogoComunas.html', {'region': region, 'comunas': comunas})




@login_required
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

@login_required
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

@login_required
def crear_comuna(request):
    if request.method == "POST":
        comuna_nombre = request.POST.get('comuna_nombre')
        provincia_id = request.POST.get('provincia_id')
        poblacion = request.POST.get('poblacion')
        codigo_postal = request.POST.get('codigo_postal')
        alcalde = request.POST.get('alcalde')
        informacion = request.POST.get('informacion')
        imagen = request.FILES.get('imagen')

        try:
            # Crear el registro de la comuna
            comuna = Comuna.objects.create(
                comuna_nombre=comuna_nombre,
                provincia_id=provincia_id
            )

            # Crear el detalle asociado a la comuna
            detalle = Detalle.objects.create(
                comuna_id=comuna.comuna_id,
                poblacion=poblacion,
                codigo_postal=codigo_postal,
                informacion=informacion,
                alcalde=alcalde,
                imagen=imagen
            )

            response_data = {
                "success": True,
                "message": "La comuna ha sido creada exitosamente."
            }
            return JsonResponse(response_data)

        except Exception as e:
            response_data = {
                "success": False,
                "message": f"Error al crear la comuna: {str(e)}"
            }
            return JsonResponse(response_data)

    else:
        regiones = Region.objects.all()
        provincias = Provincia.objects.all()
        return render(request, 'templatesAppRegiones/crearComuna.html', {
            'regiones': regiones,
            'provincias': provincias
        })

@login_required
def obtener_provincias(request, region_id):
    try:
        provincias = Provincia.objects.filter(region_id=region_id)
        provincias_data = [{'provincia_id': provincia.provincia_id, 'provincia_nombre': provincia.provincia_nombre} for provincia in provincias]
        return JsonResponse({'provincias': provincias_data}, safe=False)
    except Provincia.DoesNotExist:
        return JsonResponse({'provincias': []}, safe=False)





def registro(request):
    if request.user.is_authenticated:
        return redirect('CatalogoRegiones')  # Redirige si ya está autenticado

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            messages.success(request, f'¡Bienvenido, {user.username}! Tu cuenta ha sido creada.')
            return redirect('CatalogoRegiones')  # Redirige a la página principal
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RegistroForm()
    return render(request, 'templatesAppRegiones/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('CatalogoRegiones')  # Redirige si ya está autenticado

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Ya no agregamos el mensaje aquí
                # messages.success(request, f'¡Bienvenido a mi Gagina Fome 2.0 {username}!')

                # Obtener la URL de redirección
                next_url = request.POST.get('next')
                if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    return redirect(next_url)
                else:
                    return redirect('CatalogoRegiones')  # Redirige a la URL deseada
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'templatesAppRegiones/iniciar_sesion.html', {'form': form})


def cerrar_sesion(request):
    # Cierra la sesión del usuario
    logout(request)
    # Borra todos los mensajes de la sesión
    storage = messages.get_messages(request)
    storage.used = True
    # Redirige a la página de inicio de sesión
    return redirect('inicio')
