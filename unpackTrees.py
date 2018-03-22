import os
import time
from multiprocessing import Pool,Manager

treeFolders = os.listdir("./")

def getFiles(ind):
    f = ind[0]
    t = str(ind[1])
    if f=="log" or f=="failed" or "root" in f: 
        return 0
    if not os.path.isdir("/".join(f.split("/")[:-1]) + "/" + f.split("/")[1] + "_chunk_" + f.split("/")[-1].split("_")[-1].split(".")[0]): #Check if the dir was created
        os.mkdir("./temp/" + t)
        os.system("tar -xf ./" + f + " -C " + "./temp/" + t)
        os.rename("./temp/" + t + "/Output/","/".join(f.split("/")[:-1]) + "/" + f.split("/")[1] + "_chunk_" + f.split("/")[-1].split("_")[-1].split(".")[0]) 

    elif not os.path.isfile("/".join(f.split("/")[:-1]) + "/" + f.split("/")[1] + "_chunk_" + f.split("/")[-1].split("_")[-1].split(".")[0] + "/treeProducerSusyMultilepton/tree.root"): #Check if tree was moved
        os.rename("/".join(f.split("/")[:-1]) + "/" + "treeProducerSusyMultilepton_tree_%s.root"%str(f.split("/")[-1].split("_")[-1].split(".")[0]), "/".join(f.split("/")[:-1]) + "/" + f.split("/")[1] + "_chunk_" + f.split("/")[-1].split("_")[-1].split(".")[0] + "/treeProducerSusyMultilepton/tree.root")
        #print "/".join(f.split("/")[:-1]) + "/" + "treeProducerSusyMultilepton_tree_%s.root"%str(f.split("/")[-1].split("_")[-1].split(".")[0]), "/".join(f.split("/")[:-1]) + "/" + f.split("/")[1] + "_chunk_" + f.split("/")[-1].split("_")[-1].split(".")[0] + "/treeProducerSusyMultilepton/tree.root"
    return 1

packedFiles = []
for t in treeFolders:
  print "Starting ......." + t + "......."
  if not os.path.isdir("./"+t): continue
  else:
    prods = os.listdir("./"+t+"/")
    prods = [t + "/" +  p for p in prods]
    for p in prods:
      if not(os.path.isdir("./"+p + "/0000/")): continue
      packedFiles += ["./"+p + "/0000/" + kap for kap in os.listdir("./"+p + "/0000/")]

packedFilesClean = []
os.mkdir("./temp/")
t = 0
for p in packedFiles:
  if "tgz" in p: 
    packedFilesClean.append([p,t])
    t += 1
    
pool = Pool(16)
retlist = pool.map(getFiles, packedFilesClean)
pool.close()
pool.join()
