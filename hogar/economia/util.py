from .models import Operaciones, Salario, Deudas

def OperacionesDelSalario(pk):

    oper = 0

    operacionActual = Operaciones.objects.filter(salario__exact=pk)

    for op in operacionActual:
        if op.tipo_op.tipo.upper() == "ENTRADA":
            oper += op.amount
        else:
            oper -= op.amount

    return oper

def DineroActual():
    salario = Salario.objects.all()
    dineroActual = 0
    operacion = 0

    for sal in salario:
        operacion = OperacionesDelSalario(sal.id)

        dineroActual += sal.amount + operacion

    return dineroActual


def restoSalario(pk):
    resto = 0

    resto += OperacionesDelSalario(pk)

    return resto



