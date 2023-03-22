from clases.mascota import Mascota
from clases.ninja import Ninja

mis_premios = ['Churru', 'Jamón', 'Aceitunas']
mi_alimento_mascota = [ 'Atún', 'Alimento seco']
lennon = ['Lennon', 'Ringo','Agata']
andrea = Ninja('Andrea', 'Lennon', mis_premios, mi_alimento_mascota, lennon)
andrea.alimentar()
andrea.caminar()
andrea.bañar()