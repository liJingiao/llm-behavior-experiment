import json
import torch
import numpy as np
import pandas as pd
import transformers
from tqdm import tqdm
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

tqdm.pandas()
from util import parse_arguments


question_type = ['ab_check']   
questions = []
for t in question_type:
    with open(f'../data/question_templates/{t}.json', 'r') as f:
        questions.append(json.load(f))

device = 'cuda:1'

normal_template = '''
{system_prompt}\n
{user_message}\n
Answer:
'''
        
llama_template = '''
<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_message} [/INST]\n
Answer:
'''

def generate_logits_answer(q_type, model_path, behavior):
    '''
    method follows mainstream evalution framework.
    access option id with maximum output probability.
    '''
    model = AutoModelForCausalLM.from_pretrained(model_path).to(device)#, device_map='auto')
    model = model.eval()
    tokenizer = AutoTokenizer.from_pretrained(model_path, unk_token='<unk>')
    
    def produce_probs(prompt):
        ### this part is from original MMLU implementation
        input_ids = tokenizer(prompt, return_tensors='pt').input_ids.to(device)
        logits = model(input_ids=input_ids).logits[0][-1]
        option_id = [tokenizer("A").input_ids[-1], tokenizer("B").input_ids[-1]]
        prob = torch.Tensor([logits[index] for index in option_id])
        probs = torch.nn.functional.softmax(
            prob, dim=0
        ).detach().cpu().to(torch.float32).numpy()
        if np.argmax(probs) == 0:
            return "A" + "," + str(probs[0])
        elif np.argmax(probs) == 1:
            return "B" + "," + str(probs[1])
           
    for q in questions:
        if q['name'] == q_type:
            question_template = q
            break
    df = pd.read_csv('../data/moralchoice_all.csv')
    answer_list = []
    print(model_path.split('/')[-1])
    print(model_path.split('/')[-1].startswith('Llama'))
    for i in tqdm(range(len(df))):
        template = llama_template if model_path.split('/')[-1].startswith('Llama') else normal_template 
        
        A_pattern, B_pattern = 'A. ', 'B. '
        if behavior == 'normal':
            action1, action2 = A_pattern + df.iloc[i]['action1'], B_pattern + df.iloc[i]['action2']
            reversed_action1, reversed_action2 = A_pattern + df.iloc[i]['action2'], B_pattern + df.iloc[i]['action1']
        if behavior == 'id': 
            action1, action2 = A_pattern + df.iloc[i]['action1'], B_pattern + df.iloc[i]['action2']
            reversed_action1, reversed_action2 = B_pattern + df.iloc[i]['action1'], A_pattern + df.iloc[i]['action2']
        elif behavior == 'total':
            action1, action2 = A_pattern + df.iloc[i]['action1'], B_pattern + df.iloc[i]['action2']
            reversed_action1, reversed_action2 = B_pattern + df.iloc[i]['action2'], A_pattern + df.iloc[i]['action1']
    
        q1 = question_template['question'].format(df.iloc[i]['question'], action1, action2)
        q2 = question_template['question'].format(df.iloc[i]['question'], reversed_action1, reversed_action2)

        result1 = produce_probs(template.format(system_prompt=q['question_header'], user_message=q1))
        result2 = produce_probs(template.format(system_prompt=q['question_header'], user_message=q2))
        
        answer_list.append([result1, result2])
    ans = pd.DataFrame(answer_list, columns=['result1', 'result2'])
    ans.to_csv('../result/probs/{}/{}.csv'.format(behavior, model_path.split('/')[-1] + "-" + q_type), index=False)



def generate_answer(q_type, model_path, behavior, temperature, do_sample:bool):
    '''
    generate answer for these settings:
    1. greedy, temperature=0
    2. sample, temperature=0
    3. sample, temperature=1
    '''
    model = AutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path, unk_token='<unk>')
    pipeline = transformers.pipeline(
    'text-generation',
    model=model,
    tokenizer=tokenizer,
    device_map='auto',
    do_sample=do_sample,
    # top_k=10,
    temperature=temperature,
    max_new_tokens=128,
    min_new_tokens=1,
    )

    def get_output(prompt):
        sequences = pipeline(prompt, eos_token_id=tokenizer.eos_token_id)
        output = sequences[0]['generated_text'].replace(prompt, "", 1).strip("\n")
        return output

    for q in questions:
        if q['name'] == q_type:
            question_template = q
            break
    df = pd.read_csv('../data/moralchoice_all.csv')
    answer_list = []

    for i in tqdm(range(len(df))):
        template = llama_template if model_path.split('/')[-1].startswith('Llama') else normal_template 
        
        A_pattern, B_pattern = 'A. ', 'B. '
        if behavior == 'normal':
            action1, action2 = A_pattern + df.iloc[i]['action1'], B_pattern + df.iloc[i]['action2']
            reversed_action1, reversed_action2 = A_pattern + df.iloc[i]['action2'], B_pattern + df.iloc[i]['action1']
        if behavior == 'id':
            action1, action2 = A_pattern + df.iloc[i]['action1'], B_pattern + df.iloc[i]['action2']
            reversed_action1, reversed_action2 = B_pattern + df.iloc[i]['action1'], A_pattern + df.iloc[i]['action2']
        elif behavior == 'total':
            action1, action2 = A_pattern + df.iloc[i]['action1'], B_pattern + df.iloc[i]['action2']
            reversed_action1, reversed_action2 = B_pattern + df.iloc[i]['action2'], A_pattern + df.iloc[i]['action1']
    
        q1 = question_template['question'].format(df.iloc[i]['question'], action1, action2)
        q2 = question_template['question'].format(df.iloc[i]['question'], reversed_action1, reversed_action2)
        
        result1 = get_output(template.format(system_prompt=q['question_header'], user_message=q1))
        result2 = get_output(template.format(system_prompt=q['question_header'], user_message=q2))

        answer_list.append([result1, result2])
    ans = pd.DataFrame(answer_list, columns=['result1', 'result2'])
    ans.to_csv('../data/{}/{}.csv'.format(behavior, model_path.split('/')[-1] + "-" + q_type), index=False)



if __name__ == '__main__':
    args = parse_arguments()

    behaviors = ["normal", "id", "total"]
    with open('eval_model_list.txt', 'r') as f:
        lines = f.readlines()
        for model_path in lines:
            model_path = model_path.strip("\n")
            for behavior in behaviors:
                generate_logits_answer(args.task, model_path, behavior)
                torch.cuda.empty_cache()

    
  