import RobotRaconteur as RR
import re
import glob, os

my_service_defs={}
current_dir=os.getcwd()
os.chdir(current_dir+"\\robotraconteur_standard_robdef_cpp\\robdef\\group1")
for file in glob.glob("*.robdef"):
    filed=open(file)
    my_service_def=filed.read()
    
    service_def = RR.ServiceDefinition()
    service_def.FromString(my_service_def)
    
    my_service_defs[service_def.Name]=service_def

Named_arrayslist=[]
Structureslist=[]

for key in my_service_defs:
    for n in my_service_defs[key].NamedArrays:
        
        name=my_service_defs[key].Name.replace(".","::")
        qualifiedname=name+"::"+n.Name
        Named_arrayslist.append(qualifiedname.replace("::","_"))

    for e in my_service_defs[key].Structures:
        
        name=my_service_defs[key].Name.replace(".","::")
        qualifiedname=name+"::"+e.Name
        Structureslist.append(qualifiedname.replace("::","_"))    




file1 = open("GeometryEnum.txt","w") 
#error_names=[]
os.chdir(current_dir+"\\Python_YAML_loader")
file2=open("python_enums.py","w")
filenames=[]
enum_list=[]
file3=open("allregisters.txt","w")
file2.write("#!/usr/bin/env python\n\n")

