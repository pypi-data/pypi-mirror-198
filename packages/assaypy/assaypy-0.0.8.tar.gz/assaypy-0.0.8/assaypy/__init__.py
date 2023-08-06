import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress
import pprint
import tqdm
import warnings

import json

# READIN FUNCTIONS


def path_to_xlsx(path):
    import os
    if os.path.exists(path) is True:
        return path

    else:

        from tkinter import Tk
        from tkinter import filedialog

        Tk().withdraw()
        filename = filedialog.askopenfilename()

        return filename


def excel_to_pandas(_file: str) -> dict:
    """
    return pandas dataframes workbook by workbooks for main data.
    Load all datasheets from the excel file and trim first
    rows bc of header, can be saved or extracted via another function
    trim last 10 rows, to exclude last NaNs
    """
    try:
        dfs = pd.read_excel(_file, sheet_name=None, skiprows=0)
        worksheets = list(dfs)

        dfs = dict()

        for worksheet in tqdm.tqdm(worksheets):
            try:
                for n in range(200):
                    df = pd.read_excel(_file, sheet_name=worksheet, skiprows=n)
                    if 'Time [s]' in list(df):
                        print(worksheet, n, 'header lines')
                        dfs[worksheet] = pd.read_excel(_file, sheet_name=worksheet, skiprows=n)
                        break
            except Exception:
                print('couldnt resolve worksheet {}'.format(worksheet))

    except Exception:
        raise ImportError('Could not import excel files. Please make sure every worksheet starts with the column names without the comment section. OR wrong filename Error above?')

    for n in dfs:
        dfs[n] = dfs[n].dropna()
        dfs[n] = dfs[n].astype({'Time [s]': 'float'})
    return dfs


# dataframe handling
def remove_assays(dfs, to_remove=[]):
    '''
    Removes Assays from dfs from list to_remove.
    '''
    if isinstance(to_remove, list) is not True:
        raise ValueError('to_remove must be a list.')

    if len(to_remove) == 0:
        print('No assays to remove.')
    else:
        for i in to_remove:
            if i in list(dfs):
                try:
                    del dfs[i]
                    print('removed assays:', i)
                except Exception:
                    raise ValueError('could not find {}'.format(i))
            else:
                print(i, 'already removed or not in dict of dataframes.')


def keep_assays(dfs, to_keep=[]):
    '''
    Keep only assays from dfs from list to_keep.
    '''

    if isinstance(to_keep, list) is not True:
        raise ValueError('to_keep must be a list.')

    if len(to_keep) == 0:
        print('removed nothing. kept all')
    else:
        for i in list(dfs):
            if i not in to_keep:
                try:
                    del dfs[i]
                    print('removed assays:', i)

                except Exception:
                    raise ValueError('could not find {}'.format(i))
            else:
                print(i, 'already included')


# dataframe handling
def remove_assays(dfs, to_remove=[]):
    '''
    Removes Assays from dfs from list to_remove.
    '''
    if isinstance(to_remove, list) is not True:
        raise ValueError('to_remove must be a list.')

    if len(to_remove) == 0:
        print('No assays to remove.')
    else:
        for i in to_remove:
            if i in list(dfs):
                try:
                    del dfs[i]
                    print('removed assays:', i)
                except Exception:
                    raise ValueError('could not find {}'.format(i))
            else:
                print(i, 'already removed or not in dict of dataframes.')


def keep_assays(dfs, to_keep=[]):
    '''
    Keep only assays from dfs from list to_keep.
    '''

    if isinstance(to_keep, list) is not True:
        raise ValueError('to_keep must be a list.')

    if len(to_keep) == 0:
        print('removed nothing. kept all')
    else:
        for i in list(dfs):
            if i not in to_keep:
                try:
                    del dfs[i]
                    print('removed assays:', i)

                except Exception:
                    raise ValueError('could not find {}'.format(i))
            else:
                print(i, 'already included')


# GROUPING FUNCTIONS
def attach_dubtrip(dfs1):

    dubtrip = dict()
    for n in list(dfs1):
        print('--')
        dubtrip[n] = int(input('Dublet/Triplet for - {} -: '.format(n)))
    print(' ')
    print('final:')
    print('')

    pprint.pprint(dubtrip)
    return dubtrip


