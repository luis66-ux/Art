from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




@login_required
def index(request):
    return render(request, 'gestionusuario/index.html')


@login_required
def profile(request):
    return render(request, 'gestionusuario/profile.html')

@login_required
def grupo(request):
    return render(request, 'gestionusuario/grupo.html')


@login_required
def crearart(request):
    if request.method == 'POST':
        supervisor = request.POST.get('supervisor')
        empresa = request.POST.get('empresa')
        gerencia = request.POST.get('gerencia')
        fecha = request.POST.get('fecha')
        hora_inicio = request.POST.get('hora_inicio')
        hora_termino = request.POST.get('hora_termino')
        superintendencia = request.POST.get('superintendencia')
        lugar_especifico = request.POST.get('lugar_especifico')
        trabajo_a_realizar = request.POST.get('trabajo_a_realizar')

        # Aquí puedes imprimir o procesar los datos como lo necesites
        print(f'Supervisor: {supervisor}')
        print(f'Empresa: {empresa}')
        print(f'Gerencia: {gerencia}')
        print(f'Fecha: {fecha}')
        print(f'Hora inicio: {hora_inicio}')
        print(f'Hora término: {hora_termino}')
        print(f'Superintendencia/Dirección: {superintendencia}')
        print(f'Lugar específico: {lugar_especifico}')
        print(f'Trabajo a realizar: {trabajo_a_realizar}')

        # Por ejemplo, podrías guardar los datos en la base de datos aquí

        # Retornar una respuesta indicando que los datos han sido procesados
        #return HttpResponse('Datos procesados correctamente')
        return redirect('crearart2')
    # Si el método de solicitud no es POST, simplemente renderiza el template inicial
    return render(request, 'gestionusuario/crearart.html')

@login_required

def crearart2(request):
    if request.method == 'POST':
        pregunta_1 = request.POST.get('pregunta_1')
        pregunta_2 = request.POST.get('pregunta_2')
        pregunta_3 = request.POST.get('pregunta_3')
        pregunta_4 = request.POST.get('pregunta_4')
        pregunta_5 = request.POST.get('pregunta_5')
        pregunta_6 = request.POST.get('pregunta_6')

        # Aquí puedes imprimir o procesar los datos como lo necesites
        print(f'Pregunta 1: {pregunta_1}')
        print(f'Pregunta 2: {pregunta_2}')
        print(f'Pregunta 3: {pregunta_3}')
        print(f'Pregunta 4: {pregunta_4}')
        print(f'Pregunta 5: {pregunta_5}')
        print(f'Pregunta 6: {pregunta_6}') 

        return redirect('crearart3')
    
    return render(request, 'gestionusuario/crearart2.html')

@login_required
def crearart3(request):

    if request.method == 'POST':
        # Procesar el formulario enviado
        nombre = request.POST.get('nombre', '')  # Obtener el nombre del formulario
        
        # Iterar sobre las opciones seleccionadas
        for i in range(1, 31):  # Iterar sobre las 30 preguntas
            opcion_si = request.POST.get(f'opcion_{i}', '')  # Obtener la respuesta Si
            opcion_no = request.POST.get(f'opcion_{i}', '')  # Obtener la respuesta No
            
            # Imprimir las opciones seleccionadas
            print(f"Pregunta {i}:")
            print(f"  - Opción Si seleccionada: {opcion_si}")
            print(f"  - Opción No seleccionada: {opcion_no}")

        return redirect('crearart4')    

    return render(request, 'gestionusuario/crearart3.html')

@login_required
def crearart4(request):
    if request.method == 'POST':
        riesgos = []
        medidas_control = []
        for i in range(1, 9):
            riesgo = request.POST.get(f'riesgo{i}')
            medida_control = request.POST.get(f'medida_control{i}')
            riesgos.append(riesgo)
            medidas_control.append(medida_control)
        
        # Imprimir los datos capturados en la consola
        print("Riesgos:", riesgos)
        print("Medidas de Control:", medidas_control)
        
        # Aquí puedes añadir el procesamiento adicional que necesites
        
        return redirect('crearart5')
    
    # Pasar una lista de números al contexto de la plantilla
    context = {'range': range(8)}
    return render(request, 'gestionusuario/crearart4.html', context)


@login_required
def crearart5(request):
    if request.method == 'POST':
        pregunta_1 = request.POST.get('pregunta_1')
        pregunta_2 = request.POST.get('pregunta_2')
        pregunta_3 = request.POST.get('pregunta_3')
        pregunta_4 = request.POST.get('pregunta_4')
        pregunta_5 = request.POST.get('pregunta_5')
        pregunta_6 = request.POST.get('pregunta_6')
        pregunta_7 = request.POST.get('pregunta_7')
        pregunta_8 = request.POST.get('pregunta_8')

        # Imprimir los datos en la consola
        print(f'Pregunta 1: {pregunta_1}')
        print(f'Pregunta 2: {pregunta_2}')
        print(f'Pregunta 3: {pregunta_3}')
        print(f'Pregunta 4: {pregunta_4}')
        print(f'Pregunta 5: {pregunta_5}')
        print(f'Pregunta 6: {pregunta_6}')
        print(f'Pregunta 7: {pregunta_7}')
        print(f'Pregunta 8: {pregunta_8}')

        #return redirect('crearart5')

    return render(request, 'gestionusuario/crearart5.html')    