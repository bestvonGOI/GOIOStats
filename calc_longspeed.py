import functions as gs
import numpy as np

ships_url='https://docs.google.com/spreadsheets/d/e/2PACX-1vRpgma08weJpQIGfDT0bMFV7GR1zlSugg53vxdgEpmgN1-2ByTQVnna9JBFliT8uc7zWXOnY4Qg0ja0/pub?gid=0&single=true&output=csv'
ptools_url='https://docs.google.com/spreadsheets/d/e/2PACX-1vRpgma08weJpQIGfDT0bMFV7GR1zlSugg53vxdgEpmgN1-2ByTQVnna9JBFliT8uc7zWXOnY4Qg0ja0/pub?gid=1987404630&single=true&output=csv'
components_url='https://docs.google.com/spreadsheets/d/e/2PACX-1vRpgma08weJpQIGfDT0bMFV7GR1zlSugg53vxdgEpmgN1-2ByTQVnna9JBFliT8uc7zWXOnY4Qg0ja0/pub?gid=1197729949&single=true&output=csv'
etools_url='https://docs.google.com/spreadsheets/d/e/2PACX-1vRpgma08weJpQIGfDT0bMFV7GR1zlSugg53vxdgEpmgN1-2ByTQVnna9JBFliT8uc7zWXOnY4Qg0ja0/pub?gid=1815544244&single=true&output=csv'
event_ulr="https://docs.google.com/spreadsheets/d/e/2PACX-1vRpgma08weJpQIGfDT0bMFV7GR1zlSugg53vxdgEpmgN1-2ByTQVnna9JBFliT8uc7zWXOnY4Qg0ja0/pub?gid=2048311394&single=true&output=csv"
dt=0.25 # n times needs to be a full number
tend=100
trange=np.linspace(0,tend,int(tend/dt)+1)
Ships_selected=['Goldfish']

gs.dltable(ships_url,'ships.csv')
gs.dltable(ptools_url,'ptools.csv')
gs.dltable(etools_url,'etools.csv')
gs.dltable(components_url,'components.csv')
gs.dltable(event_url,'events.csv')
ShipStats=gs.readtable('ships.csv','Ship')
PToolStats=gs.readtable('ptools.csv','Tool')
EToolStats=gs.readtable('etools.csv','Tool')
ComponentStats=gs.readtable('components.csv','Component')
events=gs.parse_input_file('inputs/in_test.txt')




for sh in range(0,len(Ships_selected)):
    Enginestatus={'Ratio' : ShipStats[Ships_selected[sh]]["Ratio_H_L"]}
    if int(ShipStats[Ships_selected[sh]]["HEngine"]) > 0:
        Enginestatus['HEngine']=(ComponentStats['HEngine']['Health'])
    if int(ShipStats[Ships_selected[sh]]["LEngine"]) > 0:
        Enginestatus['LEngine']=(ComponentStats['LEngine']['Health'])
    Enginestatus['Buff']=0

    Shipstatus={'a':ShipStats[Ships_selected[sh]]["Acceleration"]}
    Shipstatus['v']=0
    Shipstatus['Thrust']=ShipStats[Ships_selected[sh]["Thrust"]
    Shipstatus['LDrag']=ShipStats[Ships_selected[sh]]["LDrag"]
    Shipstatus['VDrag']=ShipStats[Ships_selected[sh]]["VDrag"]
    Shipstatus['ADrag']=ShipStats[Ships_selected[sh]]["ADrag"]
    Shipstatus['Enginedmg']=0
    Shipstatus['ActivePTool']=""
    Shipstatus['ActiveETool']=""
    AtiveTool=0
    ev_id=0
    for ts in range(len(trange)):
        t=trange[ts]
        if ev_id!=0:
            old_event=events[str(ev_id-1)]
        else:
            old_event=events[str(ev_id)]
        curr_event=events[str(ev_id)]
        if abs(t-curr_event["Time"]) < dt/2:
            Shipstatus["Thrust"]=ShipStats[Ships_selected[sh]["Thrust"]*EngineStatus['HEngine']/ComponentStats['HEngine']['Health']*Enginestatus['Ratio']+EngineStatus['LEngine']/ComponentStats['LEngine']['Health']*(1-Enginestatus['Ratio'])
            ActivePTools=curr_event["Claw"]+curr_event["Kerosene"]+curr_event["Moonshine"]+curr_event["Hydrogen"]+curr_event["Ballonvent"]
            if ActivePTools>1:
                disp("Can only have 1 active Pilot tool")
                break
            Shipstatus["Thrust"]=Shipstatus["Thrust"]*(curr_event["Kerosene"]*PToolStats["Kerosene"]["Thrust"]+curr_event["Moonshine"]*PToolStats["Moonshine"]["Thrust"]+curr_event["Claw"]*PToolStats["Claw"]["Thrust"])*curr_event["Driftsail"]*PToolStats["Driftsail"]["Thrust"]


        Shipstatus["LDrag"]=ShipStats[Ships_selected[sh]["LDrag"]*PToolStats[events[ev_id][2]]["LDrag"]
        Shipstatus["ADrag"]=ShipStats[Ships_selected[sh]["ADrag"]*PToolStats[events[ev_id][2]]["ADrag"]
        Shipstatus["VDrag"]=ShipStats[Ships_selected[sh]["VDrag"]*PToolStats[events[ev_id][2]]["VDrag"]
        Shipstatus['Enginedmg']=PToolStats["Damage"]
