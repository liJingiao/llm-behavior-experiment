import os
import openai
import pickle
import llm_prompts as oip
import time
import datetime
import argparse
from utils import *
import csv
from scipy.stats import wasserstein_distance
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_distances
from vendi_score import vendi
from sklearn.covariance import empirical_covariance
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from top2vec import Top2Vec
import umap
import hdbscan
import random
import gzip
from sklearn.decomposition import PCA
from statsmodels.stats.proportion import proportion_confint
from scipy.stats import ttest_ind
from sklearn.metrics import pairwise_distances
from sklearn.metrics import jaccard_score

parser = argparse.ArgumentParser()
parser.add_argument('--models', nargs='+', type=int, default=1, help='1 is wvuncensored, 2 is llama-2, 3 is gpt-3.5, 4 is gpt-4, 5 is in-group, 6 is out-group')
parser.add_argument('--save_loc', type=str, default="try", help='save location')
parser.add_argument('--clean', action='store_true', default=False, help='on data cleaned of identity words, e.g., "woman" ')
args = parser.parse_args()

prefix_path = '' # set to be where data is

system_prompt = 2

rand_33 = pickle.load(open('files/33.pkl', 'rb')) # for runs where we only need 33 of the samples

embedder = Embedder()
start_time = time.time()

if type(args.models) is int:
    args.models = [args.models]

# save all numbers so in another file can generate visualizations
all_model_nums = {}

if not os.path.exists('files/fitted_pca.pkl'):
    # from https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/distillation/dimensionality_reduction.py
    #nli_dataset_path = 'https://sbert.net/datasets/AllNLI.tsv.gz'
    nli_dataset_path = 'AllNLI.tsv.gz'
    nli_dataset_path = 'AllNLI.tsv'
    nli_sentences = set()
    with open(nli_dataset_path, 'rt', encoding='utf8') as fIn:
        reader = csv.DictReader(fIn, delimiter='\t', quoting=csv.QUOTE_NONE)
        for row in reader:
            nli_sentences.add(row['sentence1'])
            nli_sentences.add(row['sentence2'])

    nli_sentences = list(nli_sentences)
    random.shuffle(nli_sentences)

    #To determine the PCA matrix, we need some example sentence embeddings.
    #Here, we compute the embeddings for 20k random sentences from the AllNLI dataset
    pca_train_sentences = nli_sentences[0:20000]
    train_embeddings = np.array([embedder.embed_paragraph(paragraph, version=3) for paragraph in pca_train_sentences])

    #Compute PCA on the train embeddings matrix
    new_dimension = 10
    pca = PCA(n_components=new_dimension)
    pca.fit(train_embeddings)
    pickle.dump(pca, open('files/fitted_pca.pkl', 'wb'))
pca = pickle.load(open('files/fitted_pca.pkl', 'rb'))

def diversity_analysis_4(identity_axis, model_name, user_prompt, system_prompt, three_identities, R2_ind=-1, boot_result=False, to_print=False):
    if len(three_identities) == 1:
        identity = '{0}-{1}'.format(identity_axis, three_identities[0])
        file_name = "{0}_{1}_{2}_{3}".format(model_name, user_prompt, identity, system_prompt)
        loc = folder+'/'+file_name+'.pkl'
        e_loc = e_folder+file_name+'.pkl'
        all_embeddings = np.array(pickle.load(open(e_loc, 'rb')))[:99]
        all_mcs = np.array(get_mcs(folder+'/mc/'+file_name+'.pkl'))[:99]
        all_texts = np.array([chunk[1] for chunk in get_texts([loc])])[:99]
        if args.clean:
            all_texts = [clean_all(paragraph, identity, user_prompt) for paragraph in all_texts]
    else:
        assert len(three_identities) == 3
        all_embeddings = []
        all_texts = []
        all_mcs = []
        for id_i in range(3):
            i = three_identities[id_i]
            identity = '{0}-{1}'.format(identity_axis, i)
            file_name = "{0}_{1}_{2}_{3}".format(model_name, user_prompt, identity, system_prompt)
            loc = folder+'/'+file_name+'.pkl'
            e_loc = e_folder+file_name+'.pkl'
            llm_embeddings = np.array(pickle.load(open(e_loc, 'rb')))
            mcs = np.array(get_mcs(folder+'/mc/'+file_name+'.pkl'))
            paragraphs = np.array([chunk[1] for chunk in get_texts([loc])])
            if 'R2b' in user_prompt:
                assert R2_ind != -1
                if 'race' in user_prompt:
                    paragraphs = np.concatenate([clean_R2b(paragraph, version=0) for paragraph in paragraphs])
                elif 'gender' in user_prompt:
                    paragraphs = np.concatenate([clean_R2b(paragraph, version=1) for paragraph in paragraphs])
                else:
                    assert False

                indices = np.reshape(np.arange(len(llm_embeddings)), (-1, 3))[:, R2_ind]
                llm_embeddings = np.array(llm_embeddings)[indices]
                mcs = np.array(mcs)[indices] 
                paragraphs = np.array(paragraphs)[indices] 

            if args.clean:
                paragraphs = np.array([clean_all(paragraph, identity, user_prompt) for paragraph in paragraphs])

            if len(llm_embeddings) == 100:
                all_embeddings.extend(llm_embeddings[rand_33])
                all_texts.extend(paragraphs[rand_33])
                all_mcs.extend(mcs[rand_33])
            else:
                assert len(mcs) == len(llm_embeddings) == len(paragraphs) == 33, "Embeddings: {0}, Texts: {1}".format(len(llm_embeddings), len(paragraphs))
                all_embeddings.extend(llm_embeddings)
                all_texts.extend(paragraphs)
                all_mcs.extend(mcs)
    assert len(all_embeddings) == 99, len(all_embeddings)
    assert len(all_texts) == 99, len(all_texts)
    assert len(all_mcs) == 99, len(all_mcs)

    all_hdb_clusters = []
    all_embeddings = np.array(all_embeddings)

    pca_embeddings = pca.transform(all_embeddings)
    cov = empirical_covariance(pca_embeddings)
    det = np.linalg.det(cov)

    all_cos_distances = cosine_distances(all_embeddings)
    vendi_score = vendi.score_K(all_cos_distances)

    all_mcs = np.array(all_mcs)
    unique_mcs = np.unique(all_mcs)
    unique_mcs = len(set(np.arange(1, 6))&set(unique_mcs))

    # vendi score
    if boot_result:
        all_vendis = []
        all_dets = []
        all_boot_mcs = []
        for boot in range(1000):
            indices = np.random.choice(np.arange(len(all_embeddings)), size=len(all_embeddings), replace=True)
            sampled_embeddings = all_embeddings[indices]
            cos_distances = cosine_distances(sampled_embeddings)
            all_vendis.append(vendi.score_K(cos_distances))
            all_dets.append(np.linalg.det(empirical_covariance(pca_embeddings[indices])))

            all_boot_mcs.append(len(set(np.arange(1, 6))&set(np.unique(all_mcs[indices]))))
        all_vendis = np.sort(all_vendis)
        vendi_score = [all_vendis[24], vendi_score, all_vendis[974]] # don't do yet til we know what's happening
        all_dets = np.sort(all_dets)
        det = [all_dets[24], det, all_dets[974]]
        all_boot_mcs = np.sort(all_boot_mcs)
        unique_mcs = [all_boot_mcs[24], unique_mcs, all_boot_mcs[974]]

    if to_print:
        rand = np.random.choice(np.arange(len(all_texts)), size=5)
        print(np.array(all_texts)[rand])
    
    return [vendi_score, det, unique_mcs]

