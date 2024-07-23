from fastapi import APIRouter
from service import classe_service

# Initailisation du router
router = APIRouter(
    prefix="/classe",
    tags=["Classe"]
)

# Ajout d'un fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_classe(id):
    return classe_service.get_one(id)

# Ajout d'un fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_classe():
    return classe_service.get_all()

# Ajout d'un fonction permettant d'inserer un element de la BDD
@router.post("/one")
def create_one_classe(item):
    return classe_service.create_one(item)

# Ajout d'un fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_classe(item):
    return classe_service.creat_many(item)

"""
# Ajout d'un fonction permettant de mettre a jour un element de la BDD
@router.patch("/one")
def update_one_classe(filter, newValue):
    return classe_service.update_one(filter, newValue)

# Ajout d'un fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_classe(filter, newValue):
    return classe_service.update_many(filter, newValue)
"""
# Ajout d'un fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_classe(id):
    return classe_service.delete_one(id)

# Ajout d'un fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_classe(item):
    return classe_service.delete_many(item)