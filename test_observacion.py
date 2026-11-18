from observacion import Observacion
import pytest

instancia = Observacion("AEROPARQUE AERO", 1, 8.6, 66, 11)

def test_comprobar_atributos():
    assert instancia.estacion == "AEROPARQUE AERO"
    assert instancia.hora == 1
    assert instancia.temperatura == 8.6
    assert instancia.humedad == 66
    assert instancia.velocidad_viento == 11

def test_validacion_invalida():
    with pytest.raises(ValueError):
        Observacion("", 1, 8.6, 66, 11)
