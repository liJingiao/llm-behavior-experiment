import pickle
import numpy as np
import os
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from utils import Embedder, get_texts
import glob


vis_0 = ['prm0_qstvacay--full_idnintersection-1_tmp1.0_mwizard-vicuna-7b-uncensored/', 'prm1_qstvacay--full_idnintersection-1_tmp1.0_mwizard-vicuna-7b-uncensored/', 'prm2_qstvacay--full_idnintersection-1_tmp1.0_mwizard-vicuna-7b-uncensored/', 'prm3_qstvacay--full_idnintersection-1_tmp1.0_mwizard-vicuna-7b-uncensored/'] # wizard censured, 4 prompts comparison

vis_1 = ['prm0_qstvacay--full_idnintersection-1_tmp1.0_mllama-2-7b/', 'prm1_qstvacay--full_idnintersection-1_tmp1.0_mllama-2-7b/', 'prm2_qstvacay--full_idnintersection-1_tmp1.0_mllama-2-7b/', 'prm3_qstvacay--full_idnintersection-1_tmp1.0_mllama-2-7b/'] # 

vis_2 = ['prm0_qstvacay-full_idnintersection-1_tmp1.0_mgpt-3.5-turbo/2023-07-10_09:15:06.pkl', 'prm1_qstvacay-full_idnintersection-1_tmp1.0_mgpt-3.5-turbo/2023-07-10_09:44:42.pkl', 'prm2_qstvacay-full_idnintersection-1_tmp1.0_mgpt-3.5-turbo/2023-07-10_10:46:46.pkl', 'prm3_qstvacay--full_idnintersection-1_tmp1.0_mgpt-3.5-turbo/'] # gpt-3.5

vis_3 = ['prm0_qstvacay-full_idnintersection-1_tmp1.0_mgpt-4/2023-07-11_16:21:33.pkl', 'prm1_qstvacay-full_idnintersection-1_tmp1.0_mgpt-4/2023-07-11_16:24:43.pkl', 'prm2_qstvacay-full_idnintersection-1_tmp1.0_mgpt-4/2023-07-11_16:25:09.pkl', 'prm3_qstvacay--full_idnintersection-1_tmp1.0_mgpt-4/'] # gpt-4 full prompts
vises = [vis_0, vis_1, vis_2, vis_3]

fig, axes = plt.subplots(4, 2, figsize=(10, 16))
fontsize=15
names = ['Prompt 1', 'Prompt 2', 'Prompt 3', 'Prompt 4']
model_names = ['Wizard Vicuna Uncensored 7b', 'LLaMA-2 7b', 'GPT-3.5', 'GPT-4']
for v_ind, vis in enumerate(vises):
    paragraphs = get_texts(vis)
    numbers = [paragraph[0] for paragraph in paragraphs]
    print(np.unique(numbers, return_counts=True))
    all_paragraphs =  [paragraph[1].lower() for paragraph in paragraphs]
    print("len all sentences: {}".format(len(all_paragraphs)))
    embedder = Embedder(all_paragraphs)

    for e_ind, e_version in enumerate([1, 3]):
        embeddings = []
        for paragraph in all_paragraphs:
            try:
                embeddings.append(embedder.embed_paragraph(paragraph, version=e_version))
            except Exception as error:
                print(error)
                print(len(paragraph))

        all_embeddings = TSNE().fit_transform(np.array(embeddings))
        for e in range(len(embeddings)):
            axes[v_ind][e_ind].scatter(all_embeddings[e][0], all_embeddings[e][1], c = 'C{}'.format(paragraphs[e][0]))
            #if np.random.randint(0, 5) == 0:
            #    print("---{0}---: {1}\n".format(sentences[e][0], sentences[e][1]))
        if e_ind == 0: 
            for v in range(len(vis)):
                axes[v_ind][e_ind].scatter([], [], c='C{}'.format(v), label=names[v])
        axes[v_ind][e_ind].tick_params(axis='x', labelsize=fontsize)
        axes[v_ind][e_ind].tick_params(axis='y', labelsize=fontsize)
    axes[v_ind][0].set_ylabel(model_names[v_ind], fontsize=fontsize)
axes[0][0].legend(fontsize=fontsize)
axes[0][0].set_title('Ngram', fontsize=fontsize)
axes[0][1].set_title('SBERT', fontsize=fontsize)
plt.tight_layout()
plt.savefig('analysis_results/vis_promptchoice.png', dpi=200)
plt.close()



