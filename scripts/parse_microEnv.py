import pandas as pd
import numpy as np
import os

def parse_microEnvironment(personalGoogleDrivePath):
    #get Data
    microEnvFilePath = os.path.join(personalGoogleDrivePath,"RISE2020/data/2020_Raanan/listOfMicroEnv_sup.tsv")
    microDF = pd.read_csv(microEnvFilePath,sep="\t",header=0)
    
    #Deal with ID patterns with two underscores
    # 5jfn.1VU_A_601 
    microDFTwoU = microDF[microDF.ID.str.count('_') == 2]

    #split ID into columns that have a prefix id_
    microDFTwoU = microDFTwoU.join(microDFTwoU.ID.str.split('\.|_', expand=True).add_prefix('id_'))

    #rename columns to the correct value identification
    microDFTwoU.rename(columns={'id_0':'pdbID',
                                'id_1':'cofactor_id',
                                'id_2':'chainID',
                                'id_3':'residueNum'},
                                inplace=True)
    microDFTwoU = microDFTwoU.loc[:,~microDFTwoU.columns.duplicated()]
    # print(microDFTwoU.columns)

    # Deal with ID patterns with three underscores
    # 5k0a.ADE_FAD_D_403
    microDFThreeU = microDF[microDF.ID.str.count('_') == 3] 
    #split ID into columns that have a prefix id_
    microDFThreeU = microDFThreeU.join(microDFThreeU.ID.str.split('\.|_', expand=True).add_prefix('id_'))

    #rename columns to the correct value identification
    microDFThreeU.rename(columns={'id_0':'pdbID',
                                'id_1':'cofactor_id',
                                'id_2':'cofactor_id2',
                                'id_3':'chainID',
                                'id_4':'residueNum'},
                                inplace=True)
    microDFThreeU = microDFThreeU.loc[:,~microDFThreeU.columns.duplicated()]
    
    #Add a cofactor_id2 column and explicitly set the column to NaN values since these IDs do not have cofactor_id2
    #when concatenating microDFTwoU and microDFThreeU below - this should be taken care of anyway - I am doing it just to be sure
    microDFTwoU['cofactor_id2'] = np.nan

    # combine dfTwo and dfThree
    dfTwo_Three = pd.concat([microDFTwoU,microDFThreeU],axis=0,ignore_index=True,sort=False)
    return(dfTwo_Three)

#main function controls everyone
def main():
    personalGoogleDrivePath = "/Users/ken/googleDrive/proj/ENIGMA" #change it to yours - use forward slashes and ***do not add one to the end of the string
    dfMicroEnv = parse_microEnvironment(personalGoogleDrivePath)
    print(dfMicroEnv.columns) #check to see if you get the information you expected
    # output
    # Index(['ID', 'module', 'cofactor_id', 'cofactor_type', 'ec', 'name', 'species',
    #    'superkingdom', 'pdbID', 'chainID', 'residueNum', 'cofactor_id2'],
    #   dtype='object')
    print("*******dfHEAD",dfMicroEnv.head(5)) #note the ID pattern
    print("*******dfTAIL",dfMicroEnv.tail(5)) #note the ID pattern
    # output
    #     *******dfHEAD                ID  module cofactor_id cofactor_type  ... pdbID chainID residueNum cofactor_id2
    # 0  5jfn.1VU_A_601       7         1VU           Nuc  ...  5jfn       A        601          NaN
    # 1  5jfn.COA_B_601       7         COA           Nuc  ...  5jfn       B        601          NaN
    # 2  5jfn.COA_C_601       7         COA           Nuc  ...  5jfn       C        601          NaN
    # 3  5jfn.COA_D_601       7         COA           Nuc  ...  5jfn       D        601          NaN
    # 4  5iuv.NAD_A_700       7         NAD           Nuc  ...  5iuv       A        700          NaN

    # [5 rows x 12 columns]
    # *******dfTAIL                        ID  module cofactor_id cofactor_type  ... pdbID chainID residueNum cofactor_id2
    # 40228  5k0a.ADE_FAD_D_403    2453         ADE           Nuc  ...  5k0a       D        403          FAD
    # 40229  5n0j.ADE_FAD_A_402    2453         ADE           Nuc  ...  5n0j       A        402          FAD
    # 40230  5n0j.ADE_FAD_B_402    2453         ADE           Nuc  ...  5n0j       B        402          FAD
    # 40231  5ode.ADE_FAD_A_401    2453         ADE           Nuc  ...  5ode       A        401          FAD
    # 40232  5ode.ADE_FAD_B_401    2453         ADE           Nuc  ...  5ode       B        401          FAD

    # [5 rows x 12 columns]

#call the main function to execute all the commands
main()