def analyze_distance_3(llm_embeddings, in_embeddings, out_embeddings, llm_mcs, in_mcs, out_mcs, llm_paragraphs, in_paragraphs, out_paragraphs):

    ## n-gram 
    vectorizer = CountVectorizer(ngram_range=(1, 2), max_features = 10000)

    all_paragraphs = np.concatenate([llm_paragraphs, in_paragraphs, out_paragraphs])
    all_paragraphs = [paragraph.strip().lower() for paragraph in all_paragraphs]
    vectorizer.fit(all_paragraphs)
    llm_ngrams = vectorizer.transform(llm_paragraphs).toarray()
    in_ngrams = vectorizer.transform(in_paragraphs).toarray()
    out_ngrams = vectorizer.transform(out_paragraphs).toarray()
    
    mat_cos_in_distances = pairwise_distances(llm_ngrams>0, in_ngrams>0, metric='jaccard')
    mat_cos_out_distances = pairwise_distances(llm_ngrams>0, out_ngrams>0, metric='jaccard')
    ngram_a_in_dists = np.sort(mat_cos_in_distances.flatten())
    ngram_a_out_dists = np.sort(mat_cos_out_distances.flatten())
    ngram_b_in_dists = np.amin(mat_cos_in_distances, axis=1)
    ngram_b_out_dists = np.amin(mat_cos_out_distances, axis=1)

    ## (a) pairwise distances
    mat_cos_in_distances = cosine_distances(llm_embeddings, in_embeddings)
    mat_cos_out_distances = cosine_distances(llm_embeddings, out_embeddings)
    a_in_dists = np.sort(mat_cos_in_distances.flatten())
    a_out_dists = np.sort(mat_cos_out_distances.flatten())

    ## (b) for every LLM-generated instance, take its closest point from human set A and human set B
    b_in_dists = np.amin(mat_cos_in_distances, axis=1)
    b_out_dists = np.amin(mat_cos_out_distances, axis=1)

    ## MC 
    c_in_dist = wasserstein_distance(llm_mcs, in_mcs)
    c_out_dist = wasserstein_distance(llm_mcs, out_mcs)
    d_in_dist = np.mean(llm_mcs) - np.mean(in_mcs)
    d_out_dist = np.mean(llm_mcs) - np.mean(out_mcs)
    all_c_in_dists = []
    all_c_out_dists = []
    all_d_in_dists = []
    all_d_out_dists = []
    for boot in range(1000):
        these_llm_mcs = np.random.choice(llm_mcs, size=len(llm_mcs), replace=True)
        these_in_mcs = np.random.choice(in_mcs, size=len(in_mcs), replace=True)
        these_out_mcs = np.random.choice(out_mcs, size=len(out_mcs), replace=True)

        all_c_in_dists.append(wasserstein_distance(these_llm_mcs, these_in_mcs))
        all_c_out_dists.append(wasserstein_distance(these_llm_mcs, these_out_mcs))
        all_d_in_dists.append(np.mean(these_llm_mcs) - np.mean(these_in_mcs))
        all_d_out_dists.append(np.mean(these_llm_mcs) - np.mean(these_out_mcs))

    all_c_in_dists = np.sort(all_c_in_dists)
    all_c_out_dists = np.sort(all_c_out_dists)
    # 24 is 1000*.05 and 974 is 
    # 83% would be 1000*.17, 85 so 84 and 915 so 914
    c_in_dist = [all_c_in_dists[24], all_c_in_dists[84], c_in_dist, all_c_in_dists[914], all_c_in_dists[974]]
    c_out_dist = [all_c_out_dists[24], all_c_out_dists[84], c_out_dist, all_c_out_dists[914], all_c_out_dists[974]]

    all_d_in_dists = np.sort(all_d_in_dists)
    all_d_out_dists = np.sort(all_d_out_dists)
    d_in_dist = [all_d_in_dists[24], all_d_in_dists[84], d_in_dist, all_d_in_dists[914], all_d_in_dists[974]]
    d_out_dist = [all_d_out_dists[24], all_d_out_dists[84], d_out_dist, all_d_out_dists[914], all_d_out_dists[974]]

    return ngram_a_in_dists, ngram_a_out_dists, ngram_b_in_dists, ngram_b_out_dists, a_in_dists, a_out_dists, b_in_dists, b_out_dists, c_in_dist, c_out_dist, d_in_dist, d_out_dist

