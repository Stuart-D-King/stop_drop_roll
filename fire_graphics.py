import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def prep_data():
    df = pd.read_csv('fire_types_1980_2015.csv', header=None)
    cols = ['year', 'total', 'fires', 'medical_aid', 'false_alarms', 'mutual_aid', 'haz_material', 'other_haz_material', 'other']
    df.columns = cols

    return df


def fires_medical_line(df):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)

    ax.plot(df.year.values, df.fires.values, color='red', label='Fires', linewidth=3)
    ax.plot(df.year.values, df.medical_aid.values, color='blue', label='Medical Aid', linewidth=3)

    ax.set_ylabel('Number of calls (in millions)', fontsize=16)
    ax.set_title('U.S. fire and medical calls from 1980 to 2015', fontsize=20)

    ax.set_yticklabels([0, 5, 10, 15, 20])
    ax.legend(loc='upper left', fontsize=16)

    plt.grid(b=True, which='major', color='lightgray', linestyle='--')
    plt.annotate('Source: National Fire Protection Association', (0,0), (0, -30), xycoords='axes fraction', textcoords='offset points', va='top', fontsize=12)

    # plt.tight_layout()
    plt.savefig('fires_medical.png', dpi=600)
    plt.show()


if __name__ == '__main__':
    plt.close('all')
    df = prep_data()
