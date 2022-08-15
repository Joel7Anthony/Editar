from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Task

# Create your views here.


def list_carro(request):
    task = Task.objects.all()
    context = {
        "task": task[::-1],
        "update_from": None
    }
    return render(request, 'list_carro.html', context)


def insert(request):
    try:
        task_modelo = request.POST['modelo']
        task_año = request.POST['año']
        task_placa = request.POST['placa']
        task_chasis = request.POST['chasis']
        task_propietario = request.POST['propietario']
        if task_modelo == "" or task_año == "" or task_placa == "" or task_chasis == "" or task_propietario == "":
            raise ValueError("El texto no puede estar vacio.")
        task = Task(modelo=task_modelo, año=task_año, placa=task_placa,
                    chasis=task_chasis, propietario=task_propietario)
        task.save()
        return redirect('/carro/')
    except ValueError as err:
        print(err)
        return redirect('/carro/')


def update(request):
    task_id = request.POST["id"]
    task_modelo = request.POST['modelo']
    task_año = request.POST['año']
    task_placa = request.POST['placa']
    task_chasis = request.POST['chasis']
    task_propietario = request.POST['propietario']  
    task = Task.objects.get(pk=task_id)
    task.modelo = task_modelo
    task.año = task_año
    task.placa = task_placa
    task.chasis = task_chasis
    task.propietario = task_propietario
    task.save()
    return redirect('/carro/')


def update_from(request, task_id):
    task = Task.objects.all()
    task_only = Task.objects.get(pk=task_id)
    print(task_only)
    context = {
        "task": task[::-1],
        "update": task_only
    }
    return render(request, 'list_carro.html', context)


def delete_task(request, task_id):
    task = Task.objects.filter(id=task_id)
    task.delete()
    return redirect('/carro/')