def group_wells(dfs, dubtrip, mode='A1-A2'):
    print('grouping wells with provided dubtrip data:')
    print('   ')
    pprint.pprint(dubtrip)
    print('   ')
    if mode == 'A1-A2':
        groups = dict()
        for n in list(dfs):
            groups[n] = dict()
            ct = 0
            _ = list()
            for i in list(dfs[n]):
                if i not in ['Cycle Nr.', 'Time [s]', 'CO2 %', 'O2 %', 'Temp. [°C]']:
                    _.append(i)
                    ct += 1
                    if ct == dubtrip[n]:
                        print('-'.join(_))
                        groups[n]['-'.join(_)] = _
                        ct = 0
                        _ = list()
            print(' ')

    elif mode == 'A1-B1':
        groups = dict()
        for n in list(dfs):
            groups[n] = dict()
            to_reshape = list(dfs[n])
            for rm in ['Cycle Nr.', 'Time [s]', 'CO2 %', 'O2 %', 'Temp. [°C]']:
                try:
                    to_reshape.remove(rm)
                except Exception:
                    pass

            _ = list()
            _list = list()
            for i in range(len(to_reshape)-1):
                startswith = to_reshape[i][0]
                next_startswith = to_reshape[i+1][0]
                if startswith == next_startswith:
                    _list.append(to_reshape[i])
                    if i == len(to_reshape)-2:
                        _list.append(to_reshape[i+1])
                        _.append(_list)
                else:
                    _list.append(to_reshape[i])
                    _.append(_list)
                    _list = list()
            reshaped = np.array(_).T.reshape(int(len(to_reshape)/dubtrip[n]), dubtrip[n]).flatten()
            ct = 0
            _ = list()
            for i in reshaped:
                if i not in ['Cycle Nr.', 'Time [s]', 'CO2 %', 'O2 %', 'Temp. [°C]']:
                    _.append(i)
                    ct += 1
                    if ct == dubtrip[n]:
                        print('-'.join(_))
                        groups[n]['-'.join(_)] = _
                        ct = 0
                        _ = list()
            print(' ')

    else:
        raise ValueError('grouping mode not clear')
    return groups


# ATTACH MOL DATA

def attach_trip_mol(groups):
    trip_mol = dict()
    for assay_name in list(groups):
        if (len(groups[assay_name][list(groups[assay_name])[0]])) == 2:
            trip_mol[assay_name] = dict()
            for gr in list(groups[assay_name]):
                trip_mol[assay_name][gr] = float(input('mol for {}?  '.format(gr)))
    # export to json:

    save = input('save? (Y/n)')
    if save == 'Y':
        with open(input('save as filename (json): ') + '.json', "w") as outfile:
            json.dump(trip_mol, outfile)
        print('saved')
    else:
        pass
    return trip_mol


def change_assay_dubtrip(dfs1, dubtrip):
    try:
        change_assay = input('which assay do you want to change? ')
        if change_assay in list(dfs1):
            dubtrip[change_assay] = int(input('to what? '))
            print(change_assay, ' set to ', dubtrip[change_assay])
            print('now:')
            print('')
            pprint.pprint(dubtrip)
        else:
            print(' ')
            print('nothing changed')
            print('still:')
            print('')
            pprint.pprint(dubtrip)

    except Exception:
        raise SyntaxError('error while handling data. repeat the previous steps. ')


# CHECKS and TESTS:


def check_dataframe(dfs, numbers_to_show=6):
    for n in dfs:
        print('Worksheet name: ', n)
        print(dfs[n].describe().iloc[:, :numbers_to_show])
        print('-------------------------------------------')
        print('-------------------------------------------')


# ANALYSIS:


