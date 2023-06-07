from math import log2
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

if __name__=='__main__':
    # probability = [9.313225746154785e-08, 3.461526833339259e-08, 2.5737055824708042e-08,
    #                2.1532783556302813e-08, 1.8983534636303025e-08, 1.7241866984387648e-08,
    #                1.5965003628384602e-08, 1.498458852361369e-08, 1.4207107602997257e-08,
    #                1.3575981380634252e-08, 1.3054753051628411e-08, 1.2618772683651448e-08,
    #                1.225073096151305e-08, 1.1938100722548432e-08, 1.1671593352175815e-08,
    #                1.1444187030263417e-08, 1.1250493015197223e-08, 1.1086330057222256e-08,
    #                1.0948431571427638e-08, 1.0834240208225823e-08, 1.0741761658911186e-08,
    #                1.066945975765324e-08, 1.0616181225409169e-08, 1.0581102392152162e-08,
    #                1.0563692858522121e-08]
    ID = [i for i in range(1, 51)]
    probability = [9.313225746154785e-08, 3.461526833339259e-08, 2.5737055824708042e-08,
                   2.1532783556302813e-08, 1.8983534636303025e-08, 1.7241866984387648e-08,
                   1.5965003628384602e-08, 1.498458852361369e-08, 1.4207107602997257e-08,
                   1.3575981380634252e-08, 1.3054753051628411e-08, 1.2618772683651448e-08,
                   1.225073096151305e-08, 1.1938100722548432e-08, 1.1671593352175815e-08,
                   1.1444187030263417e-08, 1.1250493015197223e-08, 1.1086330057222256e-08,
                   1.0948431571427638e-08, 1.0834240208225823e-08, 1.0741761658911186e-08,
                   1.066945975765324e-08, 1.0616181225409169e-08, 1.0581102392152162e-08,
                   1.0563692858522121e-08]
    probability +=  reversed(probability)
    for i in range(50):
        probability[i] = probability[i] * 1/(57*(2**7))
    fig = plt.figure()
    plt.rcParams['xtick.labelsize'] = 13  # x 轴刻度标签的字体大小
    plt.rcParams['ytick.labelsize'] = 13  # y 轴刻度标签的字体大小
    plt.xlabel('ID',fontsize=13)  # 设置x，y轴的标签
    plt.ylabel(r'$Pr_{success}$',fontsize=13)
    plt.scatter(ID, probability,marker='3')
    # 修改 y 轴刻度格式为 "10 的 -n 次方"
    plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    plt.gca().yaxis.set_minor_formatter(FormatStrFormatter('%1.0e'))
    fig.savefig('./maxProbability.pdf',dpi=600,format='pdf',bbox_inches='tight')

    plt.show()

    # mini_enptropy = []
    # for i in probability:
    #     mini_enptropy.append(-log2(i))
    # print(mini_enptropy)
    # fig = plt.figure()
    # plt.xlabel('ID',fontsize=13)  # 设置x，y轴的标签
    # plt.ylabel('Hmin',fontsize=13)
    # plt.scatter(ID, mini_enptropy,marker='3',color='g')
    # fig.savefig('./mini_enptropy.eps',dpi=600,format='eps',bbox_inches='tight')
    # plt.show()