
# coding: utf-8

# In[19]:


#CALCULO DE MEDIA, MODA, PROMEDIO, VARIANZA Y COVARIANZA  

import statistics as stats

print ("VALORES ALMACENADOS ESTATICAMENTE")
valores = [1, 12, 5, 8, 1, 6, 3, 9, 1, 7, 15, 11, 1, 13, 5, 6] 
                                                                                         
print (valores)   
print ("")

# Calculo de Moda 
def calculoModa(): 
    nDatos = 0 
    for i in valores:                                                                              
        nNuevo = valores.count(i)                                                             
        if nNuevo > nDatos:                                                       
            nDatos = nNuevo                                                                                                                               
    modas = []                                                                               
    for i in valores:                                                                              
        nNuevo = valores.count(i)                                                             
        if nNuevo == nDatos and i not in modas:                                   
            modas.append(i)
            return modas

# Calculo de Mediana                                                                                
def calculoMediana():
    valores.sort()                                                                            
    if len(valores) % 2 == 0:                                                                      
        n = len(valores)                                                                           
        mediana = (valores[n//2-1]+ valores[n//2] )//2                                                      
    else:                                                                                    
        mediana =valores[len(valores)//2]
    return mediana

#Calculo de Promedio
def calculoPromedio():
    promedio = sum(valores)/len(valores)
    return promedio

#Calculo de Varianza
def calculoVarianza():
    var=(stats.pvariance(valores))
    return var

#Calculo de Covarianza
def calculoCovarianza():
    covar=(stats.stdev(valores))
    return covar

tDatos=len(valores) 
print ("Total Valores Almacenados: ", tDatos)
print ("")

print ('Mediana:' ,calculoMediana()) 
print ('Moda:' ,calculoModa())
print ("Promedio: ", calculoPromedio()) 
print ("Varianza: ", calculoVarianza())
print ("Covarianza: ", calculoCovarianza())

