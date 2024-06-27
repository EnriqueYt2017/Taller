from .Mindicator import Mindicador
from datetime import datetime

def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}

def total_carrito_usd(request):
    mindicador = Mindicador('dolar', datetime.now().strftime ("%d-%m-%Y")).InfoApi()
    dolar = mindicador.get('serie')[0].get('valor')
    total_clp = total_carrito(request).get("total_carrito")
    total = round(total_clp / dolar, 2)
    return {"total_carrito_usd": total}