def analyse_all(dfs, interval: int = 100, time0: bool = True, endtime: int = None) -> dict:
    '''
    interval = interval in seconds for slope analysis
    dubtrip  = dublicate or triplete data given, it seperates t
    time0 = start time of analysis, if true its starts after reaction starts but we can also give a number
    endtime = time in seconds where analysis ends
    '''

    all_slopes = dict()
    all_errors = dict()

    # make regression for all assays:
    for assay in dfs:
        header = list(dfs[assay])
        for t in ['Cycle Nr.', 'Time [s]', 'CO2 %', 'O2 %', 'Temp. [°C]']:
            header.remove(t)
        new_header = header.copy()
        new_header.insert(0, 'Time [s]')

        # timewise slicing
        df_sliced = dfs[assay]
        if time0 is True:
            time0_ = get_time_zero(dfs[assay])
            df_sliced = df_sliced[df_sliced['Time [s]'] > time0_]
        else:
            try:
                time0_ = time0
                df_sliced = df_sliced[df_sliced['Time [s]'] > time0_]
            except Exception:
                time0_ = 0
                df_sliced = dfs[assay]

        if endtime is None:
            df_sliced = df_sliced
        else:
            try:
                endtime_ = endtime
                df_sliced = df_sliced[df_sliced['Time [s]'] < endtime_]
            except Exception:
                print('couldnt slice endtime of experiment. analysis ending at {}s'.format(df_sliced['Time [s]']))

        _all_slopes = list()
        _all_errors = list()
        # slice from start to end point in seconds:
        for tt in range(0, int(np.max(df_sliced['Time [s]'])/interval)):
            try:
                df_sliced = df_sliced.astype({'Time [s]': 'float'})
                df_sliced_ = df_sliced[df_sliced['Time [s]'] >= tt*interval+time0_]
                df_sliced_ = df_sliced_[df_sliced_['Time [s]'] < (tt+1)*interval+time0_]
                _slope = list()
                _error = list()
                for i in header:
                    x = df_sliced_['Time [s]']
                    y = df_sliced_[i]
                    result = linregress(x, y)
                    _slope.append(result.slope)
                    _error.append(result.stderr)
                _slope.insert(0, float(tt*interval+time0_))
                _error.insert(0, float(tt*interval+time0_))
            except Exception:
                pass

            _all_slopes.append(_slope)
            _all_errors.append(_error)
        all_slopes[assay] = pd.DataFrame(_all_slopes, columns=new_header).dropna()
        all_errors[assay] = pd.DataFrame(_all_errors, columns=new_header).dropna()
    return all_slopes, all_errors


def plot_assays_and_slopes(dfs1,
                           groups,
                           slopes,
                           errslo,
                           show_average=True,
                           exclude=[]):
    '''
    dfs1 = dataframe
    groups = grouping information about all assays
    slopes = slope data
    errslo = information about slope error
    show_average = True -> plot with slope average
    exclude can be list of Assay names or dub/trip number
    '''
    for assay_to_plot in list(groups):
        if assay_to_plot not in exclude:
            print(assay_to_plot)
            for n in list(groups[assay_to_plot]):
                if len(groups[assay_to_plot][n]) not in exclude:
                    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
                    f.set_figheight(5)
                    f.set_figwidth(10)
                    plt.title(assay_to_plot + ' | ' + n)
                    list_for_average_slope = list()
                    for m in groups[assay_to_plot][n]:
                        ax1.plot(dfs1[assay_to_plot]['Time [s]'],
                                 dfs1[assay_to_plot][m])
                        ax2.errorbar(slopes[assay_to_plot]['Time [s]'],
                                     slopes[assay_to_plot][m],
                                     errslo[assay_to_plot][m],
                                     label=m)
                        list_for_average_slope.append(slopes[assay_to_plot][m])
                    # optional plot average:
                    if show_average is True:

                        _average_slopes = np.mean(list_for_average_slope)
                        _std_slopes = np.std(list_for_average_slope)

                        ax2.axhline(_average_slopes, label='avg', color='grey')
                        ax2.axhspan(_average_slopes-_std_slopes, _average_slopes+_std_slopes,
                                    color='grey', alpha=0.2, label='std')
                    plt.tight_layout()
                    ax2.set_xlabel('Time [s]')
                    ax1.set_ylabel('absorbance')
                    ax2.set_ylabel('absorbance change [absorbance/s]')
                    ax1.grid()
                    ax2.grid()
                    plt.legend()
                    plt.show()


