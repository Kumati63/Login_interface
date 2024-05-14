class Catalogo:
    def __init__(self, id_Catalogo, nombre):
        self.id_Catalogo = id_Catalogo
        self.nombre = nombre
        self.lista_virus = []
    # con esta funcion podrias agregar virus a un catalogo
    def agregar_al_catalogo (self, Virus):
        self.lista_virus.append(Virus)

    def ver_virus_en_catalogo(self):
        if not self.lista_virus:
            print("El catálogo está vacío. No hay virus registrados.")
        else:
            print(f"Virus en el catálogo '{self.nombre}':")
            for virus in self.lista_virus:
                print(f"Nombre Científico: {virus.nombreCientifico}, Nombre: {virus.nombre}, Fecha de Descubrimiento: {virus.fechaDesc}")