def within_group_2(llm_embeddings, paragraphs, llm_mcs):
    ## (a) unique n-grams (n=[1, 2])
    vectorizer = CountVectorizer(ngram_range=(1, 2))

    all_feature_names = {}
    min_thresh = int(.05 * len(paragraphs))
    for p in range(len(paragraphs)):
        try:
            features = vectorizer.fit_transform([paragraphs[p]])
            feature_names = vectorizer.get_feature_names_out()
        except ValueError:
            feature_names = []
        for feature_name in feature_names:
            if feature_name not in all_feature_names.keys():
                all_feature_names[feature_name] = 0
            all_feature_names[feature_name] += 1

    unique_props = []
    for p in range(len(paragraphs)):
        try:
            features = vectorizer.fit_transform([paragraphs[p]])
            feature_names = vectorizer.get_feature_names_out()
        except:
            feature_names = []
        unique = 0
        for feature_name in feature_names:
            if all_feature_names[feature_name] <= (1+min_thresh):
                unique += 1

        if len(feature_names) != 0:
            unique_props.append(unique/len(feature_names))
    
    unique_means = []
    for boot in range(1000):
        unique_means.append(np.mean(np.random.choice(unique_props, size=len(unique_props), replace=True)))
    unique_means = np.sort(unique_means)
    unique_means = [unique_means[24], unique_means[84], np.mean(unique_props), unique_means[914], unique_means[974]]
    assert np.mean(unique_props) > unique_means[0]
    assert np.mean(unique_props) < unique_means[4]

    ## (b) average pairwise on Sbert
    all_cos_distances = cosine_distances(llm_embeddings)

    flat_distances = np.sort(all_cos_distances.flatten())
    assert np.sum(flat_distances[:len(llm_embeddings)]) == 0
    sorted_cos_distances = flat_distances[len(llm_embeddings):] # to get rid of the self-distances
    assert sorted_cos_distances[-1] == sorted_cos_distances[-2]
    assert sorted_cos_distances[-3] == sorted_cos_distances[-4]
    all_dists = []

    cov_trace = empirical_covariance(llm_embeddings).trace()
    all_traces = []
    all_vendis = []
    llm_embeddings = np.array(llm_embeddings)

    unique_mcs = np.unique(llm_mcs)
    unique_mcs = len(set(np.arange(1, 6))&set(unique_mcs))
    all_unique_mcs = []
    llm_mcs = np.array(llm_mcs)

    for boot in range(1000):
        indices = np.random.choice(np.arange(len(llm_embeddings)), size=len(llm_embeddings), replace=True)
        all_dists.append(np.mean(np.random.choice(sorted_cos_distances, size=(len(sorted_cos_distances)//2), replace=True)))

        sampled_embeddings = llm_embeddings[indices]
        this_cov_trace = empirical_covariance(sampled_embeddings).trace()
        all_traces.append(this_cov_trace)

        all_unique_mcs.append(len(set(np.arange(1, 6))&set(np.unique(llm_mcs[indices]))))

    all_dists = np.sort(all_dists)
    pairwise_dists = [all_dists[24], all_dists[84], np.mean(sorted_cos_distances), all_dists[914], all_dists[974]]
    assert np.mean(sorted_cos_distances) > pairwise_dists[0]
    assert np.mean(sorted_cos_distances) < pairwise_dists[4]

    ## (c) trace of covariance on Sbert
    all_traces = np.sort(all_traces)
    cov_trace = [all_traces[24], all_traces[84], cov_trace, all_traces[914], all_traces[974]]

    ## (d) MC: number of distinct answers
    all_unique_mcs = np.sort(all_unique_mcs)
    unique_mcs = [all_unique_mcs[24], all_unique_mcs[84], unique_mcs, all_unique_mcs[914], all_unique_mcs[974]]

    return unique_means, pairwise_dists, cov_trace, unique_mcs

def sample_distances(embeddings_a, sample_size, embeddings_b=None):
    if embeddings_b is None:
        all_cos_distances = cosine_distances(embeddings_a)
        flat_distances = np.sort(all_cos_distances.flatten())
        assert np.sum(flat_distances[:len(embeddings_a)]) == 0
        sorted_cos_distances = flat_distances[len(embeddings_a):] # to get rid of the self-distances
        assert sorted_cos_distances[-1] == sorted_cos_distances[-2]
        assert sorted_cos_distances[-3] == sorted_cos_distances[-4]
    else:
        all_cos_distances = cosine_distances(embeddings_a, embeddings_b)
        flat_distances = np.sort(np.triu(all_cos_distances).flatten())
        if len(embeddings_a) % 2 == 0:
            assert len(embeddings_a) == 100, len(embeddings_a)
            num_zero = (len(embeddings_a)-1)*(len(embeddings_a)//2)
        else:
            assert len(embeddings_a) == 33, len(embeddings_a)
            num_zero = (len(embeddings_a)-1)*(len(embeddings_a)//2) + (len(embeddings_a)//2)
        assert np.sum(flat_distances[:num_zero]) == 0
        sorted_cos_distances = flat_distances[num_zero:] # to get rid of the self-distances
    return np.random.choice(sorted_cos_distances, size=sample_size, replace=True)

def different_1(embeddings_a, mcs_a, embeddings_b, mcs_b):
    
    within_dists = np.concatenate([sample_distances(embeddings_a, 500), sample_distances(embeddings_b, 500)])
    across_dists = sample_distances(embeddings_a, 1000, embeddings_b=embeddings_b)
    tstat, p_t = ttest_ind(across_dists, within_dists, equal_var=False, alternative='greater')
    chisq, p_chi = chisq_homogeneity(mcs_a, mcs_b)
    return tstat, p_t, chisq, p_chi

# embeddings are needed for all
for model in args.models:
    model_name, folder = oip.model_info[model]
    if 'human' in model_name:
        continue
    print("MODEL NAME: {}".format(model_name))

    if args.clean:
        e_folder = prefix_path+'llm_responses/{}/sbert_embeddings_clean/'.format(folder)
    else:
        e_folder = prefix_path+'llm_responses/{}/sbert_embeddings/'.format(folder)
    if not os.path.exists(e_folder):
        os.makedirs(e_folder)

    model_configs = oip.configs[model_name]
    for identity_axis in model_configs.keys():
        identity_time = time.time()
        for user_prompt in model_configs[identity_axis]:
            for i, identity_name in enumerate(oip.identities[identity_axis]):
                if identity_name in ['a person with a permanent physical disability', 'a person who is blind or has low vision']: # not used
                    continue

                identity = '{0}-{1}'.format(identity_axis, i)
                if identity_axis == 'intersection': 
                    if ('R1' in user_prompt) or ('R2a' in user_prompt):
                        for name_ind in [0, 1]:
                            file_name = "{0}_{1}_{2}-{4}_{3}".format(model_name, user_prompt, identity, system_prompt, name_ind)

                            loc = folder+'/'+file_name+'.pkl'
                            e_loc = e_folder+file_name+'.pkl'

                            if os.path.exists(e_loc): ## so if it has already done this, it won't do it again
                                continue

                            paragraphs = [chunk[1] for chunk in get_texts([loc])]
                            if args.clean:
                                paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in paragraphs]
                            embeddings = np.array([embedder.embed_paragraph(paragraph, version=3) for paragraph in paragraphs])
                            pickle.dump(embeddings, open(e_loc, 'wb'))

                        # generic identity
                        if i == 0:
                            if user_prompt == 'R2a-healthcare-full':
                                more_prompts = ['R2a-criminaljustice-full', 'R2a-immigration-full', 'R2a-climatechange-full']
                                for more_prompt in more_prompts:
                                    file_name = "{0}_{1}_{2}_{3}".format(model_name, more_prompt, 'other-47', system_prompt)

                                    loc = folder+'/'+file_name+'.pkl'
                                    e_loc = e_folder+file_name+'.pkl'
                                    if os.path.exists(e_loc): ## won't get same embeddings
                                        continue

                                    paragraphs = [chunk[1] for chunk in get_texts([loc])]
                                    if args.clean:
                                        paragraphs = [clean_all(paragraph, 'other-47', user_prompt) for paragraph in paragraphs]
                                    embeddings = np.array([embedder.embed_paragraph(paragraph, version=3) for paragraph in paragraphs])
                                    pickle.dump(embeddings, open(e_loc, 'wb'))

                            file_name = "{0}_{1}_{2}_{3}".format(model_name, user_prompt, 'other-47', system_prompt)
                            loc = folder+'/'+file_name+'.pkl'
                            e_loc = e_folder+file_name+'.pkl'
                            if os.path.exists(e_loc): 
                                continue

                            paragraphs = [chunk[1] for chunk in get_texts([loc])]
                            if args.clean:
                                paragraphs = [clean_all(paragraph, 'other-47', user_prompt) for paragraph in paragraphs]
                            embeddings = np.array([embedder.embed_paragraph(paragraph, version=3) for paragraph in paragraphs])
                            pickle.dump(embeddings, open(e_loc, 'wb'))

                file_name = "{0}_{1}_{2}_{3}".format(model_name, user_prompt, identity, system_prompt)
                loc = folder+'/'+file_name+'.pkl'
                e_loc = e_folder+file_name+'.pkl'

                if os.path.exists(e_loc): 
                    continue

                paragraphs = [chunk[1] for chunk in get_texts([loc])]

                if 'R2b' in user_prompt:
                    if 'race' in user_prompt:
                        paragraphs = np.concatenate([clean_R2b(paragraph, version=0) for paragraph in paragraphs])
                    elif 'gender' in user_prompt:
                        paragraphs = np.concatenate([clean_R2b(paragraph, version=1) for paragraph in paragraphs])
                    else:
                        assert False

                if args.clean:
                    paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in paragraphs]

                embeddings = np.array([embedder.embed_paragraph(paragraph, version=3) for paragraph in paragraphs])
                pickle.dump(embeddings, open(e_loc, 'wb'))
        print("Finished identity axis {0} in {1:.4f} minutes".format(identity_axis, (time.time()-identity_time)/60))

human_responses = pickle.load(open(prefix_path+'human_responses/raw_responses.pkl', 'rb'))
if args.clean:
    e_loc = prefix_path+'human_responses/sbert_embeddings_clean.pkl'
else:
    e_loc = prefix_path+'human_responses/sbert_embeddings.pkl'
human_start = time.time()
if not os.path.exists(e_loc): ## so if it has already done this, it won't do it again
    human_embeddings = {}
    for key in human_responses.keys():
        who, user_prompt, identity = key.split('_')
        paragraphs = human_responses[key][0]
        if args.clean:
            paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in paragraphs]
        embeddings = np.array([embedder.embed_paragraph(paragraph, version=3) for paragraph in paragraphs])
        human_embeddings[key] = embeddings
    pickle.dump(human_embeddings, open(e_loc, 'wb'))
else:
    human_embeddings = pickle.load(open(e_loc, 'rb'))
print("Human embedding took {:.2f}".format((time.time()-human_start)/60))

sample_num = 1000
for model in args.models:
    nums_3_4 = [] # first number is reason, second number is analysis, so could also be nums_2a_1
    nums_t_2 = [] # t stands for three, 1-3
    nums_t_1 = [] # t stands for three, 1-3. this is analysis 1 on whether different prompts
    nums_t_3 = [] # t stands for three, 1-2. compares to the human
    model_name, folder = oip.model_info[model]

    if 'human' in model_name:
        if args.clean:
            e_loc = prefix_path+'human_responses/sbert_embeddings_clean.pkl'
        else:
            e_loc = prefix_path+'human_responses/sbert_embeddings.pkl'
    else:
        if args.clean:
            e_folder = prefix_path+'llm_responses/{}/sbert_embeddings_clean/'.format(folder)
        else:
            e_folder = prefix_path+'llm_responses/{}/sbert_embeddings/'.format(folder)

    model_configs = oip.configs[model_name]
    all_user_prompts = list(set(np.concatenate([model_configs[identity_axis] for identity_axis in model_configs.keys()])))
    all_user_prompts = np.sort(all_user_prompts)
    for user_prompt in all_user_prompts:
        id_ax = 0
        for identity_axis in model_configs.keys():

            if user_prompt not in model_configs[identity_axis]:
                continue

            ## Getting the paragraphs, MCs, and embeddings that will be used throughout
            for i, identity_name in enumerate(oip.identities[identity_axis]):
                if identity_axis == 'other':
                    continue
                if identity_name in ['a person with a permanent physical disability', 'a person who is blind or has low vision']:
                    continue
                
                identity = '{0}-{1}'.format(identity_axis, i)

                if 'human' not in model_name:
                    file_name = "{0}_{1}_{2}_{3}".format(model_name, user_prompt, identity, system_prompt)
                    loc = folder+'/'+file_name+'.pkl'
                    e_loc = e_folder+file_name+'.pkl'
                    llm_embeddings = pickle.load(open(e_loc, 'rb'))

                    # getting the actual text in addition to embeddings
                    paragraphs = [chunk[1] for chunk in get_texts([loc])]
                    if 'R2b' in user_prompt:
                        if 'race' in user_prompt:
                            paragraphs = np.concatenate([clean_R2b(paragraph, version=0) for paragraph in paragraphs])
                        elif 'gender' in user_prompt:
                            paragraphs = np.concatenate([clean_R2b(paragraph, version=1) for paragraph in paragraphs])
                        else:
                            assert False
                else:
                    if model_name == 'human-ingroup':
                        human_key = '{0}_{1}_{2}'.format('real', user_prompt, identity)
                    else:
                        human_key = '{0}_{1}_{2}'.format('portray', user_prompt, identity)
                    llm_embeddings = human_embeddings[human_key]
                    paragraphs = human_responses[human_key][0]

                if args.clean:
                    paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in paragraphs]

                if 'R3' not in user_prompt:
                    this_user_prompt = user_prompt
                    if user_prompt.split('-')[-1] in ['v1', 'v2', 'v3', 'v4']:
                        this_user_prompt = '-'.join(user_prompt.split('-')[:-1])
                    in_key = '{0}_{1}_{2}'.format('real', this_user_prompt, identity)
                    out_key = '{0}_{1}_{2}'.format('portray', this_user_prompt, identity) 
                    in_embeddings = human_embeddings[in_key]
                    out_embeddings = human_embeddings[out_key]
                    in_paragraphs, in_mcs = human_responses[in_key]
                    out_paragraphs, out_mcs = human_responses[out_key]
                    if args.clean:
                        in_paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in in_paragraphs]
                        out_paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in out_paragraphs]

                if ('R2b' in user_prompt) and ('gender' in user_prompt):
                    if 'human' not in model_name:
                        llm_mcs = np.array(pickle.load(open(prefix_path+'llm_responses/'+folder+'/mc/'+file_name+'.pkl', 'rb')))
                    else:
                        llm_mcs = human_responses[human_key][1]
                    # discretize the mcs which are sentiment analyze results
                    llm_mcs[llm_mcs==1] = 5
                    llm_mcs[llm_mcs<0] = 1
                    llm_mcs[llm_mcs<.25] = 2
                    llm_mcs[llm_mcs<.5] = 3
                    llm_mcs[llm_mcs<.75] = 4
                    llm_mcs[llm_mcs<1.] = 5
                else:
                    if 'human' in model_name:
                        llm_mcs = human_responses[human_key][1]
                    else:
                        llm_mcs = get_mcs(folder+'/mc/'+file_name+'.pkl')
                ## ANALYSIS 2 ##
                if id_ax == 0 and i == 0 and (('R2a' in user_prompt) or ("R1" in user_prompt)):
                    # the "generic" identity
                    if i == 0 and 'human' not in model_name: 
                        generic_file_name = "{0}_{1}_{2}_{3}".format(model_name, user_prompt, 'other-47', system_prompt)
                        generic_loc = folder+'/'+generic_file_name+'.pkl'
                        generic_e_loc = e_folder+generic_file_name+'.pkl'
                        generic_name_embeddings = pickle.load(open(generic_e_loc, 'rb'))
                        generic_name_mcs = get_mcs(folder+'/mc/'+generic_file_name+'.pkl')
                        generic_paragraphs = [chunk[1] for chunk in get_texts([generic_loc])]
                        if args.clean:
                            generic_paragraphs = [clean_all(paragraph, 'other-47', user_prompt) for paragraph in generic_paragraphs]
                        results = within_group_2(generic_name_embeddings, generic_paragraphs, generic_name_mcs)
                        nums_t_2.append([user_prompt, [identity_axis, 'Generic'], results[0], results[1], results[2], results[3]])

                if 'R3' not in user_prompt:
                    if 'R2b' in user_prompt:
                        for R2_ind in range(3):
                            indices = np.reshape(np.arange(len(llm_embeddings)), (-1, 3))[:, R2_ind]
                            these_llm_embeddings = np.array(llm_embeddings)[indices]
                            these_llm_mcs = np.array(llm_mcs)[indices] 
                            these_paragraphs = np.array(paragraphs)[indices]
                            results = within_group_2(these_llm_embeddings, these_paragraphs, these_llm_mcs)
                            nums_t_2.append([user_prompt+'_{}'.format(R2_ind), [identity_axis, identity_name], results[0], results[1], results[2], results[3]])
                    else:
                        results = within_group_2(llm_embeddings, paragraphs, llm_mcs)
                        nums_t_2.append([user_prompt, [identity_axis, identity_name], results[0], results[1], results[2], results[3]])
                    if identity_axis == 'intersection' and 'human' not in model_name:
                        if ('R1' in user_prompt) or ('R2a' in user_prompt):
                            for name_ind in [0, 1]:
                                file_name = "{0}_{1}_{2}-{4}_{3}".format(model_name, user_prompt, identity, system_prompt, name_ind)
                                loc = folder+'/'+file_name+'.pkl'
                                e_loc = e_folder+file_name+'.pkl'

                                name_embeddings = pickle.load(open(e_loc, 'rb'))
                                name_mcs = get_mcs(folder+'/mc/'+file_name+'.pkl')
                                name_paragraphs = [chunk[1] for chunk in get_texts([loc])]
                                if args.clean:
                                    name_paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in name_paragraphs]
                                results = within_group_2(name_embeddings, name_paragraphs, name_mcs)
                                nums_t_2.append([user_prompt, [identity_axis, "{0} name: {1}".format(identity_name, name_ind)], results[0], results[1], results[2], results[3]])

                ## ANALYSIS 1 ##

                # comparison between a group mentioned generically and the two names
                if identity_axis == 'intersection' and 'human' not in model_name:
                    if ('R1' in user_prompt) or ('R2a' in user_prompt):
                        name0_file_name = "{0}_{1}_{2}-{4}_{3}".format(model_name, user_prompt, identity, system_prompt, 0)
                        name0_loc = folder+'/'+name0_file_name+'.pkl'
                        name0_e_loc = e_folder+name0_file_name+'.pkl'
                        name0_llm_embeddings = pickle.load(open(name0_e_loc, 'rb'))
                        name0_llm_mcs = get_mcs(folder+'/mc/'+name0_file_name+'.pkl')

                        name1_file_name = "{0}_{1}_{2}-{4}_{3}".format(model_name, user_prompt, identity, system_prompt, 1)
                        name1_loc = folder+'/'+name1_file_name+'.pkl'
                        name1_e_loc = e_folder+name1_file_name+'.pkl'
                        name1_llm_embeddings = pickle.load(open(name1_e_loc, 'rb'))
                        name1_llm_mcs = get_mcs(folder+'/mc/'+name1_file_name+'.pkl')

                        results = different_1(llm_embeddings, llm_mcs, name0_llm_embeddings, name0_llm_mcs)
                        nums_t_1.append([user_prompt, [identity_axis + " (within comp-0)", identity_name, "{0} Name 0".format(identity_name)], results[0], results[1], results[2], results[3]])

                        results = different_1(llm_embeddings, llm_mcs, name1_llm_embeddings, name1_llm_mcs)
                        nums_t_1.append([user_prompt, [identity_axis + " (within comp-0)", identity_name, "{0} Name 1".format(identity_name)], results[0], results[1], results[2], results[3]])

                        results = different_1(name0_llm_embeddings, name0_llm_mcs, name1_llm_embeddings, name1_llm_mcs)
                        nums_t_1.append([user_prompt, [identity_axis + " (within comp-0)", "{0} Name 0".format(identity_name), "{0} Name 1".format(identity_name)], results[0], results[1], results[2], results[3]])

                if 'human-ingroup' in model_name:
                    human_key = '{0}_{1}_{2}'.format('portray', user_prompt, identity)
                    outgr_llm_embeddings = human_embeddings[human_key]
                    outgr_llm_mcs = human_responses[human_key][1]
                    outgr_paragraphs = human_responses[human_key][0]
                    if 'R2b' in user_prompt and 'gender' in user_prompt:
                        outgr_llm_mcs[outgr_llm_mcs==1] = 5
                        outgr_llm_mcs[outgr_llm_mcs<0] = 1
                        outgr_llm_mcs[outgr_llm_mcs<.25] = 2
                        outgr_llm_mcs[outgr_llm_mcs<.5] = 3
                        outgr_llm_mcs[outgr_llm_mcs<.75] = 4
                        outgr_llm_mcs[outgr_llm_mcs<1.] = 5

                    if 'R2b' in user_prompt:
                        for R2_ind in range(3):
                            indices = np.reshape(np.arange(len(llm_embeddings)), (-1, 3))[:, R2_ind]
                            these_llm_embeddings = np.array(llm_embeddings)[indices]
                            these_llm_mcs = np.array(llm_mcs)[indices] 

                            these_outgr_llm_embeddings = np.array(outgr_llm_embeddings)[indices]
                            these_outgr_llm_mcs = np.array(outgr_llm_mcs)[indices] 

                            results = different_1(these_llm_embeddings, these_llm_mcs, these_outgr_llm_embeddings, these_outgr_llm_mcs)
                            nums_t_1.append([user_prompt+'_{}'.format(R2_ind), [identity_axis + " (within comp-1)", "{0} In-group".format(identity_name), "{0} Out-group".format(identity_name)], results[0], results[1], results[2], results[3]])
                    else:
                        results = different_1(llm_embeddings, llm_mcs, outgr_llm_embeddings, outgr_llm_mcs)
                        nums_t_1.append([user_prompt, [identity_axis + " (within comp-1)", "{0} In-group".format(identity_name), "{0} Out-group".format(identity_name)], results[0], results[1], results[2], results[3]])


                for comp_i, comp_identity_name in enumerate(oip.identities[identity_axis]):
                    if 'R3' in user_prompt:
                        continue
                    if comp_identity_name in ['a person with a permanent physical disability', 'a person who is blind or has low vision']:
                        continue
                    if comp_i < i:
                        comp_identity = '{0}-{1}'.format(identity_axis, comp_i)
                        if 'human' not in model_name:
                            comp_file_name = "{0}_{1}_{2}_{3}".format(model_name, user_prompt, comp_identity, system_prompt)
                            comp_loc = folder+'/'+comp_file_name+'.pkl'
                            comp_e_loc = e_folder+comp_file_name+'.pkl'
                            comp_llm_embeddings = pickle.load(open(comp_e_loc, 'rb'))
                            # getting the actual text in addition to embeddings
                            comp_paragraphs = [chunk[1] for chunk in get_texts([comp_loc])]
                            if 'R2b' in user_prompt:
                                if 'race' in user_prompt:
                                    comp_paragraphs = np.concatenate([clean_R2b(paragraph, version=0) for paragraph in comp_paragraphs])
                                elif 'gender' in user_prompt:
                                    comp_paragraphs = np.concatenate([clean_R2b(paragraph, version=1) for paragraph in comp_paragraphs])
                                else:
                                    assert False
                        else:
                            if model_name == 'human-ingroup':
                                comp_human_key = '{0}_{1}_{2}'.format('real', user_prompt, comp_identity)
                            else:
                                comp_human_key = '{0}_{1}_{2}'.format('portray', user_prompt, comp_identity)
                            comp_llm_embeddings = human_embeddings[comp_human_key]
                            comp_paragraphs = human_responses[comp_human_key][0]

                        if args.clean:
                            comp_paragraphs = [clean_all(paragraph, identity, user_prompt) for paragraph in comp_paragraphs]

                        if ('R2b' in user_prompt) and ('gender' in user_prompt):
                            if 'human' not in model_name:
                                comp_llm_mcs = np.array(pickle.load(open(prefix_path+'llm_responses/'+folder+'/mc/'+comp_file_name+'.pkl', 'rb')))
                            else:
                                comp_llm_mcs = human_responses[comp_human_key][1]
                            comp_llm_mcs[comp_llm_mcs==1] = 5
                            comp_llm_mcs[comp_llm_mcs<0] = 1
                            comp_llm_mcs[comp_llm_mcs<.25] = 2
                            comp_llm_mcs[comp_llm_mcs<.5] = 3
                            comp_llm_mcs[comp_llm_mcs<.75] = 4
                            comp_llm_mcs[comp_llm_mcs<1.] = 5
                        else:
                            if 'human' not in model_name:
                                comp_llm_mcs = get_mcs(folder+'/mc/'+comp_file_name+'.pkl')
                            else:
                                comp_llm_mcs = human_responses[comp_human_key][1]


                        if 'R2b' in user_prompt:
                            for R2_ind in range(3):
                                indices = np.reshape(np.arange(len(llm_embeddings)), (-1, 3))[:, R2_ind]
                                these_llm_embeddings = np.array(llm_embeddings)[indices]
                                these_llm_mcs = np.array(llm_mcs)[indices] 

                                these_comp_llm_embeddings = np.array(comp_llm_embeddings)[indices]
                                these_comp_llm_mcs = np.array(comp_llm_mcs)[indices] 

                                results = different_1(these_llm_embeddings, these_llm_mcs, these_comp_llm_embeddings, these_comp_llm_mcs)
                                nums_t_1.append([user_prompt+'_{}'.format(R2_ind), [identity_axis, identity_name, comp_identity_name], results[0], results[1], results[2], results[3]])
                        else:
                            results = different_1(llm_embeddings, llm_mcs, comp_llm_embeddings, comp_llm_mcs)
                            nums_t_1.append([user_prompt, [identity_axis, identity_name, comp_identity_name], results[0], results[1], results[2], results[3]])

                        if identity_axis == 'intersection' and 'human' not in model_name:
                            if ('R1' in user_prompt) or ('R2a' in user_prompt):
                                for name_ind in [0, 1]:
                                    name_file_name = "{0}_{1}_{2}-{4}_{3}".format(model_name, user_prompt, identity, system_prompt, name_ind)
                                    name_loc = folder+'/'+name_file_name+'.pkl'
                                    name_e_loc = e_folder+name_file_name+'.pkl'

                                    name0_llm_embeddings = pickle.load(open(name_e_loc, 'rb'))
                                    name0_llm_mcs = get_mcs(folder+'/mc/'+name_file_name+'.pkl')
                                    comp_file_name = "{0}_{1}_{2}-{4}_{3}".format(model_name, user_prompt, comp_identity, system_prompt, name_ind)
                                    comp_loc = folder+'/'+comp_file_name+'.pkl'
                                    comp_e_loc = e_folder+comp_file_name+'.pkl'
                                    comp1_llm_embeddings = pickle.load(open(comp_e_loc, 'rb'))
                                    comp1_llm_mcs = get_mcs(folder+'/mc/'+comp_file_name+'.pkl')
                                    results = different_1(name0_llm_embeddings, name0_llm_mcs, comp1_llm_embeddings, comp1_llm_mcs)
                                    nums_t_1.append([user_prompt, [identity_axis + " name", "{0} name: {1}".format(identity_name, name_ind), "{0} name: {1}".format(comp_identity_name, name_ind)], results[0], results[1], results[2], results[3]])

                ## ANALYSIS 3 ##
                if 'R1' in user_prompt or 'R2' in user_prompt:
                    if 'human' in model_name:
                        continue

                    if 'R2b' in user_prompt:
                        for R2_ind in range(3):
                            indices = np.reshape(np.arange(len(llm_embeddings)), (-1, 3))[:, R2_ind]

                            these_llm_embeddings = np.array(llm_embeddings)[indices]
                            these_llm_mcs = np.array(llm_mcs)[indices] 
                            these_llm_paragraphs = np.array(paragraphs)[indices]
                            
                            these_in_embeddings = np.array(in_embeddings)[indices]
                            these_in_mcs = np.array(in_mcs)[indices] 
                            these_in_paragraphs = np.array(in_paragraphs)[indices]

                            these_out_embeddings = np.array(out_embeddings)[indices]
                            these_out_mcs = np.array(out_mcs)[indices] 
                            these_out_paragraphs = np.array(out_paragraphs)[indices]

                            results = analyze_distance_3(these_llm_embeddings, these_in_embeddings, these_out_embeddings, these_llm_mcs, these_in_mcs, these_out_mcs, these_llm_paragraphs, these_in_paragraphs, these_out_paragraphs)
                            nums_t_3.append([user_prompt+'_{}'.format(R2_ind), [identity_axis, identity_name], results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[8], results[9], results[10], results[11]])
                    else:
                        results = analyze_distance_3(llm_embeddings, in_embeddings, out_embeddings, llm_mcs, in_mcs, out_mcs, paragraphs, in_paragraphs, out_paragraphs)
                        nums_t_3.append([user_prompt, [identity_axis, identity_name], results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[8], results[9], results[10], results[11]])

                    if identity_axis == 'intersection':
                        if ('R1' in user_prompt) or ('R2a' in user_prompt):
                            for name_ind in [0, 1]:
                                file_name = "{0}_{1}_{2}-{4}_{3}".format(model_name, user_prompt, identity, system_prompt, name_ind)
                                loc = folder+'/'+file_name+'.pkl'
                                e_loc = e_folder+file_name+'.pkl'

                                name_embeddings = pickle.load(open(e_loc, 'rb'))
                                name_mcs = get_mcs(folder+'/mc/'+file_name+'.pkl')
                                name_paragraphs = [chunk[1] for chunk in get_texts([loc])]
                                results = analyze_distance_3(name_embeddings, in_embeddings, out_embeddings, name_mcs, in_mcs, out_mcs, name_paragraphs, in_paragraphs, out_paragraphs)
                                nums_t_3.append([user_prompt, [identity_axis, "{0} name: {1}".format(identity_name, name_ind)], results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[8], results[9], results[10], results[11]])
                

            ### (3) Number of distinct clusters 
            def make_range_array(all_results, first_4):
                end_chunk = ['{0}-{1}'.format(round(np.amin(all_results[:, 0]), precision_val), round(np.amax(all_results[:, 0]), precision_val)), '{0}-{1}'.format(np.format_float_scientific(np.amin(all_results[:, 1]), precision=precision_val), np.format_float_scientific(np.amax(all_results[:, 1]), precision=precision_val)), '{0}-{1}'.format(int(np.amin(all_results[:, 2])), int(np.amax(all_results[:, 2])))]
                return first_4 + end_chunk
                
            ## ANALYSIS 4 ##
            if 'R3' in user_prompt:
                precision_val = 2
                n = 1000
                if identity_axis == 'other': # do like 3 of them at once right now
                    other_mapping = {0: 'Myers-Briggs', 1: 'Random personas', 2: 'Political', 3: 'Astrology', 4: 'Generic'}
                    categories, identity_names = oip.generate_identities_other()
                    for cat in range(4):
                        possible_identities = np.where(categories==cat)[0]
                        all_results = []
                        for it in range(n):
                            results = diversity_analysis_4(identity_axis, model_name, user_prompt, system_prompt, np.random.choice(possible_identities, size=3, replace=False), boot_result=False, to_print=False)
                            all_results.append(results)
                        all_results = np.array(all_results)
                        nums_3_4.append([user_prompt, other_mapping[cat], all_results[:, 0], all_results[:, 1], all_results[:, 2]])

                    results = diversity_analysis_4(identity_axis, model_name, user_prompt, system_prompt, np.where(categories==4)[0], boot_result=True) # the single generic one
                    nums_3_4.append([user_prompt, 'Generic', results[0], results[1], results[2]])
                elif identity_axis == 'intersection':
                    all_results = []
                    for it in range(n):
                        results = diversity_analysis_4(identity_axis, model_name, user_prompt, system_prompt, np.random.choice(np.arange(len(oip.identities[identity_axis])), size=3, replace=False), boot_result=False)
                        all_results.append(results)
                    all_results = np.array(all_results)
                    nums_3_4.append([user_prompt, 'Intersection', all_results[:, 0], all_results[:, 1], all_results[:, 2]])
                else:
                    if identity_axis == 'disability':
                        three_identities = [0, 1, 4]
                    else:
                        three_identities = np.arange(3)
                    results = diversity_analysis_4(identity_axis, model_name, user_prompt, system_prompt, three_identities, boot_result=True)
                    nums_3_4.append([user_prompt, identity_axis.capitalize(), results[0], results[1], results[2]])
            id_ax += 1

    if 'human' not in model_name:
        all_model_nums['{0}-{1}'.format(model_name, 'nums_3_4')] = nums_3_4
        all_model_nums['{0}-{1}'.format(model_name, 'nums_t_3')] = nums_t_3
    all_model_nums['{0}-{1}'.format(model_name, 'nums_t_2')] = nums_t_2
    all_model_nums['{0}-{1}'.format(model_name, 'nums_t_1')] = nums_t_1

pickle.dump(all_model_nums, open('analysis_results/{}_data.pkl'.format(args.save_loc), 'wb'))
end_time = time.time()
print("Took {:.3f} minutes".format((end_time-start_time)/60))


