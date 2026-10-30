import pandas as pd
import numpy as np

model_result = dict()

def get_consistency(result_path_list, behavior):
    
    for path in result_path_list:
        Consis_num, Incosis_num, high_consis, low_consis = 0, 0, 0, 0
        df = pd.read_csv(path)
        model_name = path.split("/")[-1].split("_")[0][:-3]
        for i in range(len(df)):
            standard_result = df.iloc[i]['result1']
            preturbed_result = df.iloc[i]['result2']
            if standard_result.split(',')[0] == preturbed_result.split(',')[0]:
                Incosis_num += 1 
                
            else:
                Consis_num += 1
                if i < 680:
                    high_consis += 1
                else:
                    low_consis += 1
                
        if behavior == 'total': 
            Consis_num, Incosis_num = Incosis_num, Consis_num
            total_num = Incosis_num + Consis_num
            high_consis, low_consis = 680 - high_consis, (Consis_num + Incosis_num - 680) - low_consis
        model_result[model_name][behavior]['ans'] = Consis_num / (Consis_num + Incosis_num)
        model_result[model_name][behavior]['high_ambiguity'] = high_consis / 680
        model_result[model_name][behavior]['low_ambiguity'] = low_consis / (Consis_num + Incosis_num - 680)

if __name__ == '__main__':
    from glob import glob
    normal_result_path_list = glob('../data/ab/normal/*')
    id_result_path_list = glob('../data/ab/id/*')
    total_result_path_list = glob('../data/ab/total/*')
    with open('eval_model_list.txt') as f: 
        lines = f.readlines()
        for line in lines:
            model_name = line.split("/")[-1].strip("\n")
            if model_name not in model_result:
                model_result[model_name] = {
                    'normal': -1,
                    'id': -1,
                    'total': -1,
                    }
                for behavior in model_result[model_name].keys():
                    model_result[model_name][behavior] = {
                        'ans': -1,
                        'high_ambiguity': -1,
                        'low_ambiguity': -1
                    }
            

    get_consistency(normal_result_path_list, normal_result_path_list[0].split("/")[-2])
    get_consistency(id_result_path_list, id_result_path_list[0].split("/")[-2])
    get_consistency(total_result_path_list, total_result_path_list[0].split("/")[-2])
    from pprint import pprint

    for key in model_result.keys():
        
        for b_key in model_result[key].keys():
            line_output = f"{key} "
            for a_key in model_result[key][b_key].keys():
                consis = model_result[key][b_key][a_key] * 100
                segment = f'& $ {consis:.1f} $ '
            
            # segment = f'& $ {avg:.3f} \pm {var:.3f} $ '
                line_output += segment
            line_output += "\\\\"
            print(b_key)
            print(line_output)
    