# duplicate list into wells, so each well can be modified
def apply_to_all_wells(cabp_mol):
    for assay in list(cabp_mol):
        for enzyme in list(cabp_mol[assay]):
            for wellpair in list(cabp_mol[assay][enzyme]):
                for well in wellpair.split('-'):
                    cabp_mol[assay][enzyme][well] = cabp_mol[assay][enzyme][wellpair]
                if len(wellpair) > 3:
                    del cabp_mol[assay][enzyme][wellpair]
    return cabp_mol


def analyse_slopes(dfs1,
                   groups,
                   cabp_mol,
                   slopes,
                   errslo):

    cabp_slopes = dict()
    for assay in list(cabp_mol):
        cabp_slopes[assay] = dict()
        for enzyme in list(cabp_mol[assay]):
            cabp_slopes[assay][enzyme] = dict()
            for wellpair in groups[assay]:
                for well in list(groups[assay][wellpair]):
                    if well in list(cabp_mol[assay][enzyme]):
                        plt.figure()
                        plt.title(enzyme + ' | ' + assay + ' | ' + str(cabp_mol[assay][enzyme][well]) + 'mMol')
                        plt.errorbar(slopes[assay]['Time [s]'],
                                     slopes[assay][well],
                                     errslo[assay][well],
                                     label=well)

                        f = slopes[assay][slopes[assay]['Time [s]'] > get_time_zero(dfs1[assay])]
                        fall = np.array(f[well])[:-1]
                        fmean = np.mean(np.array(f[well])[:-1])
                        cabp_slopes[assay][enzyme][well] = (fmean, list(fall))
                        plt.plot([get_time_zero(dfs1[assay]),
                                 np.max(f['Time [s]'])],
                                 [fmean, fmean],
                                 label=well + 'mean: ' + str(np.around(np.mean(f[well]), 8)))

                        plt.plot([get_time_zero(dfs1[assay]), get_time_zero(dfs1[assay])],
                                 [np.min(slopes[assay][well]), np.max(slopes[assay][well])],
                                 color='grey', label='time 0')
                        plt.legend()
                        plt.show()
    return cabp_slopes


def analyse_cabp_slopes(dfs1,
                        groups,
                        cabp_mol,
                        slopes,
                        errslo):
    warnings.warn('analyse_cabp_slopes() was updated to analyse_slopes(). Please use analyse_slopes() instead from version 0.0.7.')
    return analyse_slopes(dfs1, groups, cabp_mol, slopes, errslo)


# CABP
def plot_cabp_slope_values(cabp_slopes,
                           cabp_mol,
                           exclude=[],
                           plot_all_slopes=True
                           ):
    '''
    cabp_slopes     = dict with dA/dt data of the measured wells
    cabp_mol        = dict with concentration data for the measured wells usually in µMol
    exclude         = list of string with assays or enzymes to exclude plotting
    plot_all_slopes = plots the histogram of all collected slope data from previous analysis
    '''

    for assay in list(cabp_slopes):
        if assay not in exclude:
            for enzyme in list(cabp_slopes[assay]):
                if enzyme not in exclude:

                    _max_wells = list()

                    _look_for_max_conc = [cabp_mol[assay][enzyme][well] for well in list(cabp_slopes[assay][enzyme])]
                    _max_conc = np.max(_look_for_max_conc)

                    for well in list(cabp_slopes[assay][enzyme]):
                        if cabp_mol[assay][enzyme][well] == _max_conc:
                            _max_wells.append(well)

                    _max_conc_slope = np.mean([cabp_slopes[assay][enzyme][n][0] for n in _max_wells])

                    wells_to_analyse = list(cabp_slopes[assay][enzyme])
                    for n in _max_wells:
                        wells_to_analyse.remove(n)

                    plt.figure(figsize=(10, 7))
                    plt.title(assay + ' | ' + enzyme)
                    for well in wells_to_analyse:
                        if plot_all_slopes is True:
                            plt.scatter(np.array(np.ones(len(cabp_slopes[assay][enzyme][well][1]))*cabp_mol[assay][enzyme][well]),
                                        -1*(np.array(cabp_slopes[assay][enzyme][well][1]) - _max_conc_slope), alpha=0.3,
                                        label=well + '|{}µmol'.format(cabp_mol[assay][enzyme][well]))
                        else:
                            plt.scatter(cabp_mol[assay][enzyme][well],
                                        -1*cabp_slopes[assay][enzyme][well][0] - _max_conc_slope, label=well + '|{}µmol'.format(cabp_mol[assay][enzyme][well]))

                    # plot the knockout concentration:
                    for well in _max_wells:
                        plt.scatter(np.array(np.ones(len(cabp_slopes[assay][enzyme][well][1]))*cabp_mol[assay][enzyme][well]),
                                    -1*(np.array(cabp_slopes[assay][enzyme][well][1]) - _max_conc_slope), alpha=0.3,
                                    label=well + '|{}µmol'.format(cabp_mol[assay][enzyme][well]))

                    # lin reg:
                    x = [cabp_mol[assay][enzyme][t] for t in wells_to_analyse]
                    y = np.array([cabp_slopes[assay][enzyme][t][0] - _max_conc_slope for t in wells_to_analyse])*-1

                    result = linregress(x, y)

                    xplot = np.linspace(0, _max_conc, 1000)
                    yplot = result.slope*np.array(xplot) + result.intercept

                    xintercept_index = np.argmin(np.diff(np.sign(yplot)))

                    plt.plot(xplot, yplot, color='grey', linestyle='dashed')
                    plt.scatter(xplot[xintercept_index], yplot[xintercept_index], color='black', marker='x',
                                label='x intercept')
                    print('xintercept', xplot[xintercept_index])
                    print('rvalue^2', result.rvalue**2)
                    print('baseline', _max_conc_slope)
                    plt.xlabel('concentration [µMol]')
                    plt.ylabel('absorption change [arb. units/s]')
                    plt.legend(loc='lower left')
                    plt.grid()
                    plt.show()


