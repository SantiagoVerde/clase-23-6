from fastapi import APIRouter
router = APIRouter()

@router.get("/dispersion_tactica")
async def root(jamming: bool, firma_invalida: bool, navegacion_confiable: bool, enlace_cuantico_seguro: bool, lider_peligra: bool, fallo_eco_laser: bool):
        if (jamming == True or lider_peligra == True) and (navegacion_confiable == False or firma_invalida == True):    
            return {"message": "Maniobra de Dispersión Táctica activada."}
        else:
            return {"message": "Maniobra de Dispersión Táctica no activada."}

@router.get("/modo_cuantico_criptografico")
async def root2(jamming: bool, firma_invalida: bool, navegacion_confiable: bool, enlace_cuantico_seguro: bool, lider_peligra: bool, fallo_eco_laser: bool):
    if enlace_cuantico_seguro and not (jamming == True or lider_peligra == True) and (navegacion_confiable == False or firma_invalida == True):
        return {"message": "Modo cuántico post-criptográfico activado."}
    else:
        return {"message": "Modo Espectro Ensanchado por Salto de Frecuencia (FHSS) activado."}

@router.get("/modo_espectro_ensanchado")
async def root3(jamming: bool, firma_invalida: bool, navegacion_confiable: bool, enlace_cuantico_seguro: bool, lider_peligra: bool, fallo_eco_laser: bool):
    if not (jamming == True or lider_peligra == True) and (navegacion_confiable == False or firma_invalida == True) and not (enlace_cuantico_seguro and not (jamming == True or lider_peligra == True) and (navegacion_confiable == False or firma_invalida == True)):
        return {"message": "Modo Espectro Ensanchado por Salto de Frecuencia (FHSS) activado."}
    else:
        return {"message": "Modo Espectro Ensanchado por Salto de Frecuencia (FHSS) no activado."}
    
@router.get("/alerta_nodo_hostil")
async def root4(jamming: bool, firma_invalida: bool, navegacion_confiable: bool, enlace_cuantico_seguro: bool, lider_peligra: bool, fallo_eco_laser: bool):
    if lider_peligra and navegacion_confiable and fallo_eco_laser:
        return {"message": "Alerta nodo hostil activada."}
    else:
        return {"message": "Alerta nodo hostil no activada."}