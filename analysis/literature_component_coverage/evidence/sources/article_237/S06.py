import pickle
import matplotlib.pyplot as plt
import numpy as np
import llm_prompts as oip
import re
import scipy.stats as st

COLOR = 'cb'
if COLOR == 'cb':
    plt.style.use('tableau-colorblind10')

file = 'all'
all_model_nums = pickle.load(open('analysis_results/{}_data.pkl'.format(file), 'rb'))

IDEN_ORDER = ['a Black man', 'a Black woman', 'a White man', 'a White woman', 'a Black person', 'an Asian person', 'a White person', 'a man', 'a woman', 'a non-binary person', 'a Baby Boomer', 'a Millennial', 'a member of Generation Z', 'a person without disabilities', 'a person with ADD or ADHD', 'a person with impaired vision']
IDEN_ORDER.reverse()

# for shortening identity name for graphs
def remove_a(remove_name):
    mid_name = re.sub('a ', '', re.sub('an A', 'A', remove_name))
    return re.sub('member of ', '', re.sub('with', 'w/', re.sub('without', 'w/o', mid_name)))

subplot_mapping = {0: 0, 1: 1, 2: 2, 3: 3}
models = ['WV-Uncensored-7b', 'Llama-2-7b', 'GPT-3.5-Turbo', 'GPT-4']
num_metrics = 4
fig, axes = plt.subplots(len(models), num_metrics, figsize=(12, 14))
xlims = [[5, 0] for _ in range(len(subplot_mapping))]
for key in all_model_nums.keys():
    if 'human' in key:
        continue
    all_vals = {} # identity to size 4 x n array of all metric values
    hum_vals = {}
    if 'nums_t_2' in key:
        print("key: {}".format(key))

        nums_t_2 = all_model_nums[key]
        identity_axes = ['intersection', 'race', 'gender', 'age', 'disability']
        row_axes = list(set([row[0].replace('-v3', '').replace('-v4', '').split('-')[0] for row in nums_t_2]))
        row_axes = list(np.sort(row_axes))

        num_metrics = 4
        axes_identity_names = {}

        all_nums_t_2 = [nums_t_2]
        if 'human' not in key:
            # overlay the human comparison
            humanin_nums_t_2 = all_model_nums['human-ingroup-nums_t_2']
            humanout_nums_t_2 = all_model_nums['human-outgroup-nums_t_2']
            all_nums_t_2.append(humanin_nums_t_2)

        for h_ind, this_nums_t_2 in enumerate(all_nums_t_2):
            for row in this_nums_t_2:
                iden_ind = identity_axes.index(row[1][0])

                if 'name' in row[1][1]: # does not graph the intersectional names part
                    continue
                if row[1][1] == 'Generic':
                    next_ind = 0
                    iden_ind = 0
                else:
                    if 'name' in row[1][1]:
                        next_ind = 4
                        identity_name = row[1][1].split(' name')[0]
                        idx = int(row[1][1][-1])
                        next_ind += (oip.identities[row[1][0]].index(identity_name)*2) + idx
                    else:
                        next_ind = oip.identities[row[1][0]].index(row[1][1])
                    if iden_ind == 0:
                        next_ind += 1

                    if iden_ind == 4:
                        if next_ind == 4:
                            next_ind = 2

                if h_ind == 0:
                    offset = 0
                    if COLOR == 'cb':
                        if iden_ind == 2:
                            c = 'C{}'.format(4)
                        elif iden_ind == 3:
                            c = 'C{}'.format(5)
                        elif iden_ind == 4:
                            c = 'C{}'.format(7)
                        elif iden_ind == 5:
                            c = 'C{}'.format(8)
                        elif iden_ind in [0, 1]:
                            c = 'C{}'.format(iden_ind)

                        if row[1][1] == 'Generic':
                            c = 'C{}'.format(8)
                    else:
                        c = 'C{}'.format(iden_ind)
                        if row[1][1] == 'Generic':
                            c = 'C{}'.format(5)
                elif h_ind == 1:
                    if COLOR == 'cb':
                        c = 'C3'
                    else:
                        c = 'k'
                    offset = .1
                elif h_ind == 2:
                    if COLOR == 'cb':
                        c = 'C2'
                    else:
                        c = 'tab:gray'
                    offset = .2

                ind = 0
                if iden_ind > 0:
                    ind += (5)
                    iden_ind -= 1
                ind = ind + (iden_ind*3) + next_ind
                ind = 16 - ind

                this_name = row[1][1]
                if '(' in this_name:
                    this_name = this_name[:this_name.index('(')].strip()

                spacing = 0

                if next_ind == 0:
                    if row[1][1] == 'Generic':
                        axes_identity_names[ind] = this_name
                    else:
                        if row[1][0] == 'race':
                            spacing = 27
                        elif row[1][0] == 'gender':
                            spacing = 40
                        elif row[1][0] == 'age':
                            spacing = 26
                        elif row[1][0] == 'disability':
                            spacing = 12
                        axes_identity_names[ind] = '{0}: {2}{1}'.format(row[1][0].capitalize(), this_name, ' '*spacing)
                else:
                    if row[1][1] == 'a Black man':
                        spacing = 30
                        axes_identity_names[ind] = 'Intersection: ' + ' '*spacing + this_name
                    else:
                        axes_identity_names[ind] = this_name

                for met in np.arange(num_metrics):
                    col = subplot_mapping[met]
                    if (type(row[2+met]) == np.ndarray) or type(row[2+met]) == list:
                        if len(row[2+met]) == 1000:
                            all_values = np.sort(row[2+met])
                            lower, actual, higher = all_values[25], np.median(all_values), all_values[974]
                            assert False
                        else:
                            assert len(row[2+met]) == 5
                            lower, low83, actual, high83, higher = row[2+met]
                        if h_ind == 0:
                            if ind not in all_vals.keys():
                                all_vals[ind] = [[] for _ in range(4)]
                            all_vals[ind][met].append(actual)
                        elif h_ind == 1:
                            if ind not in hum_vals.keys():
                                hum_vals[ind] = [[] for _ in range(4)]
                            hum_vals[ind][met].append(actual)
                    else:
                        assert False
        if 'wizard' in key:
            plt_num = 0
        elif 'llama' in key:
            plt_num = 1
        elif 'gpt-3.5' in key:
            plt_num = 2
        elif 'gpt-4' in key:
            plt_num = 3
        for ind in all_vals.keys():
            for met in range(4):
                if COLOR == 'cb':
                    if ind in [0, 1, 2]:
                        c = 'C0'
                    elif ind in [3, 4, 5]:
                        c = 'C1'
                    elif ind in [6, 7, 8]:
                        c = 'C4'
                    elif ind in [9, 10, 11]:
                        c = 'C5'
                    elif ind in [12, 13, 14, 15]:
                        c = 'C7'
                    elif ind in [16]:
                        c = 'C8'

                arr = all_vals[ind][met]
                ci = st.bootstrap((arr,), np.mean).confidence_interval
                width = 4
                axes[plt_num][met].errorbar([np.mean(arr)], [ind], xerr=[[np.mean(arr)-ci[0]], [ci[1]-np.mean(arr)]], capsize=width, ms=10, marker='.', c=c, linewidth=2, elinewidth=2, capthick=2)
                xlims[met][0] = np.nanmin([xlims[met][0], ci[0]])
                xlims[met][1] = np.nanmax([xlims[met][1], ci[1]])
                if ind in hum_vals.keys():
                    arr = hum_vals[ind][met]
                    ci = st.bootstrap((arr,), np.mean).confidence_interval
                    axes[plt_num][met].errorbar([np.mean(arr)], [ind], xerr=[[np.mean(arr)-ci[0]], [ci[1]-np.mean(arr)]], capsize=width, ms=7, marker='x', c='C3', linewidth=2, elinewidth=2, capthick=2, mew=2)
                    xlims[met][0] = np.nanmin([xlims[met][0], ci[0]])
                    xlims[met][1] = np.nanmax([xlims[met][1], ci[1]])
        fontsize=14
        yticks = np.arange(len(axes_identity_names))
        j_range = yticks
        make_smaller_right = True # gets rid of intersection name on right side

        yticklabels = []
        for j in j_range:
            if 'Generic' == axes_identity_names[j]:
                yticklabels.append(remove_a(axes_identity_names[j]))
            else:
                this_name = axes_identity_names[j]
                if ':' in this_name:
                    this_name = this_name.split(':')[1]
                    this_name = this_name[this_name.index('a'):]
                extra_pad = ''
                yticklabels.append(extra_pad+remove_a(axes_identity_names[j]).replace('intersection', 'intersectional'))
        axes[plt_num][0].set_yticks(yticks)
        axes[plt_num][0].set_yticklabels(yticklabels, fontsize=fontsize)

