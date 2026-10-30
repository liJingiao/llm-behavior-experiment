import pickle
import matplotlib.pyplot as plt
import numpy as np
import llm_prompts as oip
from scipy.stats import ttest_ind
from matplotlib import rc,rcParams
import copy
import re
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

for key in all_model_nums.keys():
    print("key: {}".format(key))
    if 'nums_t_1' in key:
        nums_t_1 = all_model_nums[key]
        identity_axes = ['intersection', 'race', 'gender', 'age', 'disability']
        identity_axes.reverse()

        row_axes = list(set([row[0].split('-')[0] for row in nums_t_1]))
        row_axes = list(np.sort(row_axes))

        pair_ordering = {
                'race': ['0-1', '0-2', '1-2'],
                'gender': ['0-1', '0-2', '1-2'],
                'age': ['0-1', '0-2', '1-2'],
                'disability': ['0-1', '0-4', '1-4'],
                'intersection': ['0-1', '0-2', '0-3', '1-2', '1-3', '2-3'],
                }

        fig, axes = plt.subplots(len(row_axes), 2, figsize=(12, 14), gridspec_kw={'height_ratios': [3, 3, 1]})
        fontsize=14
        xlims = [[0, 0] for _ in range(2)]

        all_nums_t_1 = [nums_t_1]
        if 'human' not in key:
            # overlay the human comparison
            humanin_nums_t_1 = all_model_nums['human-ingroup-nums_t_1']
            humanout_nums_t_1 = all_model_nums['human-outgroup-nums_t_1']
            all_nums_t_1.append(humanin_nums_t_1)
            all_nums_t_1.append(humanout_nums_t_1)

        counts = {}

        for h_ind, this_nums_t_1 in enumerate(all_nums_t_1):
            for row in this_nums_t_1:
                identity_axis, identity_name, comp_identity_name = row[1]
                if 'within comp' in identity_axis:
                    continue
                plot_num = row_axes.index(row[0].split('-')[0])
                iden_ind = identity_axes.index(identity_axis)
                ind1, ind2 = oip.identities[identity_axis].index(identity_name), oip.identities[identity_axis].index(comp_identity_name)
                id_key = '{0}-{1}'.format(ind1, ind2)
                if id_key not in pair_ordering[identity_axis]:
                    id_key = '{0}-{1}'.format(ind2, ind1)
                    assert id_key in pair_ordering[identity_axis]
                ind = (iden_ind*3) + pair_ordering[identity_axis].index(id_key)

                if h_ind == 0:
                    counts_key = '{0}-{1}'.format(plot_num, ind)
                    if counts_key not in counts:
                        counts[counts_key] = 0
                    if row[3] < .05 and row[2] > 0:
                        counts[counts_key] += 1
                    if row[5] < .05 and row[4] > 0:
                        counts[counts_key] += 1
                
                if h_ind == 0:
                    c = 'C{}'.format(iden_ind)
                elif h_ind == 1:
                    c = 'k'
                elif h_ind == 2:
                    c = 'tab:gray'

                axes[plot_num][0].scatter(row[2], ind, c=c, s=20, marker='x' if row[3] >= .05 else 'o')
                axes[plot_num][1].scatter(row[4], ind, c=c, s=20, marker='x' if row[5] >= .05 else 'o')

                xlims[0][0] = np.amin([xlims[0][0], row[2]])
                xlims[0][1] = np.amax([xlims[0][1], row[2]])
                xlims[1][0] = np.amin([xlims[1][0], row[4]])
                xlims[1][1] = np.amax([xlims[1][1], row[4]])

        ind_counter = 0
        yticks = []
        for axis_ind, axis in enumerate(identity_axes):
            for ident_ind, ident in enumerate(pair_ordering[axis]):
                ind1, ind2 = ident.split('-')
                name1, name2 = oip.identities[axis][int(ind1)], oip.identities[axis][int(ind2)]
                if '(' in name1:
                    name1 = name1[:name1.index('(')].strip()
                if '(' in name2:
                    name2 = name2[:name2.index('(')].strip()

                format_names = '{0} - {1}'.format(remove_a(name1), remove_a(name2))
                yticks.append(format_names)

        for i in range(len(row_axes)):
            extra_pad = ''
            if i == 2:
                j_range = [6, 7, 8, 9, 10, 11]
            else:
                j_range = np.arange(len(yticks))
            if i == 0:
                denom = 2
            elif i == 1:
                denom = 4
            elif i == 2:
                denom = 6
                extra_pad = '     '


            yticks_labels = [(extra_pad+yticks[j]+': '+str(counts['{0}-{1}'.format(i, j)])+'/'+str(denom)) for j in j_range]
            axes[i][0].set_yticks(j_range)
            axes[i][1].set_yticks(j_range)
            axes[i][0].set_yticklabels(yticks_labels, fontsize=fontsize)
            axes[i][0].set_ylim(bottom=np.amin(j_range)-.5, top=np.amax(j_range)+.5)
            axes[i][1].set_ylim(bottom=np.amin(j_range)-.5, top=np.amax(j_range)+.5)

            axes[i][0].set_ylabel(row_axes[i].replace('R1', 'R1-Contingent').replace('R2a', 'R2-Relevant').replace('R2b', 'R3-Subj'), fontsize=fontsize)
            axes[i][1].set_yticks([])

            for j in range(2):
                axes[i][j].set_xlim(left=(xlims[j][0]*1.05 if xlims[j][0]<0 else xlims[j][0]*.95), right=xlims[j][1]*1.05)
                axes[i][j].tick_params(axis='x', labelsize=fontsize)

        axes[0][0].set_title('SBERT: Cosine', fontsize=fontsize)
        axes[0][1].set_title('MC: Chi-Squared', fontsize=fontsize)
   
        axes[0][0].scatter([], [], c='k', label='In-Group')
        axes[0][0].scatter([], [], c='tab:gray', label='Out-Group')
                
        for i in range(len(row_axes)):
            for lab in axes[i][0].get_yticklabels():
                labtext = lab.get_text()
                if '/' in labtext:
                    num, den = labtext.split(':')[-1].split('/')
                    if float(num)/float(den) > .5:
                        lab.set_fontweight('bold')


        fig.align_ylabels(axes[:, 0])
        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}.png'.format(file, key), dpi=300)
        plt.close()

        fig, axes = plt.subplots(3, 2, figsize=(12, 14))
        xlims = [[0, 0] for _ in range(2)]

        all_nums_t_1 = [nums_t_1]
        if 'human' not in key:
            # overlay the human comparison
            humanin_nums_t_1 = all_model_nums['human-ingroup-nums_t_1']
            humanout_nums_t_1 = all_model_nums['human-outgroup-nums_t_1']
            all_nums_t_1.append(humanin_nums_t_1)
            all_nums_t_1.append(humanout_nums_t_1)

        counts = {}

        for h_ind, this_nums_t_1 in enumerate(all_nums_t_1):
            for row in this_nums_t_1:
                identity_axis, identity_name, comp_identity_name = row[1]
                if 'within comp' in identity_axis:
                    continue
                plot_num = row_axes.index(row[0].split('-')[0])
                iden_ind = identity_axes.index(identity_axis)
                ind1, ind2 = oip.identities[identity_axis].index(identity_name), oip.identities[identity_axis].index(comp_identity_name)
                id_key = '{0}-{1}'.format(ind1, ind2)
                if id_key not in pair_ordering[identity_axis]:
                    id_key = '{0}-{1}'.format(ind2, ind1)
                    assert id_key in pair_ordering[identity_axis]
                ind = (iden_ind*3) + pair_ordering[identity_axis].index(id_key)

                if h_ind == 0:
                    counts_key = '{0}-{1}'.format(plot_num, ind)
                    if counts_key not in counts:
                        counts[counts_key] = 0
                    if row[3] < .05 and row[2] > 0:
                        counts[counts_key] += 1
                    if row[5] < .05 and row[4] > 0:
                        counts[counts_key] += 1
                
                if h_ind == 0:
                    c = 'C{}'.format(iden_ind)
                elif h_ind == 1:
                    c = 'k'
                elif h_ind == 2:
                    c = 'tab:gray'

                axes[plot_num][0].scatter(row[2], ind, c=c, s=20, marker='x' if row[3] >= .05 else 'o')
                axes[plot_num][1].scatter(row[4], ind, c=c, s=20, marker='x' if row[5] >= .05 else 'o')

                xlims[0][0] = np.amin([xlims[0][0], row[2]])
                xlims[0][1] = np.amax([xlims[0][1], row[2]])
                xlims[1][0] = np.amin([xlims[1][0], row[4]])
                xlims[1][1] = np.amax([xlims[1][1], row[4]])

        ind_counter = 0
        yticks = []
        for axis_ind, axis in enumerate(identity_axes):
            for ident_ind, ident in enumerate(pair_ordering[axis]):
                ind1, ind2 = ident.split('-')
                name1, name2 = oip.identities[axis][int(ind1)], oip.identities[axis][int(ind2)]
                if '(' in name1:
                    name1 = name1[:name1.index('(')].strip()
                if '(' in name2:
                    name2 = name2[:name2.index('(')].strip()

                format_names = '{0} - {1}'.format(name1, name2)
                yticks.append(format_names)

        for i in range(len(row_axes)):
            if i == 2:
                j_range = [6, 7, 8, 9, 10, 11]
            else:
                j_range = np.arange(len(yticks))
            if i == 0:
                denom = 2
            elif i == 1:
                denom = 4
            elif i == 2:
                denom = 6

            yticks_labels = [(yticks[j]+': '+str(counts['{0}-{1}'.format(i, j)])+'/'+str(denom)) for j in j_range]
            axes[i][0].set_yticks(j_range)
            axes[i][1].set_yticks(j_range)
            axes[i][0].set_yticklabels(yticks_labels)
            axes[i][0].set_ylim(bottom=np.amin(j_range)-.5, top=np.amax(j_range)+.5)
            axes[i][1].set_ylim(bottom=np.amin(j_range)-.5, top=np.amax(j_range)+.5)

            axes[i][0].set_ylabel(row_axes[i])
            axes[i][1].set_yticks([])

            for j in range(2):
                axes[i][j].set_xlim(left=(xlims[j][0]*1.05 if xlims[j][0]<0 else xlims[j][0]*.95), right=xlims[j][1]*1.05)

        axes[0][0].set_title('FR: t-statistic')
        axes[0][1].set_title('MC: chi-squared')
   
        axes[0][0].scatter([], [], c='tab:gray', label='Out')
        axes[0][0].scatter([], [], c='k', label='In')
        axes[0][0].legend()
                
        for i in range(len(row_axes)):
            for lab in axes[i][0].get_yticklabels():
                labtext = lab.get_text()
                if '/' in labtext:
                    num, den = labtext.split(':')[-1].split('/')
                    if float(num)/float(den) > .5:
                        lab.set_fontweight('bold')


        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}_intersectname.png'.format(file, key), dpi=300)
        plt.close()

        row_axes = ['R1--full', 'R2a-gunregulation-full', 'R2a-healthcare-full']
        row_axes = list(np.sort(row_axes))
        fig, axes = plt.subplots(len(row_axes), 2, figsize=(8, 10))
        ind = -1
        names = {}
        identity_names = ['a Black man', 'a Black woman', 'a White man', 'a White woman']
        for row in nums_t_1:
            identity_axis, identity_name, comp_identity_name = row[1]
            if 'within comp-0' not in identity_axis:
                continue
            plot_num = row_axes.index(row[0])

            for iden in identity_names:
                if iden in identity_name:
                    break
            name = "{0}: {1}-{2}".format(iden, identity_name[len(iden):].strip(), comp_identity_name[len(iden):].strip())
            if name not in names:
                ind += 1
                names[name] = ind
            ind = names[name]
            axes[plot_num][0].scatter(row[2], ind, c="C{}".format(identity_names.index(iden)), s=20, marker='x' if row[3] >= .05 else 'o')
            axes[plot_num][1].scatter(row[4], ind, c="C{}".format(identity_names.index(iden)), s=20, marker='x' if row[5] >= .05 else 'o')
        axes[0][0].set_title('FR: t-statistic')
        axes[0][1].set_title('MC: chi-squared')
        for i in range(len(row_axes)):
            axes[i][0].set_yticks(np.arange(len(names)))
            axes[i][1].set_yticks(np.arange(len(names)))
            axes[i][0].set_yticklabels(names)
            axes[i][0].set_ylabel(row_axes[i])
    
        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}_withincomp-0.png'.format(file, key), dpi=300)
        plt.close()

        if 'human-ingroup' in key:
            row_axes = list(set([row[0].split('-')[0] for row in nums_t_1]))
            row_axes = list(np.sort(row_axes))
            fig, axes = plt.subplots(len(row_axes), 2, figsize=(8, 10), gridspec_kw={'height_ratios': [6.6, 6.6, 2.2]})
            fontsize=14
            count = {}
            for row in nums_t_1:
                identity_axis, identity_name, comp_identity_name = row[1]
                if 'within comp-1' not in identity_axis:
                    continue
                plot_num = row_axes.index(row[0].split('-')[0])

                name = identity_name[:identity_name.index(' In-group')]
                if '(' in name:
                    name = name[:name.index('(')].strip()
                ind = IDEN_ORDER.index(name)

                count_key = '{0}-{1}'.format(plot_num, ind)
                if count_key not in count:
                    count[count_key] = 0
                axes[plot_num][0].scatter(row[2], ind, c="C{}".format(identity_axes.index(identity_axis.split(' ')[0])), s=20, marker='x' if row[3] >= .05 else 'o')
                axes[plot_num][1].scatter(row[4], ind, c="C{}".format(identity_axes.index(identity_axis.split(' ')[0])), s=20, marker='x' if row[5] >= .05 else 'o')
                
                if row[3] < .05 and row[2] > 0:
                    count[count_key] += 1
                if row[5] < .05 and row[4] > 0:
                    count[count_key] += 1

            axes[0][0].set_title('SBERT: Cosine', fontsize=fontsize)
            axes[0][1].set_title('MC: Chi-Squared', fontsize=fontsize)
            for i in range(len(row_axes)):
                extra_pad = ''
                if i in [0, 1]:
                    j_range = np.arange(len(IDEN_ORDER))
                    denom = 2
                    if i == 1:
                        denom = 4
                elif i == 2:
                    j_range = [6, 7, 8, 9, 10, 11]
                    denom = 6
                    extra_pad = '     '
                elif i == 3:
                    j_range = [9, 10, 11]
                    denom = 6
                axes[i][0].set_ylim(bottom=np.amin(j_range)-.5, top=np.amax(j_range)+.5)
                axes[i][1].set_ylim(bottom=np.amin(j_range)-.5, top=np.amax(j_range)+.5)
                axes[i][0].set_yticks(j_range)
                axes[i][1].set_yticks(j_range)
                axes[i][0].set_yticklabels(["{0}: {1}/{2}".format(extra_pad+remove_a(IDEN_ORDER[j]), count['{0}-{1}'.format(i, j)], denom) for j in j_range], fontsize=fontsize)
                axes[i][0].set_ylabel(row_axes[i].replace('R1', 'R1-Contingent').replace('R2a', 'R2-Relevant').replace('R2b', 'R3-Subj'), fontsize=fontsize)
                axes[i][1].set_yticks([])

                axes[i][0].tick_params(axis='x', labelsize=fontsize)
                axes[i][1].tick_params(axis='x', labelsize=fontsize)
        
                for lab in axes[i][0].get_yticklabels():
                    labtext = lab.get_text()
                    if '/' in labtext:
                        num, den = labtext.split(':')[-1].split('/')
                        if float(num)/float(den) > .5:
                            lab.set_fontweight('bold')
            fig.align_ylabels(axes[:, 0])
            plt.tight_layout()
            plt.savefig('analysis_results/{0}_fig_{1}_withincomp-1.png'.format(file, key), dpi=300)
            plt.close()

    if 'nums_t_2' in key:
        subplot_mapping = {0: 0, 1: 1, 2: 2, 3: 3}
        nums_t_2 = all_model_nums[key]
        identity_axes = ['intersection', 'race', 'gender', 'age', 'disability']
        row_axes = list(set([row[0].replace('-v3', '').replace('-v4', '').split('-')[0] for row in nums_t_2]))
        row_axes = list(np.sort(row_axes))

        num_metrics = 4
        if 'temp_1o' in file:
            fig, axes = plt.subplots(len(row_axes), num_metrics, figsize=(18, 5))
        else:
            fig, axes = plt.subplots(len(row_axes), num_metrics, figsize=(15, 9), gridspec_kw={'height_ratios': [6.6, 6.6, 2.2]})
        axes_identity_names = {}

        all_nums_t_2 = [nums_t_2]
        if 'human' not in key:
            # overlay the human comparison
            humanin_nums_t_2 = all_model_nums['human-ingroup-nums_t_2']
            humanout_nums_t_2 = all_model_nums['human-outgroup-nums_t_2']
            all_nums_t_2.append(humanin_nums_t_2)

        xlims = [[5, 0] for _ in range(len(subplot_mapping))]
        within_question_axis_lowest = {}
        for h_ind, this_nums_t_2 in enumerate(all_nums_t_2):
            for row in this_nums_t_2:
                try:
                    plot_num = row_axes.index(row[0].replace('-v3', '').replace('-v4', '').split('-')[0])
                except:
                    if 'temp_1o' in file:
                        continue
                    else:
                        assert False
                iden_ind = identity_axes.index(row[1][0])
                if h_ind == 0:
                    lowest_key = row[0].replace('-v3', '').replace('-v4', '')+'_'+row[1][0]
                    if 'Generic' == row[1][1]:
                        lowest_key = 'Generic'
                    if lowest_key not in within_question_axis_lowest:
                        within_question_axis_lowest[lowest_key] = [['', 100, 100, False] for _ in range(num_metrics)]

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
                        axes[plot_num][col].errorbar([actual], [ind+offset], xerr=[[actual-lower], [higher-actual]], c=c, capsize=3., ms=6, marker='.')
                        xlims[met][0] = np.amin([xlims[met][0], lower])
                        xlims[met][1] = np.amax([xlims[met][1], higher])
                        if h_ind == 0:
                            if high83 < within_question_axis_lowest[lowest_key][met][1]:
                                within_question_axis_lowest[lowest_key][met] = [this_name, low83, high83, True]
                            elif low83 < within_question_axis_lowest[lowest_key][met][1]:
                                within_question_axis_lowest[lowest_key][met] = [this_name, low83, high83, False]
                            elif low83 < within_question_axis_lowest[lowest_key][met][2]: ## set to be False if another makes it not stat sig
                                within_question_axis_lowest[lowest_key][met][3] = False
                    else:
                        assert False

        fontsize=14
        for i in range(len(row_axes)):
            if i in [0, 1]:
                yticks = np.arange(len(axes_identity_names))
                if i == 0:
                    denom = 4
                elif i == 1:
                    denom = 8
            elif i in [2]:
                yticks = np.array([6, 7, 8, 9, 10, 11])
                denom = 12
            if 'temp_1o' in file:
                yticks = np.array([12, 13, 14, 15])
            j_range = yticks
            for j in range(len(axes[0])):
                axes[i][j].plot([0]*(len(yticks)), yticks, c='k', linestyle='dashed')
                axes[i][j].set_yticks(yticks)
                axes[i][j].set_yticklabels(['' for _ in range(len(yticks))], fontsize=fontsize)
                axes[i][j].set_ylim(bottom=np.amin(yticks)-.5, top=np.amax(yticks)+.5)
                axes[i][j].set_xlim(left=(xlims[j][0]*1.05 if xlims[j][0]<0 else xlims[j][0]*.95), right=xlims[j][1]*1.05)
                axes[i][j].tick_params(axis='x', labelsize=fontsize)

            make_smaller_right = True # gets rid of intersection name on right side

            yticklabels = []
            these_lowest = np.concatenate([within_question_axis_lowest[include] for include in within_question_axis_lowest.keys() if row_axes[i] in include])
            for j in j_range:
                if 'Generic' == axes_identity_names[j]:
                    yticklabels.append(remove_a(axes_identity_names[j]))
                else:
                    this_name = axes_identity_names[j]
                    if ':' in this_name:
                        this_name = this_name.split(':')[1]
                        this_name = this_name[this_name.index('a'):]
                    numer = np.sum([((this_name in chunk[0]) and (chunk[3] == 'True')) for chunk in these_lowest])
                    extra_pad = ''
                    if i == 2:
                        extra_pad = '     '
                    elif i == 3:
                        extra_pad = '         '
                    yticklabels.append(extra_pad+remove_a(axes_identity_names[j]).replace('intersection', 'intersectional'))

            axes[i][0].set_yticklabels(yticklabels, fontsize=fontsize)

            yticklabels = []
            for j in j_range:
                if 'Generic' == axes_identity_names[j]:
                    yticklabels.append(axes_identity_names[j])
                else:
                    this_name = axes_identity_names[j]
                    if ':' in this_name:
                        this_name = this_name.split(':')[1]
                        this_name = this_name[this_name.index('a'):]
                    numer = np.sum([((this_name in chunk[0]) and (chunk[3] == 'True')) for chunk in these_lowest])
                    if ':' in axes_identity_names[j]:
                        axis, rest = axes_identity_names[j].split(':')
                        spaces, name = rest[:rest.index('a')], remove_a(rest[rest.index('a'):])
                        if make_smaller_right:
                            yticklabels.append(name)
                        else:
                            yticklabels.append(name + spaces + ': ' + axis)
                    else:
                        yticklabels.append(remove_a(axes_identity_names[j]))
            axes[i][3].set_yticklabels(yticklabels, fontsize=fontsize)

            for j in [1, 2]:
                axes[i][j].set_yticks([])

            axes[i][0].set_ylabel(row_axes[i].replace('R2a', 'R2-Relevant').replace('R2b', 'R3-Subj').replace('R1', 'R1-Contingent'), fontsize=fontsize)
            axes[i][3].yaxis.tick_right()

        axes[0][0].scatter([], [], c='k', label='Human')
        for met in np.arange(5):
            axes[0][subplot_mapping[0]].set_title('Ngram: Unique', fontsize=fontsize)
            axes[0][subplot_mapping[1]].set_title('SBERT: Cosine', fontsize=fontsize)
            axes[0][subplot_mapping[2]].set_title('SBERT: Cov Trace', fontsize=fontsize)
            axes[0][subplot_mapping[3]].set_title('MC: Unique', fontsize=fontsize)
        fig.align_ylabels(axes[:, 0])


        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}.png'.format(file, key), dpi=300)
        plt.close()

        if 'temp_1o' in file:
            continue
        num_metrics = 4

        all_nums_t_2 = [nums_t_2]
        if 'human' not in key:
            # overlay the human comparison
            humanin_nums_t_2 = all_model_nums['human-ingroup-nums_t_2']
            humanout_nums_t_2 = all_model_nums['human-outgroup-nums_t_2']
            all_nums_t_2.append(humanin_nums_t_2)
            all_nums_t_2.append(humanout_nums_t_2)
            fig, axes = plt.subplots(2, num_metrics, figsize=(16, 8))
            axes_identity_names = {}

            xlims = [[5, 0] for _ in range(len(subplot_mapping))]
            within_question_axis_lowest = {}
            for h_ind, this_nums_t_2 in enumerate(all_nums_t_2):
                for row in this_nums_t_2:
                    if 'intersection' not in row[1][0]: 
                        continue
                    plot_num = row_axes.index(row[0].replace('-v3', '').replace('-v4', '').split('-')[0] if 'R2b' not in row[0] else '-'.join(row[0].split('-')[:2]))

                    if 'name' in row[1][1]:
                        identity_name = row[1][1].split(' name')[0]
                        idx = int(row[1][1][-1])
                        iden_ind = oip.identities[row[1][0]].index(identity_name)
                        ind = (iden_ind*3) + idx + 1
                    else:
                        iden_ind = oip.identities[row[1][0]].index(row[1][1])
                        ind = iden_ind*3

                    if h_ind == 0:
                        lowest_key = row[0].replace('-v3', '').replace('-v4', '')+'_'+str(iden_ind)
                        if lowest_key not in within_question_axis_lowest:
                            within_question_axis_lowest[lowest_key] = [['', 100, 100, False] for _ in range(num_metrics)]

                    if h_ind == 0:
                        c = 'C{}'.format(iden_ind)
                        if row[1][1] == 'Generic':
                            c = 'C{}'.format(5)
                        offset = 0
                    elif h_ind == 1:
                        c = 'k'
                        offset = .1
                    elif h_ind == 2:
                        c = 'tab:gray'
                        offset = .2

                    ind = 11 - ind

                    spacing = 10

                    if 'name' not in row[1][1]:
                        axes_identity_names[ind] = '{0}: {2}{1}'.format(row[1][1], 'Iden', ' '*spacing)
                    else:
                        axes_identity_names[ind] = "Name {}".format(idx)

                    this_name = axes_identity_names[ind]

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
                            axes[plot_num][col].errorbar([actual], [ind+offset], xerr=[[actual-lower], [higher-actual]], c=c, capsize=3., ms=6, marker='.')
                            xlims[met][0] = np.amin([xlims[met][0], lower])
                            xlims[met][1] = np.amax([xlims[met][1], higher])
                            if h_ind == 0:
                                if high83 < within_question_axis_lowest[lowest_key][met][1]:
                                    within_question_axis_lowest[lowest_key][met] = [this_name, low83, high83, True]
                                elif low83 < within_question_axis_lowest[lowest_key][met][1]:
                                    within_question_axis_lowest[lowest_key][met] = [this_name, low83, high83, False]
                                elif low83 < within_question_axis_lowest[lowest_key][met][2]: ## set to be False if another makes it not stat sig
                                    within_question_axis_lowest[lowest_key][met][3] = False

                        else:
                            axes[plot_num][col].scatter(row[2+met], ind+offset, c=c, s=20)
                            assert False
            for i in range(2):
                yticks = np.arange(len(axes_identity_names))
                if i == 0:
                    denom = 4
                elif i == 1:
                    denom = 8
                j_range = yticks
                for j in range(len(axes[0])):
                    axes[i][j].plot([0]*(len(yticks)), yticks, c='k', linestyle='dashed')
                    axes[i][j].set_yticks(yticks)
                    axes[i][j].set_yticklabels(['' for _ in range(len(yticks))])
                    axes[i][j].set_ylim(bottom=np.amin(yticks)-.5, top=np.amax(yticks)+.5)
                    axes[i][j].set_xlim(left=(xlims[j][0]*1.05 if xlims[j][0]<0 else xlims[j][0]*.95), right=xlims[j][1]*1.05)

                yticklabels = []
                these_lowest = np.concatenate([within_question_axis_lowest[include] for include in within_question_axis_lowest.keys() if row_axes[i] in include])
                for j in j_range:
                    this_name = axes_identity_names[j]
                    if ':' in this_name:
                        this_name = this_name.split(':')[1]
                    numer = np.sum([((this_name in chunk[0]) and (chunk[3] == 'True')) for chunk in these_lowest])
                    yticklabels.append(axes_identity_names[j])

                axes[i][0].set_yticklabels(yticklabels)

                axes[i][3].set_yticklabels(yticklabels)

                for j in [1, 2]:
                    axes[i][j].set_yticks([])

                axes[i][0].set_ylabel(row_axes[i])
                axes[i][3].yaxis.tick_right()
        
            axes[0][0].scatter([], [], c='tab:gray', label='Out')
            axes[0][0].scatter([], [], c='k', label='In')
            axes[0][0].legend()
            for met in np.arange(5):
                axes[0][subplot_mapping[0]].set_title('Unique n-grams')
                axes[0][subplot_mapping[1]].set_title('Pairwise cos dist')
                axes[0][subplot_mapping[2]].set_title('Trace of Cov')
                axes[0][subplot_mapping[3]].set_title('Unique MC')


            plt.tight_layout()
            plt.savefig('analysis_results/{0}_fig_{1}_intersectname.png'.format(file, key), dpi=300)
            plt.close()

    elif 'nums_t_3' in key:

        nums_t_3 = all_model_nums[key]
        identity_axes = ['intersection', 'race', 'gender', 'age', 'disability']
        row_axes = list(set([row[0] for row in nums_t_3]))
        row_axes = list(np.sort(row_axes))

        fig, axes = plt.subplots(len(row_axes), 6, figsize=(35, 45))
        axes_identity_names = {}

        for row in nums_t_3:
            plot_num = row_axes.index(row[0])

            iden_ind = identity_axes.index(row[1][0])
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
            ind = 0
            if iden_ind > 0:
                ind += (5+8)
                iden_ind -= 1
            ind = ind + (iden_ind*3) + next_ind
            ind = 24 - ind

            if next_ind == 0:
                if row[1][1] == 'Generic':
                    axes_identity_names[ind] = row[1][1]
                else:
                    axes_identity_names[ind] = "{0}: {1}".format(row[1][0], row[1][1])
            else:
                if row[1][1] == 'a Black man':
                    axes_identity_names[ind] = "intersection: " + row[1][1] 
                else:
                    axes_identity_names[ind] = row[1][1] 

            for met in np.arange(6):
                if met in [0, 1, 2, 3]:
                    assert len(row[2+met*2]) in [100, 10000], len(row[2+met*2])
                    assert len(row[2+met*2+1]) in [100, 10000]
                    in_dists = row[2+met*2]
                    in_std, in_mean = np.std(in_dists), np.mean(in_dists)
                    out_dists = row[2+met*2+1]
                    out_std, out_mean = np.std(out_dists), np.mean(out_dists)

                    axes[plot_num][met].errorbar([in_mean], [ind], xerr=[[1.96*in_std], [1.96*in_std]], c='C{}'.format(ind), capsize=5., ms=10, marker='.')
                    to_dash = axes[plot_num][met].errorbar([out_mean], [ind+.3], xerr=[[1.96*out_std], [1.96*out_std]], c='C{}'.format(ind), capsize=5., ms=10, marker='.', linestyle='dashed')
                    to_dash[-1][0].set_linestyle('dashed')
                    tstat, p = ttest_ind(out_dists, in_dists, equal_var=False, alternative='two-sided')
                    axes[plot_num][met].text(np.amin([in_mean-1.96*in_std, out_mean-1.96*out_std])-.02, ind+.15, 't: {0:.2f}\np: {1:.2f}'.format(tstat, p), fontsize='x-small')
                else:

                    in_lower, _, in_actual, _, in_higher = row[2+met*2]
                    out_lower, _, out_actual, _, out_higher = row[2+met*2+1]
                    axes[plot_num][met].errorbar([in_actual], [ind], xerr=[[in_actual-in_lower], [in_higher-in_actual]], c='C{}'.format(ind), capsize=5., ms=10, marker='.')
                    to_dash = axes[plot_num][met].errorbar([out_actual], [ind+.3], xerr=[[out_actual-out_lower], [out_higher-out_actual]], c='C{}'.format(ind), capsize=5., ms=10, marker='.', linestyle='dashed')
                    to_dash[-1][0].set_linestyle('dashed')


        for i in range(len(row_axes)):
            axes[i][5].plot([0]*(len(axes_identity_names)), np.arange(len(axes_identity_names)), c='k', linestyle='dashed')
            for j in range(len(axes[0])):
                axes[i][j].set_yticks(np.arange(len(axes_identity_names)))
            axes[i][0].set_yticklabels([axes_identity_names[j] if j in axes_identity_names else '' for j in range(len(axes_identity_names))])
            axes[i][0].set_ylabel(row_axes[i])
    
        axes[0][0].set_title('Ngram: Jaccard Distance')
        axes[0][1].set_title('Ngram: Closest Point Distance')
        axes[0][2].set_title('SBERT: Cosine Distance')
        axes[0][3].set_title('SBERT: Closest Point Distance')
        axes[0][4].set_title('MC: Wasserstein')
        axes[0][5].set_title('MC: (LLM - Group) Mean')

        axes[0][0].plot([], [], linestyle='dashed', label='Out portray')
        axes[0][0].plot([], [], label='In real')
        axes[0][0].legend()
        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}.png'.format(file, key), dpi=300)
        plt.close()

        # second one of just the t-statistics
        row_axes = list(set([row[0].split('-')[0] for row in nums_t_3]))
        row_axes = list(np.sort(row_axes))
        num_metrics = 6
        fig, axes = plt.subplots(len(row_axes), num_metrics, figsize=(18, 10), gridspec_kw={'height_ratios': [6.6, 6.6, 2]})
        axes_identity_names = {}
        axes_identity_counts = [{} for _ in range(len(row_axes))]
        xlims = [[0, 0] for _ in range(num_metrics)]
        rcParams['text.latex.preamble'] = [r'\usepackage{sfmath} \boldmath']

        for row in nums_t_3:
            plot_num = row_axes.index(row[0].split('-')[0])
            if 'name' in row[1][1]: # does not graph the intersectional names part
                continue

            iden_ind = identity_axes.index(row[1][0])
            color = iden_ind
            if 'name' in row[1][1]:
                color = 5
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
                    axes_identity_names[ind] = row[1][1]
                else:
                    if row[1][0] == 'race':
                        spacing = 31
                    elif row[1][0] == 'gender':
                        spacing = 44
                    elif row[1][0] == 'age':
                        spacing = 30
                    elif row[1][0] == 'disability':
                        spacing = 16
                    axes_identity_names[ind] = '{0}: {2}{1}'.format(row[1][0].capitalize(), this_name, ' '*spacing)
            else:
                if row[1][1] == 'a Black man':
                    spacing = 34
                    axes_identity_names[ind] = 'Intersection: ' + ' '*spacing + this_name
                else:
                    axes_identity_names[ind] = this_name

            if ind not in axes_identity_counts[plot_num]:
                axes_identity_counts[plot_num][ind] = 0
            for met in np.arange(num_metrics):
                if met in [0, 1, 2, 3]:
                    assert len(row[2+met*2]) in [100, 10000], len(row[2+met*2])
                    assert len(row[2+met*2+1]) in [100, 10000]
                    in_dists = row[2+met*2]
                    in_std, in_mean = np.std(in_dists), np.mean(in_dists)
                    out_dists = row[2+met*2+1]
                    out_std, out_mean = np.std(out_dists), np.mean(out_dists)


                    tstat, p = ttest_ind(in_dists, out_dists, equal_var=False, alternative='two-sided')
                    axes[plot_num][met].scatter([tstat], [ind], marker='x' if p >= .05 else 'o', c='C{}'.format(color))
                    if p < .05 and tstat > 0:
                        axes_identity_counts[plot_num][ind] += 1
                    xlims[met][0] = np.amin([xlims[met][0], tstat])
                    xlims[met][1] = np.amax([xlims[met][1], tstat])
                else:

                    in_lower, in_low83, in_actual, in_high83, in_higher = row[2+met*2]
                    out_lower, out_low83, out_actual, out_high83, out_higher = row[2+met*2+1]
                    if met == 4:
                        to_graph = in_actual-out_actual
                        statsig = False
                        if in_actual < out_actual:
                            if in_high83 < out_low83:
                                statsig = True
                        else:
                            if out_high83 < in_low83:
                                statsig = True
                    elif met == 5:
                        to_graph = np.absolute(in_actual)-np.absolute(out_actual)
                        statsig = False
                        in_low83, in_high83 = np.sort([np.absolute(in_low83), np.absolute(in_high83)])
                        out_low83, out_high83 = np.sort([np.absolute(out_low83), np.absolute(out_high83)])
                        if in_low83 < out_low83:
                            if in_high83 < out_low83:
                                statsig = True
                        else:
                            if out_high83 < in_low83:
                                statsig = True
                    else:
                        assert False

                    axes[plot_num][met].scatter([to_graph], [ind], c="C{}".format(color), marker = 'o' if statsig else 'x')
                    if to_graph > 0 and statsig:
                        axes_identity_counts[plot_num][ind] += 1
                    xlims[met][0] = np.amin([xlims[met][0], to_graph])
                    xlims[met][1] = np.amax([xlims[met][1], to_graph])

        fontsize=13
        for i in range(len(row_axes)):
            if i in [0, 1]:
                yticks = np.arange(len(axes_identity_names))
            elif i in [2]:
                yticks = np.array([6, 7, 8])
                yticks = np.array([6, 7, 8, 9, 10, 11])
            for j in range(len(axes[0])):
                axes[i][j].plot([0]*(len(yticks)), yticks, c='k', linestyle='dashed')
                axes[i][j].set_yticks(yticks)
                axes[i][j].set_yticklabels(['' for _ in range(len(yticks))], fontsize=fontsize)
                axes[i][j].set_ylim(bottom=np.amin(yticks)-.5, top=np.amax(yticks)+.5)
                axes[i][j].set_xlim(left=xlims[j][0]*1.07, right=xlims[j][1]*1.07)
                axes[i][j].tick_params(axis='x', labelsize=fontsize)
            if i == 0:
                denom = 6
            elif i == 1:
                denom = 12
            elif i in [2, 3]:
                denom = 18
            else:
                assert False

            make_smaller_right = True # gets rid of intersection name on right side

            if i in [0, 1]:
                axes[i][0].set_yticklabels([(remove_a(axes_identity_names[j]).replace('intersection', 'intersectional')+': ' + str(axes_identity_counts[i][j])+'/'+str(denom)) if j in axes_identity_counts[i] else axes_identity_names[j] for j in range(len(axes_identity_names))], fontsize=fontsize)
                yticklabels = []
                for j in range(len(axes_identity_names)):
                    if j in axes_identity_counts[i]:
                        if ':' in axes_identity_names[j]:
                            axis, rest = axes_identity_names[j].split(':')
                            spaces, name = rest[:rest.index('a')], remove_a(rest[rest.index('a'):])
                            if make_smaller_right:
                                yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name)
                            else:
                                yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name + spaces + ': ' + axis)
                        else:
                            yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + remove_a(axes_identity_names[j]))
                    else:
                        yticklabels.append(remove_a(axes_identity_names[j]))

                axes[i][5].set_yticklabels(yticklabels, fontsize=fontsize)

            elif i in [2]:
                axes[i][0].set_yticklabels([('     ' + remove_a(axes_identity_names[j]).replace('intersection', 'intersectional')+': ' + str(axes_identity_counts[i][j])+'/'+str(denom)) if j in axes_identity_counts[i] else axes_identity_names[j] for j in [6, 7, 8, 9, 10, 11]], fontsize=fontsize)
                yticklabels = []
                for j in [6, 7, 8, 9, 10, 11]:
                    if j in axes_identity_counts[i]:
                        if ':' in axes_identity_names[j]:
                            axis, rest = axes_identity_names[j].split(':')
                            spaces, name = rest[:rest.index('a')], remove_a(rest[rest.index('a'):])
                            if make_smaller_right:
                                yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name)
                            else:
                                yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name + spaces + ': ' + axis)
                        else:
                            yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + remove_a(axes_identity_names[j]))
                    else:
                        yticklabels.append(remove_a(axes_identity_names[j]))
                axes[i][5].set_yticklabels(yticklabels, fontsize=fontsize)
            elif i in [3]:
                axes[i][0].set_yticklabels([('         ' + remove_a(axes_identity_names[j]).replace('intersection', 'intersectional')+': ' + str(axes_identity_counts[i][j])+'/'+str(denom)) if j in axes_identity_counts[i] else axes_identity_names[j] for j in [9, 10, 11]], fontsize=fontsize)
                yticklabels = []
                for j in [9, 10, 11]:
                    if j in axes_identity_counts[i]:
                        if ':' in axes_identity_names[j]:
                            axis, rest = axes_identity_names[j].split(':')
                            spaces, name = rest[:rest.index('a')], remove_a(rest[rest.index('a'):])
                            if make_smaller_right:
                                yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name)
                            else:
                                yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name + spaces + ': ' + axis)
                        else:
                            yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + remove_a(axes_identity_names[j]))
                    else:
                        yticklabels.append(remove_a(axes_identity_names[j]))

                axes[i][5].set_yticklabels(yticklabels, fontsize=fontsize)

            for j in [1, 2, 3, 4]:
                axes[i][j].set_yticks([])

            axes[i][0].set_ylabel(row_axes[i].replace('R2a', 'R2-Relevant').replace('R2b', 'R3-Subj').replace('R1', 'R1-Contingent'), fontsize=fontsize)
            axes[i][5].yaxis.tick_right()

            for j in [0, 5]:
                for lab in axes[i][j].get_yticklabels():
                    labtext = lab.get_text()
                    if j == 0:
                        num, den = labtext.split(':')[-1].split('/')
                    elif j == 5:
                        num, den = labtext.split(':')[0].split('/')
                    if float(num)/float(den) > .5:
                        lab.set_fontweight('bold')

        axes[0][0].set_title('Ngram: Jaccard', fontsize=fontsize)
        axes[0][1].set_title('Ngram: Closest', fontsize=fontsize)
        axes[0][2].set_title('SBERT: Cosine', fontsize=fontsize)
        axes[0][3].set_title('SBERT: Closest', fontsize=fontsize)
        axes[0][4].set_title('MC: Wasserstein', fontsize=fontsize)
        axes[0][5].set_title('MC: LLM - Group', fontsize=fontsize)
        fig.align_ylabels(axes[:, 0])

        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}_v2.png'.format(file, key), dpi=300)
        plt.close()
        axes_identity_names_prev = copy.deepcopy(axes_identity_names)

        fig, axes = plt.subplots(2, num_metrics, figsize=(16.6, 8))
        axes_identity_names = {}
        axes_identity_counts = [{} for _ in range(len(row_axes))]
        xlims = [[0, 0] for _ in range(num_metrics)]

        for row in nums_t_3:
            plot_num = row_axes.index(row[0].split('-')[0])
            if 'intersection' not in row[1][0]: 
                continue

            if 'name' in row[1][1]:
                identity_name = row[1][1].split(' name')[0]
                idx = int(row[1][1][-1])
                iden_ind = oip.identities[row[1][0]].index(identity_name)
                ind = (iden_ind*3) + idx + 1
            else:
                iden_ind = oip.identities[row[1][0]].index(row[1][1])
                ind = iden_ind*3

            ind = 11 - ind 
            color = iden_ind

            spacing = 8

            if 'name' not in row[1][1]:
                axes_identity_names[ind] = '{0}: {2}{1}'.format(row[1][1], 'Iden', ' '*spacing)
            else:
                axes_identity_names[ind] = "Name {}".format(idx)

            this_name = axes_identity_names[ind]

            if ind not in axes_identity_counts[plot_num]:
                axes_identity_counts[plot_num][ind] = 0
            for met in np.arange(num_metrics):
                if met in [0, 1, 2, 3]:
                    assert len(row[2+met*2]) in [100, 10000], len(row[2+met*2])
                    assert len(row[2+met*2+1]) in [100, 10000]
                    in_dists = row[2+met*2]
                    in_std, in_mean = np.std(in_dists), np.mean(in_dists)
                    out_dists = row[2+met*2+1]
                    out_std, out_mean = np.std(out_dists), np.mean(out_dists)

                    tstat, p = ttest_ind(in_dists, out_dists, equal_var=False, alternative='two-sided')
                    axes[plot_num][met].scatter([tstat], [ind], marker='x' if p >= .05 else 'o', c='C{}'.format(color))
                    if p < .05 and tstat > 0:
                        axes_identity_counts[plot_num][ind] += 1
                    xlims[met][0] = np.amin([xlims[met][0], tstat])
                    xlims[met][1] = np.amax([xlims[met][1], tstat])
                else:

                    in_lower, in_low83, in_actual, in_high83, in_higher = row[2+met*2]
                    out_lower, out_low83, out_actual, out_high83, out_higher = row[2+met*2+1]
                    if met == 4:
                        to_graph = in_actual-out_actual
                        statsig = False
                        if in_actual < out_actual:
                            if in_high83 < out_low83:
                                statsig = True
                        else:
                            if out_high83 < in_low83:
                                statsig = True
                    elif met == 5:
                        to_graph = np.absolute(in_actual)-np.absolute(out_actual)
                        statsig = False
                        in_low83, in_high83 = np.sort([np.absolute(in_low83), np.absolute(in_high83)])
                        out_low83, out_high83 = np.sort([np.absolute(out_low83), np.absolute(out_high83)])
                        if in_low83 < out_low83:
                            if in_high83 < out_low83:
                                statsig = True
                        else:
                            if out_high83 < in_low83:
                                statsig = True
                    else:
                        assert False

                    axes[plot_num][met].scatter([to_graph], [ind], c="C{}".format(color), marker = 'o' if statsig else 'x')
                    if to_graph > 0 and statsig:
                        axes_identity_counts[plot_num][ind] += 1
                    xlims[met][0] = np.amin([xlims[met][0], to_graph])
                    xlims[met][1] = np.amax([xlims[met][1], to_graph])

        fontsize=13
        make_smaller_right = False # gets rid of intersection name on right side

        for i in range(2):
            yticks = np.arange(len(axes_identity_names))
            for j in range(len(axes[0])):
                axes[i][j].plot([0]*(len(yticks)), yticks, c='k', linestyle='dashed')
                axes[i][j].set_yticks(yticks)
                axes[i][j].set_yticklabels(['' for _ in range(len(yticks))])
                axes[i][j].set_ylim(bottom=np.amin(yticks)-.5, top=np.amax(yticks)+.5)
                axes[i][j].set_xlim(left=xlims[j][0]*1.07, right=xlims[j][1]*1.07)
                axes[i][j].tick_params(axis='x', labelsize=fontsize)
            if i == 0:
                denom = 6
            elif i == 1:
                denom = 12
            else:
                assert False
            axes[i][0].set_yticklabels([(remove_a(axes_identity_names[j])+': ' + str(axes_identity_counts[i][j])+'/'+str(denom)) if j in axes_identity_counts[i] else remove_a(axes_identity_names[j]) for j in range(len(axes_identity_names))], fontsize=fontsize)
            yticklabels = []
            for j in range(len(axes_identity_names)):
                if j in axes_identity_counts[i]:
                    if ':' in axes_identity_names[j]:
                        axis, rest = axes_identity_names[j].split(':')
                        spaces, name = rest[:rest.index('I')], remove_a(rest[rest.index('I'):])
                        if make_smaller_right:
                            yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name + spaces)
                        else:
                            yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + name + spaces + ': ' + axis)
                    else:
                        yticklabels.append(str(axes_identity_counts[i][j])+'/'+str(denom) + ': ' + remove_a(axes_identity_names[j]))
                else:
                    yticklabels.append(remove_a(axes_identity_names[j]))

            axes[i][5].set_yticklabels(yticklabels, fontsize=fontsize)

            for j in [1, 2, 3, 4]:
                axes[i][j].set_yticks([])

            axes[i][0].set_ylabel(row_axes[i].replace('R2a', 'R2-Relevant').replace('R2b', 'R3-Subj').replace('R1', 'R1-Contingent'), fontsize=fontsize)
            axes[i][5].yaxis.tick_right()

            for j in [0, 5]:
                for lab in axes[i][j].get_yticklabels():
                    labtext = lab.get_text()
                    if j == 0:
                        num, den = labtext.split(':')[-1].split('/')
                    elif j == 5:
                        num, den = labtext.split(':')[0].split('/')
                    if float(num)/float(den) > .5:
                        lab.set_fontweight('bold')

        axes[0][0].set_title('Ngram: Jaccard', fontsize=fontsize)
        axes[0][1].set_title('Ngram: Closest', fontsize=fontsize)
        axes[0][2].set_title('SBERT: Cosine', fontsize=fontsize)
        axes[0][3].set_title('SBERT: Closest', fontsize=fontsize)
        axes[0][4].set_title('MC: Wasserstein', fontsize=fontsize)
        axes[0][5].set_title('MC: LLM - Group', fontsize=fontsize)

        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}_v2_intersectname.png'.format(file, key), dpi=300)
        plt.close()

        fontsize=13
        row_axes = list(set([row[0].split('-')[0] for row in nums_t_3]))
        row_axes = list(np.sort(row_axes))
        fig, axes = plt.subplots(len(row_axes), 1, figsize=(8.3, 8.3), gridspec_kw={'height_ratios': [6.6, 6.6, 2.2]})
        
        name_ind_mapping = {}
        for k, v in axes_identity_names_prev.items():
            if ':' in v:
                name_ind_mapping[v.split(':')[1].strip()] = k
            else:
                name_ind_mapping[v] = k

        row_axes = list(set([row[0].split('-')[0] if 'R2b' not in row[0] else '-'.join(row[0].split('-')[:2]) for row in nums_t_3]))
        row_axes = list(np.sort(row_axes))
        fig, axes = plt.subplots(2, 1, figsize=(10, 10))
        
        name_ind_mapping = {}
        for k, v in axes_identity_names.items():
            if ':' in v:
                name_ind_mapping[v.split(':')[1].strip()] = k
            else:
                name_ind_mapping[v] = k

    elif 'nums_3_4' in key:
        subplot_mapping = {2: 2, 1: 0, 0: 1}
        fig, axes = plt.subplots(3, 3, figsize=(8, 8))
        fontsize=13
        nums_3_4 = all_model_nums[key]
        identity_axes = ['Generic', 'Astrology', 'Random personas', 'Myers-Briggs', 'Political', 'Race', 'Gender', 'Intersection', 'Age', 'Disability']
        identity_axes.reverse()

        for row in nums_3_4:
            plot_num = int(row[0].split('-')[1]) - 1
            ind = identity_axes.index(row[1])
            
            for met in np.arange(3):
                col = subplot_mapping[met]
                if type(row[2+met]) == np.ndarray or type(row[2+met])==list:
                    c = 2
                    if ind < 9:
                        c = 1
                    if ind <= 4:
                        c = 0
                    axes[plot_num][col].errorbar([np.median(row[2+met])], [ind], xerr=[[np.median(row[2+met])-np.amin(row[2+met])], [np.amax(row[2+met])-np.median(row[2+met])]], c='C{}'.format(c), capsize=5., ms=10, marker='.')
                else:
                    axes[plot_num][col].scatter(row[2+met], ind, c="C{}".format(ind), s=20)

        for i in range(3):
            axes[i][0].set_yticks(np.arange(len(identity_axes)))
            axes[i][0].set_yticklabels([' ' + id_ax for id_ax in identity_axes], fontsize=fontsize)
            axes[i][0].set_ylabel('Question {}'.format(i+1), fontsize=fontsize)

        axes[0][subplot_mapping[0]].set_title('SBERT: Vendi', fontsize=fontsize)
        axes[0][subplot_mapping[1]].set_title('SBERT: Cov Det', fontsize=fontsize)
        axes[0][subplot_mapping[2]].set_title('MC: Unique', fontsize=fontsize)
        plt.tight_layout()
        plt.savefig('analysis_results/{0}_fig_{1}.png'.format(file, key), dpi=200)
        plt.close()