def plot_cabp_slopes(cabp_slopes,
                     cabp_mol,
                     exclude=[],
                     plot_all_slopes=True
                     ):
    warnings.warn('plot_cabp_slopes() was updated to plot_cabp_slope_values(). Please use plot_cabp_slope_values() instead from version 0.0.7.')
    return plot_cabp_slope_values(cabp_slopes, cabp_mol, exclude=[], plot_all_slopes=True)


# TRIP data
def plot_trip_slope_values(trip_slopes,
                           trip_mol,
                           exclude=[],
                           beta=1,
                           epsilon=6220,
                           plot_all_slopes=True
                           ):
    '''
    trip_slopes     = dict with dA/dt data of the measured wells
    trip_mol        = dict with concentration data for the measured wells usually in µMol
    exclude         = list of string with assays or enzymes to exclude plotting
    beta            = beta factor to correct measurement
    epsilon         = molar absorptivity
    plot_all_slopes = plots the histogram of all collected slope data from previous analysis
    '''

    for assay in list(trip_slopes):
        if assay not in exclude:
            for enzyme in list(trip_slopes[assay]):
                if enzyme not in exclude:

                    wells_to_analyse = list(trip_slopes[assay][enzyme])

                    plt.figure(figsize=(10, 7))
                    plt.title(assay + ' | ' + enzyme)
                    print(assay + ' | ' + enzyme)
                    print('name, slope [see plot for units], well')
                    for well in wells_to_analyse:
                        if plot_all_slopes is True:
                            if beta == 1:
                                plt.scatter(np.array(np.ones(len(trip_slopes[assay][enzyme][well][1]))*trip_mol[assay][enzyme][well]), -1*(np.array(trip_slopes[assay][enzyme][well][1])), alpha=0.3, label=well + '|{}'.format(trip_mol[assay][enzyme][well]))
                            else:
                                try:
                                    plt.scatter(np.array(np.ones(len(trip_slopes[assay][enzyme][well][1]))*trip_mol[assay][enzyme][well]), absorption_to_concentration(-1*np.array(np.array(trip_slopes[assay][enzyme][well][1])), beta, epsilon), alpha=0.3, label=well + '|{}'.format(trip_mol[assay][enzyme][well]))
                                    print(np.array(np.ones(len(trip_slopes[assay][enzyme][well][1]))*trip_mol[assay][enzyme][well]), absorption_to_concentration(-1*np.array(np.array(trip_slopes[assay][enzyme][well][1])), beta, epsilon), label=well + '|{}'.format(trip_mol[assay][enzyme][well]))
                                except Exception:
                                    raise ValueError('beta must be a number')
                        else:
                            if beta == 1:
                                plt.scatter(trip_mol[assay][enzyme][well], -1*trip_slopes[assay][enzyme][well][0], label=well + '|{}'.format(trip_mol[assay][enzyme][well]))
                            else:
                                try:
                                    plt.scatter(trip_mol[assay][enzyme][well], absorption_to_concentration(-1*trip_slopes[assay][enzyme][well][0], beta, epsilon), label=well + '|{}'.format(trip_mol[assay][enzyme][well]))
                                    print(trip_mol[assay][enzyme][well], absorption_to_concentration(-1*trip_slopes[assay][enzyme][well][0], beta, epsilon), str(well) + '|{}'.format(trip_mol[assay][enzyme][well]))
                                except Exception:
                                    raise ValueError('beta must be a number')
                    if beta == 1:
                        plt.ylabel('absorption change [arb. units/s]')
                    else:
                        plt.ylabel('absorption change [µmol/s]')
                    plt.xlabel('concentration [µMol]')
                    plt.legend(loc='upper left', ncols=3)
                    plt.grid()
                    plt.show()


