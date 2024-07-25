from fastapi import APIRouter
from service import professeur_service
from schema.professeur_schema import ProfesseurUpdateSchema

# Initailisation du router
router = APIRouter(
    prefix="/professeur",
    tags=["Professeur"]
)

# Ajout d'une fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_professeur(id):
    return professeur_service.get_one(id)

# Ajout d'une fonction permettant d'afficher les eleves et leur note selon un professeur
@router.get("/q5_get_eleve_note_by_professeur/all_professeur")
def get_eleve_note_by_professeur():
    return professeur_service.get_eleve_note_by_professeur()

# Ajout d'une fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/q1_liste_professeur/all_professeur")
def get_all_professeur():
    return professeur_service.get_all()

# Ajout d'une fonction permettant d'inserer un element de la BDD
@router.post("/one")
def create_one_professeur(item):
    return professeur_service.create_one(item)

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_professeur(item):
    return professeur_service.create_many(item)

# Ajout d'une fonction permettant de mettre a jour l'adresse' d'un professeur de la BDD
@router.patch("/one/{id_prof}", response_model=dict)
def update_one_professeur(id_prof, update: ProfesseurUpdateSchema):
    update_dict = update.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = professeur_service.update_one(id_prof, update_dict)
    return {"modified_count": results.modified_count}

"""
# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_professeur(filter, newValue):
    return professeur_service.update_many(filter, newValue)
"""
# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_professeur(id):
    return professeur_service.delete_one(id)

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_professeur(item):
    return professeur_service.delete_many(item)