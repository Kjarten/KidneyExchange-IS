# -*- coding: utf-8 -*-
class random_icelanders:
    
    import numpy as np
    
    def eGFR_data(self):
    
        #Estimated Glomerular Filtration Rate
        #kidney.org/sites/default/files/docs/11-10-1813_abe_patbro_gfr_b.pdf
        
        import numpy as np
        
        eGFRm18 = np.random.normal(100,13,1000) #Male 18 to 24
        eGFRm25 = np.random.normal(93,13,1000)  #Male 25 to 29
        eGFRm30 = np.random.normal(86,13,1000)  #Male 30 to 34
        eGFRm35 = np.random.normal(85,14,1000)  #Male 35 to 39
        eGFRm40 = np.random.normal(84,13,1000)  #Male 40 to 44
        eGFRm45 = np.random.normal(83,13,1000)  #Male 45 to 49
        eGFRm50 = np.random.normal(79,12,1000)  #Male 50 to 54
        eGFRm55 = np.random.normal(76,13,1000)  #Male 55 to 59
        eGFRm60 = np.random.normal(75,15,1000)  #Male 60 to 64

        eGFRf18 = np.random.normal(91,15,1000)  #Female 18 to 24
        eGFRf25 = np.random.normal(85,13,1000)  #Female 25 to 29
        eGFRf30 = np.random.normal(85,15,1000)  #Female 30 to 34
        eGFRf35 = np.random.normal(79,13,1000)  #Female 35 to 39
        eGFRf40 = np.random.normal(77,12,1000)  #Female 40 to 44
        eGFRf45 = np.random.normal(74,10,1000)  #Female 45 to 49
        eGFRf50 = np.random.normal(73,13,1000)  #Female 50 to 54
        eGFRf55 = np.random.normal(70,12,1000)  #Female 55 to 59
        eGFRf60 = np.random.normal(68,12,1000)  #Female 60 to 64
    
        return (eGFRm18,eGFRm25,eGFRm30,eGFRm35,eGFRm40,eGFRm45,eGFRm50, \
            eGFRm55,eGFRm60,eGFRf18,eGFRf25,eGFRf30,eGFRf35,eGFRf40,eGFRf45, \
            eGFRf50,eGFRf55,eGFRf60)

    def rand_pop(self,size):
        #--------------------------------------------------------------------------------------------------------------------------
        #Function that creates a random pool of Icelandic people
    
        #Input Variables:
            #size:       Number of persons, int
    
        #Output:
            #pop:        Pool of Icelandic people with and critera used for evaluating kidney compatibility, array
        #--------------------------------------------------------------------------------------------------------------------------
    
        import numpy as np
    
        [eGFRm18,eGFRm25,eGFRm30,eGFRm35,eGFRm40,eGFRm45,eGFRm50, \
         eGFRm55,eGFRm60,eGFRf18,eGFRf25,eGFRf30,eGFRf35,eGFRf40,eGFRf45, \
         eGFRf50,eGFRf55,eGFRf60] = eGFR_data(self)
    
        bt_pop = np.random.choice(['O', 'A', 'B', 'AB'], size, p=[0.55, 0.32, 0.10, 0.03])   #Blood type
        aa_pop = np.random.choice([0, 1], size, p=[0.995, 0.005])                            #Born in Africa
        age_pop = np.random.randint(18, 60 ,size)                                            #Age
        gen_pop = np.random.choice([0, 1], size, p=[0.5, 0.5])                               #Sex
    
        #Initialize
        #Estimated Glomerular Filtration Rate:
        eGFR_pop = np.zeros(size)            #kidney.org/sites/default/files/docs/11-10-1813_abe_patbro_gfr_b.pdf
    
        #Body Mass Index:
        BMI_pop = np.zeros(size)             #landlaeknir.is/servlet/file/store93/item35880/4950_zbmifl_BMI_UTFEGID.pdf
    
        #Systolic Blood Pressure:
        SBP_pop = np.zeros(size)             #hjarta.is/wp-content/uploads/2019/03/Handbok-Hjartaverndar.pdf
    
        #History of Cigarette Use:
        cig_pop = np.zeros(size)             #https://www.landlaeknir.is/tolfraedi-og-rannsoknir/tolfraedi/heilsa-og-lidan/tobaksnotkun/
    
        #Place holders:
        hla_b_pop = np.zeros(size)           #Does not belong in this function, only here as a placeholder.
        hla_dr_pop = np.zeros(size)          #Does not belong in this function, only here as a placeholder.
        rel_pop = np.zeros(size)             #Could the probably be calculated. What is the likelihood of an Icelander running
                                         #someone as related as first from a randomly choice group of Icelanders.
                                         #Does not belong in this function, only here as a placeholder.
    
        for i in range(size):
        
            if age_pop[i] >= 18 and age_pop[i] <= 29:
            
                if gen_pop[i] == 0:
                
                    if age_pop[i] <= 24:
                        eGFR_pop[i] = np.random.choice(eGFRm18)
                    else:
                        eGFR_pop[i] = np.random.choice(eGFRm25)
                    
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.6925, 0.3075])
                
                elif gen_pop[i] == 1:

                    if age_pop[i] <= 24:
                        eGFR_pop[i] = np.random.choice(eGFRf18)
                    else:
                        eGFR_pop[i] = np.random.choice(eGFRf25)
                    
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.7440, 0.256])
                
            elif age_pop[i] >= 30 and age_pop[i] <= 39:
            
                if gen_pop[i] == 0:

                    if age_pop[i] <= 34:
                        eGFR_pop[i] = np.random.choice(eGFRm30)
                    else:
                        eGFR_pop[i] = np.random.choice(eGFRm35)
                    
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.5837, 0.4163])
                
                elif gen_pop[i] == 1:
                
                    if age_pop[i] <= 34:
                        eGFR_pop[i] = np.random.choice(eGFRf30)
                    else:
                        eGFR_pop[i] = np.random.choice(eGFRf35)                
                
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.6085, 0.3915])
                
            elif age_pop[i] >= 40 and age_pop[i] <= 49:
            
                if gen_pop[i] == 0:
                
                    if age_pop[i] <= 44:
                        eGFR_pop[i] = np.random.choice(eGFRm40)
                    else:
                        eGFR_pop[i] = np.random.choice(eGFRm45)
                    
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.5457, 0.4543])
                
                elif gen_pop[i] == 1:
                
                    if gen_pop[i] == 0:
                
                        if age_pop[i] <= 44:
                            eGFR_pop[i] = np.random.choice(eGFRf40)
                        else:
                            eGFR_pop[i] = np.random.choice(eGFRf45)
                
                        cig_pop[i] = np.random.choice([0, 1], 1, p=[0.5702, 0.4298])
                
            elif age_pop[i] >= 50 and age_pop[i] <= 59:
            
                if gen_pop[i] == 0:
                
                    if age_pop[i] <= 54:
                        eGFR_pop[i] = np.random.choice(eGFRm50)
                    else:
                        eGFR_pop[i] = np.random.choice(eGFRm55)
                    
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.384, 0.616])
                
                elif gen_pop[i] == 1:
                
                    if age_pop[i] <= 54:
                        eGFR_pop[i] = np.random.choice(eGFRf50)
                    else:
                        eGFR_pop[i] = np.random.choice(eGFRf55)
                
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.4553, 0.5447])
            
            elif age_pop[i] >= 60 and age_pop[i] <= 69:
            
                if gen_pop[i] == 0:
                
                    if age_pop[i] <= 64:  
                        eGFR_pop[i] = np.random.choice(eGFRm60)

                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.3371, 0.6629])
                
                elif gen_pop[i] == 1:
                
                    if age_pop[i] <= 64:
                    
                        eGFR_pop[i] = np.random.choice(eGFRf60)
                
                    cig_pop[i] = np.random.choice([0, 1], 1, p=[0.3682, 0.6318])
                
            elif age_pop[i] >= 70 and age_pop[i] <= 79:
                eGFR_pop[i] = 75
            
            if gen_pop[i] == 0:
            
                if age_pop[i] >=18 and age_pop[i] <= 44:
                
                    temp = np.random.choice([0, 1, 2, 3], 1, p=[0.009, 0.376, 0.386, 0.229])
                
                    SBP_pop[i] = 122
                
                    if temp == 0:
                        BMI_pop[i] = np.random.randint(14, 18.49 ,1)
                    elif temp == 1:
                        BMI_pop[i] = np.random.randint(18.5, 25 ,1)
                    elif temp == 2:
                        BMI_pop[i] = np.random.randint(25.01, 30 ,1)
                    elif temp == 3:
                        BMI_pop[i] = np.random.randint(30.01, 47 ,1)
                    
                elif age_pop[i] >=45 and age_pop[i] <= 66:
                
                    temp = np.random.choice([0, 1, 2, 3], 1, p=[0.001, 0.191, 0.522, 0.286])
                
                    SBP_pop[i] = 126
                
                    if temp == 0:
                        BMI_pop[i] = np.random.randint(14, 18.49 ,1)
                    elif temp == 1:
                        BMI_pop[i] = np.random.randint(18.5, 25 ,1)
                    elif temp == 2:
                        BMI_pop[i] = np.random.randint(25.01, 30 ,1)
                    elif temp == 3:
                        BMI_pop[i] = np.random.randint(30.01, 47 ,1)                
                
                elif age_pop[i] >= 67:

                    temp = np.random.choice([0, 1, 2, 3], 1, p=[0.003, 0.27, 0.473, 0.255])
                
                    SBP_pop[i] = 140
                
                    if temp == 0:
                        BMI_pop[i] = np.random.randint(14, 18.49 ,1)
                    elif temp == 1:
                        BMI_pop[i] = np.random.randint(18.5, 25 ,1)
                    elif temp == 2:
                        BMI_pop[i] = np.random.randint(25.01, 30 ,1)
                    elif temp == 3:
                        BMI_pop[i] = np.random.randint(30.01, 47 ,1)                 
            
            elif gen_pop[i] == 1:
                    
                if age_pop[i] >= 18 and age_pop[i] <= 44:
                    
                    temp = np.random.choice([0, 1, 2, 3], 1, p=[0.011, 0.452, 0.269, 0.268])
                    
                    SBP_pop[i] = 108
                    
                    if temp == 0:
                        BMI_pop[i] = np.random.randint(14, 18.49 ,1)
                    elif temp == 1:
                        BMI_pop[i] = np.random.randint(18.5, 25 ,1)
                    elif temp == 2:
                        BMI_pop[i] = np.random.randint(25.01, 30 ,1)
                    elif temp == 3:
                        BMI_pop[i] = np.random.randint(30.01, 47 ,1)
                        
                elif age_pop[i] >= 45 and age_pop[i] <= 66:
                    
                    temp = np.random.choice([0, 1, 2, 3], 1, p=[0.002, 0.343, 0.350, 0.305])
                    
                    SBP_pop[i] = 120
                    
                    if temp == 0:
                        BMI_pop[i] = np.random.randint(14, 18.49 ,1)
                    elif temp == 1:
                        BMI_pop[i] = np.random.randint(18.5, 25 ,1)
                    elif temp == 2:
                        BMI_pop[i] = np.random.randint(25.01, 30 ,1)
                    elif temp == 3:
                        BMI_pop[i] = np.random.randint(30.01, 47 ,1)                
                    
                elif age_pop[i] >= 67:
    
                    temp = np.random.choice([0, 1, 2, 3], 1, p=[0.015, 0.318, 0.413, 0.253])
                    
                    SBP_pop[i] = 140
                    
                    if temp == 0:
                        BMI_pop[i] = np.random.randint(14, 18.49 ,1)
                    elif temp == 1:
                        BMI_pop[i] = np.random.randint(18.5, 25 ,1)
                    elif temp == 2:
                        BMI_pop[i] = np.random.randint(25.01, 30 ,1)
                    elif temp == 3:
                        BMI_pop[i] = np.random.randint(30.01, 47 ,1)
        
        pop = [bt_pop, cig_pop, age_pop, eGFR_pop, BMI_pop, aa_pop, SBP_pop, rel_pop, hla_b_pop, hla_dr_pop, gen_pop]
        pop = np.array(pop,dtype=object)
                    
        return pop