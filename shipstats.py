## shipstats ##
import h5py
import numpy as np
##
Ships={"Pyramidion"}#,"Squid","Goldfish","Mobula","Galleon","Junker","Spire","Magnate","Crusader","Corsair","Judgement","Shrike","Stormbreaker"}
Pyramidion={"Mass":200,"Thrust":700000,"Lift":600000,"LDrag":0.061,"ADrag":0.1322,"VDrag":0.0208,"TAcc":8}


### tool stats

#PTools=["Claw","Kerosene","Moonshine","Driftsail"]
#PTools["Claw"]={"Thrust":1.5,"Dmg":13,"ADrag":0.35,"LDrag":2,"LaDrag":1,"Duration":0}
#PTools["Kerosene"]={"Thrust":2.5,"Dmg":10,"ADrag":3,"LDrag":2,"LaDrag":1,"Duration":0}
#PTools["Moonshine"]={"Thrust":3,"Dmg":30,"ADrag":10,"LDrag":0.5,"LaDrag":1,"Duration":0}
#PTools["Driftsail"]={"Thrust":0.5,"Dmg":0,"ADrag":0.23,"LDrag":0.1,"LaDrag":0,"Duration":0}



#ETools=


statfilen = "stats10.h5"
statfile  = h5py.File(statfilen, "w")
g1 = statfile.create_group('Ships')
g1.create_dataset('empty',data=[0,0,0])
for el in Ships:
    g2=g1.create_group(el)
    k=list(globals()[el].keys())
    kv=np.array(list(globals()[el].values()))
    for stati in range(0,len(k)):
        g2.create_dataset(k[stati],data=kv[stati])
