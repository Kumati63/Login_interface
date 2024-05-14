from DTO import tipo_usuario
from DTO import lista_cargas
from DAO import CRUDVirus
virus1 = Virus.Virus("Severe acute respiratory syndrome coronavirus 2", "SARS-CoV-2", "2019-12-01")
virus2 = Virus.Virus("Human Immunodeficiency Virus", "HIV", "1983-05-20")
virus3 = Virus.Virus("Influenza A virus subtype H1N1", "H1N1", "2009-04-15")

cat1= catalogo.Catalogo(101, "Catálogo 1")
CRUDVirus.ingresar(virus1)

cat1.agregar_al_catalogo(virus1)
cat1.agregar_al_catalogo(virus3)
cat1.agregar_al_catalogo(virus2)

cat1.ver_virus_en_catalogo()