for mod in range(len(models)):
    axes[mod][0].set_ylabel(models[mod], fontsize=fontsize)
    #axes[mod][3].yaxis.tick_right()
    for j in range(len(axes[0])):
        #axes[i][j].plot([0]*(len(yticks)), yticks, c='k', linestyle='dashed')
        if j != 0:
            axes[mod][j].set_yticks(yticks)
            axes[mod][j].set_yticklabels(['' for _ in range(len(yticks))], fontsize=fontsize)
        axes[mod][j].set_ylim(bottom=np.amin(yticks)-.5, top=np.amax(yticks)+.5)
        #axes[mod][j].set_xlim(left=(xlims[j][0]*1.05 if xlims[j][0]<0 else xlims[j][0]*.85), right=xlims[j][1]*1.05)
        axes[mod][j].tick_params(axis='x', labelsize=fontsize)


axes[0][subplot_mapping[0]].set_title('Ngram: Unique', fontsize=fontsize)
axes[0][subplot_mapping[1]].set_title('SBERT: Cosine', fontsize=fontsize)
axes[0][subplot_mapping[2]].set_title('SBERT: Cov Trace', fontsize=fontsize)
axes[0][subplot_mapping[3]].set_title('MC: Unique', fontsize=fontsize)
#fig.align_ylabels(axes[:, 0])

plt.tight_layout()
plt.savefig('analysis_results/summary_flatten.png', dpi=300)
plt.close()