def plot_trip_slopes(trip_slopes,
                     trip_mol,
                     exclude=[],
                     beta=1,
                     epsilon=6220,
                     plot_all_slopes=True
                     ):
    warnings.warn('plot_trip_slopes() was updated to plot_cabp_trip_values(). Please use plot_cabp_trip_values() instead from version 0.0.7.')
    return plot_trip_slope_values(trip_slopes, trip_mol, exclude=[], beta=1, epsilon=6220, plot_all_slopes=True)


# UTIL FUNCTIONS:
def print_data_structure(dfs):
    print('data structure with columns found:')
    print('   ')
    for n in list(dfs):
        _ = list()
        print(n)
        for i in list(dfs[n]):
            if i not in ['Cycle Nr.', 'Time [s]', 'CO2 %', 'O2 %', 'Temp. [°C]']:
                _.append(i)
        print(_)
        print('number of columns:', len(_))
        print('  ')


def get_time_zero(df):
    df = df.astype({'Time [s]': 'float'})
    times = df['Time [s]']
    diffs = np.diff(times)
    max_diffs = np.argmax(diffs)
    return times[max_diffs+1]


def absorption_to_concentration(A, beta, epsilon=6220):
    '''
    epsilon in 1/mol/cm
    beta in cm
    returns c in µmol
    '''
    c = A/(beta*epsilon)/2  # 2 number of possible spaces
    c = c * 1_000_000  # convert to µmol
    return c


def export_to_excel(slopes, path='output.xlsx'):
    with pd.ExcelWriter(path) as writer:
        for assay in list(slopes):
            slopes[assay].to_excel(writer, sheet_name=assay)


# extra dashboard functions:
def plot_slope_values(groups,
                      slopes,
                      exclude=[]):
    '''
    groups = grouping information about all assays
    slopes = slope data
    exclude = subgroups to exclude
    '''
    for assay_to_plot in list(groups):
        if assay_to_plot not in exclude:
            print(assay_to_plot)
            f, ax1 = plt.subplots(1, 1, sharex=True)
            f.set_figheight(5)
            f.set_figwidth(10)
            plt.title(assay_to_plot)
            for n in list(groups[assay_to_plot]):
                if len(groups[assay_to_plot][n]) not in exclude:
                    list_for_average_slope = list()
                    for m in groups[assay_to_plot][n]:
                        list_for_average_slope.append(slopes[assay_to_plot][m])

                    _average_slopes = np.mean(list_for_average_slope)
                    _std_slopes = np.std(list_for_average_slope)

                    ax1.scatter(n, _average_slopes, label=n)
                    ax1.scatter(n, _average_slopes-_std_slopes, color='grey', alpha=0.5)
                    ax1.scatter(n, _average_slopes+_std_slopes, color='grey', alpha=0.5)
                    plt.tight_layout()
                    plt.legend(ncols=3)
                    plt.xticks(rotation=90)
        plt.show()
