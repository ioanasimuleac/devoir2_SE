#Simuleac Ioana-Veronica

import sys, threading, logging, os
import multiprocessing
from multiprocessing import Process, Queue, current_process, freeze_support

def bonjour(personne):
     return "Bonjour " + personne + " !"
   
def utilisation():
    #Affichage mode d'utilisation
    print """
          Le programme doit etre appelle avec minimum 1 argument:
          python bonjour_listes.py Dragos
          """

def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    #Configurez le logging pour ecrire dans un fichier texte
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename=working_dir + 'process.log',
                        level=logging.INFO)
    logging.info("Main start")

    nomQueue = Queue()
    mmeThread = []
    mThread = []
    mlleThread = []
    #La boucle principale
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
    else:
        with open(working_dir+argv[1], 'r') as f:
        #Dites bonjour a chaque personne de la liste
            for ligne in f:
                    if ligne[0:2] == "M.":
                        mThread.append(bonjour(ligne.strip(' \r\n')))
                    else:
                        if ligne[0:4] == "Mme.":
                            mme_local = bonjour(ligne.strip(' \r\n'))
                            mmeThread.append(mme_local)
                            #mme_local.start()
                        else:
                             mlle_local = bonjour(ligne.strip(' \r\n'))
                             mlleThread.append(mlle_local)


    for nume in mlleThread:
        nomQueue.put(nume);
    
    for nume in mmeThread:
        nomQueue.put(nume);
            
    for nume in mThread:
        nomQueue.put(nume);
  
    for i in range(nomQueue.qsize()):
        print nomQueue.get()

    print "Programme principal execution terminee.\n"  
    return 0

if __name__ == "__main__":
    #Simplifiez la logique de la fonction principale
    sys.exit(main())
