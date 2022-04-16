from packageF1.Pilote import *
from packageF1.GrandPrix import *
from packageF1.Joueur import *
from packageF1.EnsembleJoueur import *
from packageF1.fonctions import *

#
# Saison 6
#
# Calcul des points pour les pilotes de division 3
#

def getPointsD3() -> dict:

    ###################################################################################################

    # Création des pilotes

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    ecs_finesse = Pilote("ESC Finesse", "Mercedes")
    ert_wartors = Pilote("ERT Wartors", "Mercedes")

    non4me_cami = Pilote("Non4ame Cami", "RedBull")
    soo_skyzzz = Pilote("Soo Skyzzz", "RedBull")

    knacki_ball = Pilote("Knacki Ball", "McLaren")
    pur_marth = Pilote("PuR Marth", "McLaren") 

    nygraal = Pilote("Nygraal", "Ferrari")
    chr_olivz = Pilote("CHR Olivz", "Ferrari") 

    eroziah_spl = Pilote("EroziaH SPL", "AlphaTauri")
    ert_mirage = Pilote("ERT Mirage", "AlphaTauri") 

    rp1_fifi = Pilote("RP1 Fifi", "Alpine")
    ducpascharlie = Pilote("DucPasCharlie", "Alpine")

    rp1_gachette = Pilote("RP1 Gachette", "AstonMartin")
    istoozen_eko = Pilote("Istoozen eKo", "AstonMartin")

    sks_flyart = Pilote("SKS Flyart", "AlfaRomeo")
    mcr_papyx = Pilote("MCR Papyx", "AlfaRomeo")

    ert_aurelius = Pilote("ERT Aurelius", "Williams")
    ert_matfax = Pilote("ERT Matfax", "Williams")

    alexgt500 = Pilote("AlexGT500", "Haas")
    ert_toon = Pilote("ERT Toon", "Haas") 

    ###################################################################################################

    # Course 1

    result01 = GrandPrix("Autriche")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    qualif01 = [
        knacki_ball,
        ducpascharlie,
        istoozen_eko,
        non4me_cami,
        ecs_finesse,
        soo_skyzzz,
        ert_matfax,
        pur_marth, # remplacé par LTR Coach
        nygraal,
        ert_aurelius,
        alexgt500,
        chr_olivz, # remplacé par Yozana
        ert_toon, # remplacé par QRL Blanco
        ert_mirage, # remplacé par Pur Ultraaa
        sks_flyart,
        ert_wartors,
        mcr_papyx,
        rp1_fifi,
        eroziah_spl,
        rp1_gachette
    ]

    course01 = [
        knacki_ball,
        eroziah_spl,
        chr_olivz,
        ert_wartors,
        mcr_papyx,
        pur_marth,
        soo_skyzzz,
        alexgt500,
        ert_aurelius,
        ecs_finesse,
        ert_mirage,
        rp1_gachette,
        ducpascharlie,
        non4me_cami,
        rp1_fifi,
        ert_toon,
        ert_matfax,
        istoozen_eko,
        nygraal,
        sks_flyart
    ]

    # classements
    result01.resultat("q", qualif01)
    result01.resultat("c", course01)

    result01.calcPointsQ()
    result01.calcPointsC()

    # évènements ponctuels
    result01.crash("q", sks_flyart)
    result01.crash("q", eroziah_spl)
    result01.crash("q", rp1_gachette)
    result01.crash("q", soo_skyzzz)

    result01.crash("c", sks_flyart)
    result01.crash("c", nygraal)
    result01.crash("c", istoozen_eko)
    result01.crash("c", ert_matfax)

    result01.meilleurTour(rp1_gachette)


    for i in result01.getCourse():
        print(i.getGamertag(), i.getHistorique())

    
    return result01.getPoints()