for key in my_service_defs:
    usingdict={}
    interior={}
    interiornamedarrays={}
    interiorstructures={}
    file3.write("RRN.RegisterServiceTypeFromFile(\""+my_service_defs[key].Name+"\")\n")
    for n in my_service_defs[key].NamedArrays:
        qualifiedname=name+"."+n.Name
        #print(qualifiedname)
        interiornamedarrays[n.Name]=qualifiedname.replace(".","_")
        interior[n.Name]=qualifiedname.replace(".","_")
        
    for l in my_service_defs[key].Structures:
        qualifiedname=name+"."+l.Name
        interiorstructures[l.Name]=qualifiedname.replace(".","_")
        interior[l.Name]=qualifiedname.replace(".","_")
    
    filename="YAMLconverter__"+my_service_defs[key].Name.replace(".","_")+".py"
    error_names=[]
    file1=open(filename,"w")
    filenames.append(filename)
    file1.write("#!/usr/bin/env python\n")
    
    file1.write("import yaml\n")
    #file1.write("import RobotRaconteur as RR\n")
    #file1.write("RRN=RR.RobotRaconteurNode.s\n")
    file1.write("import numpy\n")
    file1.write("import python_enums\n")
    file1.write("")
    
    for e in my_service_defs[key].Enums:
        file2.write("def string_to_enum_%s(enumval):\n"%(e.Name))
        # Compare e.Name to the enum you are looking for
        #print(e.Values[-1].Name)
        enum_list.append(e.Name)
        for e_value in e.Values:
            #if(e_value.Name==e.Values[-1].Name):
            file2.write("\tif(enumval==\""+e_value.Name + "\"): return " + str(e_value.Value)+"\n")
            #else:
            #    file1.write("\t"+e_value.Name + " = " + str(e_value.Value)+",\n")
            
        file2.write("\n")
    
    for imports in my_service_defs[key].Imports:
        file1.write("import YAMLconverter__%s\n"%(imports.replace(".","_")))
        #print(imports)
    
    
    for use in my_service_defs[key].Using:
        #print(use.UnqualifiedName)
        
        if(use.UnqualifiedName not in usingdict.keys()):
            usingdict[use.UnqualifiedName]=use.QualifiedName.replace(".","_")
            #print(use.QualifiedName)
    name=my_service_defs[key].Name
    underscored_name=my_service_defs[key].Name.replace(".","_")
    for n in my_service_defs[key].NamedArrays:
        file1.write("def yaml_loader_%s_%s(RRN,data):\n"%(underscored_name,n.Name))
        file1.write("\toutput_type=RRN.GetNamedArrayDType(\"%s.%s\")\n"%(my_service_defs[key].Name,n.Name))
        file1.write("\toutput=numpy.zeros((1,),dtype=output_type)\n")
        
        qualifiedname=name+"."+n.Name
        #print(qualifiedname)
        usingdict[n.Name]=qualifiedname.replace(".","_")
        count=0
        for field in n.Members:
            output=field.ToString()
            fieldname=field.Name
            f=re.split('\s+', output)
            #print(f)
            if(f[0]=="property"):
                #position[0]['orientation']['z']=data['orientation']['z']
                if(f[1]=="string" or f[1]=="single" or f[1]=="double" or f[1]=="int32" or f[1]=="uint32" or f[1]=="int8" or f[1]=="uint8" or f[1]=="int16" or f[1]=="uint16" or f[1]=="int64" or f[1]=="uint64" or f[1]=="bool"):
                    file1.write("\toutput[0]['%s']=data['%s']\n"%(f[2],f[2]))
                    
                elif(f[1]=="uint8[16]"):
                    file1.write("\t#uuid_list=list(data['%s'])\n"%(f[2]))
                    file1.write("\t#uuid=numpy.array(uuid_list,dtype=numpy.uint8)\n")
                    file1.write("\t#output[0]['%s']=uuid\n"%(f[2]))
                elif("[" in f[1]):
                    if("single" in f[1]):
                        file1.write("\tarray=numpy.zeros(len(data['%s']),dtype=numpy.single)\n"%(f[2]))
                        file1.write("\tfor i in range(len(data['%s'])):\n"%(f[2]))
                        file1.write("\t\tarray[i]=data['%s'][i]\n"%(f[2]))
                        file1.write("\toutput[0]['%s']=array\n"%(f[2]))
                    elif("double" in f[1]):
                        file1.write("\tarray=numpy.zeros(len(data[%s]),dtype=numpy.double)\n"%(f[2]))
                        file1.write("\tfor i in range(len(data['%s'])):\n"%(f[2]))
                        file1.write("\t\tarray[i]=data['%s'][i]\n"%(f[2]))
                        file1.write("\toutput[0]['%s']=array\n"%(f[2]))
                
                
                

                elif(f[1] in usingdict.keys()):
                    #print(f[1])
                    #print(usingdict.get(f[1]))
                    #print(name)
                    
                    if(usingdict.get(f[1]) in Structureslist):
                        #print(usingdict.get(f[1]))
                        #Never happens in current robdefs
                        if(f[1] in interior.keys()):
                            file1.write("\toutput[0]['%s'] = yaml_loader_%s(RRN,data['%s'])\n"%(f[2],usingdict.get(f[1]),f[2]))
                        
                        print("hello")
                        
                    if(usingdict.get(f[1]) in Named_arrayslist):
                        if(f[1] in interior.keys()):
                            file1.write("\toutput[0]['%s'] = yaml_loader_%s(RRN,data['%s'])\n"%(f[2],usingdict.get(f[1]),f[2]))
                        else:
                            #print("\n"+f[1]+"\n")
                            #print(f[2])
                            importing="YAMLconverter__"+usingdict.get(f[1]).replace("_"+f[1],"")
                            #print(importing)
                            final=importing+".yaml_loader_"+usingdict.get(f[1])+"(RRN,data['"+f[2]+"'])\n"
                            #print(final)
                            file1.write("\toutput[0]['%s']= %s"%(f[2],final))
                
                else:
                    print(f[2])
                    if(qualifiedname not in error_names):
                        error_names.append(qualifiedname)
                    #print("\n"+f[1]+"\n")
                    #print(f[2]+"\n")
                    
            count+=1
        file1.write("\treturn output\n\n")
        
    for e in my_service_defs[key].Structures:
        qualifiedname=name+"."+e.Name
        usingdict[e.Name]=qualifiedname.replace(".","_")
            
        
    for e in my_service_defs[key].Structures:
        file1.write("def yaml_loader_%s_%s(RRN,data):\n"%(underscored_name,e.Name))
        file1.write("\toutput=RRN.NewStructure(\"%s.%s\")\n"%(my_service_defs[key].Name,e.Name))
        #state.seqno=self.seqno
        #qualifiedname=name+"."+e.Name
        #usingdict[e.Name]=qualifiedname.replace(".","_")
        for field in e.Members:
            output=field.ToString()
            fieldname=field.Name
            f=re.split('\s+', output)
            #print(f)
            if(f[0]=="property"):
                #if("list" in f[1]):
                    #print(f[1])
                
                if(f[1]=="string" or f[1]=="single" or f[1]=="double" or f[1]=="int32" or f[1]=="uint32" or f[1]=="int8" or f[1]=="uint8" or f[1]=="int16" or f[1]=="uint16" or f[1]=="int64" or f[1]=="uint64" or f[1]=="bool"):
                    file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                    file1.write("\t\toutput.%s=data['%s']\n"%(f[2],f[2]))
                    file1.write("\telse:\n")
                    file1.write("\t\tprint(\"No value found for %s\\n\")\n"%(f[2]))
                elif("[" in f[1]):
                    #print("\n"+f[2])
                    #print(f[1]) 
                    if("," in f[1]):
                        if("single" in f[1]):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\tarray=numpy.zeros(len(data['%s']),dtype=numpy.single)\n"%(f[2]))
                            
                            temp = re.findall(r'\d+', f[1]) 
                            res = list(map(int, temp))  
                            #res = [int(i) for i in f[1].split() if i.isdigit()]
                            #print(res)
                            
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\t\tarray[i]=data['%s'][i]\n"%(f[2]))
                            file1.write("\t\tarray=array.reshape(%d,%d)\n"%(res[0],res[1]))
                            file1.write("\t\toutput.%s=array\n"%(f[2]))
                            file1.write("\telse:\n")
                            file1.write("\t\tprint(\"No value found for %s\\n\")\n"%(f[2]))
                            
                        elif("double" in f[1]):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\tarray=numpy.zeros(len(data['%s']),dtype=numpy.double)\n"%(f[2]))
                            
                            temp = re.findall(r'\d+', f[1]) 
                            res = list(map(int, temp))  
                            #res = [int(i) for i in f[1].split() if i.isdigit()]
                            #print(res)
                            
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\t\tarray[i]=data['%s'][i]\n"%(f[2]))
                            file1.write("\t\tarray=array.reshape(%d,%d)\n"%(res[0],res[1]))
                            file1.write("\t\toutput.%s=array\n"%(f[2]))
                            file1.write("\telse:\n")
                            file1.write("\t\tprint(\"No value found for %s\\n\")\n"%(f[2]))
        
                        
                    else:
                        if("single" in f[1]):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\toutput.%s=numpy.zeros(len(data['%s']),dtype=numpy.single)\n"%(f[2],f[2]))
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\t\toutput.%s[i]=data['%s'][i]\n"%(f[2],f[2]))
                            
                        elif("double" in f[1]):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\toutput.%s=numpy.zeros(len(data['%s']),dtype=numpy.double)\n"%(f[2],f[2]))
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\t\toutput.%s[i]=data['%s'][i]\n"%(f[2],f[2]))
                            
                        elif("uint32" in f[1]):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\toutput.%s=numpy.zeros(len(data['%s']),dtype=numpy.uint32)\n"%(f[2],f[2]))
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\t\toutput.%s[i]=data['%s'][i]\n"%(f[2],f[2]))
                            
                        elif("uint8" in f[1]):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\toutput.%s=numpy.zeros(len(data['%s']),dtype=numpy.uint8)\n"%(f[2],f[2]))
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\t\toutput.%s[i]=data['%s'][i]\n"%(f[2],f[2]))
                            
                        elif("int32" in f[1]):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\toutput.%s=numpy.zeros(len(data['%s']),dtype=numpy.int32)\n"%(f[2],f[2]))
                            file1.write("\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\toutput.%s[i]=data['%s'][i]\n"%(f[2],f[2]))
                            
                        elif(f[1].replace("[]","") in usingdict.keys()):
                            #print(f[2])
                            #print(f[1])
                            #only contains named arrays so this is valid
                            if(f[1].replace("[]","") in interior.keys()):
                                file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                                file1.write("\t\tdtype=RRN.GetNamedArrayDType(\"%s\")\n"%(usingdict.get(f[1].replace("[]","")).replace("_",".")))
                                #print(usingdict.get(f[1].replace("[]","")).replace("_","."))
                                file1.write("\t\tmyarray=numpy.zeros((len(data['%s'],),dtype=dtype)\n"%(f[2]))
                                file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                                file1.write("\t\t\tmyarray[i]=yaml_loader_%s(RRN,data['%s'][i])\n"%(usingdict.get(f[1].replace("[]","")),f[2]))
                                
                                file1.write("\t\toutput.%s=myarray\n"%(f[2]))
                                
                                
                            else:
                                file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                                file1.write("\t\tdtype=RRN.GetNamedArrayDType(\"%s\")\n"%(usingdict.get(f[1].replace("[]","")).replace("_",".")))
                                file1.write("\t\tmyarray=numpy.zeros((len(data['%s'],),dtype=dtype)\n"%(f[2]))
                                file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                                
                                #print(usingdict.get(f[1].replace("[]","")).replace("_","."))
                                importing="YAMLconverter__"+usingdict.get(f[1].replace("[]","")).replace("_"+f[1].replace("[]",""),"")
                                #print(importing)
                                final="\t\t\tmyarray[i]"+" = "+importing+".yaml_loader_"+usingdict.get(f[1].replace("[]",""))+"(RRN,data['"+f[2]+"'][i])\n"
                                #print(final)
                                file1.write(final)
                                file1.write("\t\toutput.%s=myarray\n"%(f[2]))
                                
                                
                                
                        else:
                            i=0
                            #print("\n"+f[2])
                            #print(f[1]) 
                            #print("\n"+f[2])
                            #print(f[1]) 
                    
                elif("{list}" in f[1]):
                    
                    if(f[1].replace("{list}","")=="string"):
                        file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                        file1.write("\t\tmylist=[]\n")
                        file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                        file1.write("\t\t\tmylist.append(data['%s'][i])\n"%(f[2]))
                        file1.write("\t\toutput.%s=mylist\n"%(f[2]))
                        
                        
                    elif(f[1].replace("{list}","") in usingdict.keys()):
                        if(f[1].replace("{list}","") in interior.keys()):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\tmylist=[]\n")
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            file1.write("\t\t\tmylist.append(yaml_loader_%s(RRN,data['%s'][i]))\n"%(usingdict.get(f[1].replace("{list}","")),f[2]))
                            file1.write("\t\toutput.%s=mylist\n"%(f[2]))
                            
                            
                        else:
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\tmylist=[]\n")
                            file1.write("\t\tfor i in range(len(data['%s'])):\n"%(f[2]))
                            importing="YAMLconverter__"+usingdict.get(f[1].replace("{list}","")).replace("_"+f[1].replace("{list}",""),"")
                            #print(importing)
                            final="\t\t\tmylist.append("+importing+".yaml_loader_"+usingdict.get(f[1].replace("{list}",""))+"(RRN,data['"+f[2]+"'][i]))\n"
                            #print(final)
                            file1.write(final)
                            #file1.write("\t\tmylist.append(yaml_loader_%s(data['%s'][i]))\n"%(usingdict.get(f[1].replace("[]","")),f[2]))
                            file1.write("\t\toutput.%s=mylist\n"%(f[2]))
                    
                    
                    else:
                        i=0
                        #print(Structureslist)
                        #print("\n"+f[2])
                        #print(f[1]) 
                elif("{string}" in f[1]):
                    if(f[1].replace("{string}","") in usingdict.keys()):
                        z=0
                        #TODO: fix this part
                    
                elif(f[1] in usingdict.keys()):
                    if(usingdict.get(f[1]) in Structureslist):
                        #print(usingdict.get(f[1]))
                        if(f[1] in interior.keys()):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\toutput.%s = yaml_loader_%s(RRN,data['%s'])\n"%(f[2],usingdict.get(f[1]),f[2]))
                            
                            
                        else:
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            importing="YAMLconverter__"+usingdict.get(f[1]).replace("_"+f[1],"")
                            #print(importing)
                            final="\t\toutput."+f[2]+" = "+importing+".yaml_loader_"+usingdict.get(f[1])+"(RRN,data['"+f[2]+"'])\n"
                            file1.write(final)
                        
                        
                        
                    if(usingdict.get(f[1]) in Named_arrayslist):
                        if(f[1] in interior.keys()):
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            file1.write("\t\toutput.%s = yaml_loader_%s(RRN,data['%s'])\n"%(f[2],usingdict.get(f[1]),f[2]))
                            
                            
                        else:
                            file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                            importing="YAMLconverter__"+usingdict.get(f[1]).replace("_"+f[1],"")
                            #print(importing)
                            final="\t\toutput."+f[2]+" = "+importing+".yaml_loader_"+usingdict.get(f[1])+"(RRN,data['"+f[2]+"'])\n"
                            file1.write(final)
                 

                
                elif(f[1] in enum_list):
                    file1.write("\tif(data.get('%s')!=None):\n"%(f[2]))
                    file1.write("\t\toutput.%s=python_enums.string_to_enum_%s"%(f[2],f[1]))
                    
                    
                    #print("\n"+f[2])
                    #print(f[1]) 
                
                else:
                    print("\n"+f[2])
                    print(f[1]) 
                    if(qualifiedname not in error_names):
                        error_names.append(qualifiedname)
                """        
                elif(f[1].replace("{list}","") in usingdict.keys()):
                    #print(f[1])
                    if(usingdict.get(f[1].replace("{list}","")) in Structureslist):
                        file1.write("\t\t\tif(node[\"%s\"]){\n"%(f[2]))
                        file1.write("\t\t\t\trhs->%s=RR::AllocateEmptyRRList<%s>();"%(f[2],f[1].replace("{list}","")))
                        file1.write("\t\t\t\trhs->%s = node[\"%s\"].as<%sPtr>();\n"%(f[2],f[2],usingdict.get(f[1])))
                        file1.write("\t\t\t}\n")
                    #    print(f[1])
                    if(usingdict.get(f[1].replace("{list}","")) in Named_arrayslist):
                        x=0
                        print(f[1])
                """
                
                
                
                
                    #print("\n"+f[1]+"\n")
                    #print(f[2]+"\n")
                    
        file1.write("\treturn output\n\n")
        #file1.write("\n\n")
    
    if(len(error_names)>0):
        file1.write("#TODO: Fix the following structures or namedarrays: \n")
        for i in error_names:
            file1.write("# "+i+" \n")
        
    file1.write("\n")
    # Compare e.Name to the enum you are looking for
    #print(e.Values[-1].Name)
#    for e_value in e.Values:
        #if(e_value.Name==e.Values[-1].Name):
#        file1.write("\tif(input==\""+e_value.Name + "\") return " + str(e_value.Value)+";\n")
        #else:
        #    file1.write("\t"+e_value.Name + " = " + str(e_value.Value)+",\n")
        
#print(Named_arrayslist)
#print("\n\n\n")
#print(Structureslist)
file1 = open("GeometryEnum.txt","w") 
for i in filenames:
    file1.write(i+"\n")
#print(error_names)
file1.close()
"""

template<>
	struct convert<geometry::NamedPosePtr> {
		static Node encode(const geometry::NamedPosePtr& rhs) {
			Node node;

			return node;
		}

		static bool decode(const Node& node, geometry::NamedPosePtr& rhs) {
			//if (!node.IsSequence() || node.size() != 3) {
			//	return false;
			//}
			if (!rhs) rhs.reset(new geometry::NamedPose);
			rhs->pose = node.as<geometry::Pose>();
			if (node["parent_frame"]) {
				rhs->parent_frame = node["parent_frame"].as<identifier::IdentifierPtr>();
			}
			if (node["frame"]) {
				rhs->frame = node["frame"].as<identifier::IdentifierPtr>();
			}
			


			return true;
		}
	};
    """