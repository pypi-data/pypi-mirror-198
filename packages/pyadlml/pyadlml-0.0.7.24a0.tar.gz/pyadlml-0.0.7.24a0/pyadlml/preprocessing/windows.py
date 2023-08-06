from pyadlml.pipeline import XOrYTransformer, XAndYTransformer, YTransformer
from pyadlml.constants import ACTIVITY, END_TIME, OTHER, START_TIME, TIME
from sklearn.base import BaseEstimator, TransformerMixin
import dask
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
from pyadlml.dataset.plot.util import  \
    fmt_seconds2time, \
    fmt_seconds2time_log

class Windows(BaseEstimator, TransformerMixin):
    REP_M2M = 'many-to-many'
    REP_M2O = 'many-to-one'

    def __init__(self, rep, window_size, stride):
        self.rep = rep
        self.window_size = window_size
        self.stride = stride



class ExplicitWindow(BaseEstimator, TransformerMixin, XOrYTransformer):
    """
    https://www.mdpi.com/1424-8220/21/18/6037

    Divide the data stream into segments by 

    """
    def __init__(self, rep: str = 'many-to-many'):
        TransformerMixin.__init__(self)
        XOrYTransformer.__init__(self)
        self.rep = rep

    def fit(self, X, y):
        assert self.rep in ['many-to-many', 'many-to-one']

    def fit_transform(self, X, y):
        self.fit(X,y)
        return self.transform(X,y)

    @XOrYTransformer.x_or_y_transform
    def transform(self, X: pd.DataFrame, y:pd.DataFrame) -> pd.DataFrame:
        """

        Parameters
        ----------
        X: pd.DataFrame

        y: pd.DataFrame


        .. Note 
        -------

        Sequences are padded with NaNs to the length of the longest sequence in order to form a tensor.


        Returns
        -------
        X: np.ndarray with shape (S, F, T)
            where S is the #sequences, F is the #features, and T is the maxmimum sequence length
        y: np.ndarray with shape (S, T)
            where S is the #sequences and T is the maximum sequence length

        """
        assert len(y.columns) == 1

        y = y.copy().reset_index(drop=True)
        X = X.copy().reset_index(drop=True)

        # Assign each sequence a unique number
        y['tmp'] = (y[ACTIVITY] != y[ACTIVITY].shift(1)).cumsum()
        S = y['tmp'].iat[-1]
        T = y['tmp'].value_counts().max()
        F = len(X.columns)

        Xt = np.full((S, F, T), np.nan, dtype='object')
        if self.rep == 'many-to-many':
            yt = np.full((S, T), np.nan, dtype='object')
        else:
            yt = np.full((S), '', dtype='object')

        for s, (_, grp) in enumerate(y.groupby('tmp')):
            X_tmp = np.swapaxes(X.loc[grp.index, :].values, 0,1)
            Xt[s, :, :X_tmp.shape[-1]] = X_tmp
            if self.rep == 'many-to-many':
                y_tmp = y.loc[grp.index, y.columns[:-1]].values.squeeze(-1)
                yt[s, :y_tmp.shape[-1]] = y_tmp
            else:
                yt[s] = y.at[grp.index[0], ACTIVITY]

        return Xt, yt

class TimeWindow(Windows):
    """ Divide data stream into time segments with a regular interval.

    Note
    ----
    Also works with regular sampled data (dt='xs').
    Van Kasteren et al. recommend 60s. 

    """
    def __init__(self, window_size : str, stride: str = None, rep: str ='many-to-many',  drop_empty_intervals=True):
        TransformerMixin.__init__(self)
        XOrYTransformer.__init__(self)
        Windows.__init__(self, rep, window_size, stride)
        self.drop_empty_intervals = drop_empty_intervals

    def fit_transform(self, X, y):
        self.fit(X, y)
        return self.transform(X, y)

    def fit(self, X, y):

        # Bring params into right format
        assert self.rep in [self.REP_M2M, self.REP_M2O]
        self.window_size = pd.Timedelta(self.window_size)
        self.stride = pd.Timedelta(self.stride) if self.stride is not None else self.window_size

    @XOrYTransformer.x_or_y_transform
    def transform(self, X, y) -> np.ndarray:
        """
        
        
        """

        # TODO refactor add conversion for different input types
        assert isinstance(X, pd.DataFrame) or X is None
        assert isinstance(y, pd.DataFrame) or y is None

        df = X.copy().sort_values(by=TIME)
        st = X[TIME].iloc[0] - pd.Timedelta('1s')
        et = X[TIME].iloc[-1] + pd.Timedelta('1s')
        win_st = st

        X_list = []
        y_list = []
        max_seq_length = 0
        i = 0


        st_windows = pd.date_range(st, et-self.window_size, freq=self.stride)
        if self.drop_empty_intervals:
            times = df[TIME].copy()
            while win_st + self.window_size <= et:

                win = (win_st, win_st + self.window_size)
                # Important the interval is [st,et) right closed
                event_idxs = df[(win[0] <= df[TIME]) & (df[TIME] < win[1])].index
                
                if not event_idxs.empty:
                    X_list.append(X.iloc[event_idxs].copy())
                    y_list.append(y.iloc[event_idxs].copy())
                    max_seq_length = max(max_seq_length, len(X_list[i]))
                    win_st = win_st + self.stride
                    i += 1
                else:
                    # Get the next first window that covers the next event 
                    next_event_time = times[win_st < times].iloc[0]
                    win_min_idx_not_containing_ev = (st_windows <= next_event_time - self.window_size).cumsum().max() - 1
                    win_st = st_windows[win_min_idx_not_containing_ev + 1]
        else: 
            for win_st in st_windows:
                win = (win_st, win_st + self.window_size)
                event_idxs = df[(win[0] <= df[TIME]) & (df[TIME] < win[1])].index
                
                if not event_idxs.empty:
                    X_list.append(X.iloc[event_idxs].copy())
                    y_list.append(y.iloc[event_idxs].copy())
                    max_seq_length = max(max_seq_length, len(X_list[i]))
                    i += 1


        F = len(X.columns)
        S = len(X_list)
        T = max_seq_length
        Xt = np.full((S, F, T), np.nan, dtype='object')
        yt = np.full((S, T), '', dtype='object')

        for s, (X_tmp, y_tmp) in enumerate(zip(X_list, y_list)):
            X_tmp = np.swapaxes(X_tmp.values, 0,1)
            Xt[s, :, :X_tmp.shape[-1]] = X_tmp
            if self.rep == 'many-to-many':
                y_tmp = y_tmp.values.squeeze(-1)
                yt[s, :y_tmp.shape[-1]] = y_tmp
            else:
                yt[s] = y_tmp.iat[0, 0]

        return Xt, yt 

class FuzzyTimeWindows():
    """
    """
    def __init__(self):
        pass


class EventWindow(Windows, XOrYTransformer):
    """ Generate subsequences from a 

    .. image:: ../_static/images/many_to_many.svg
       :height: 200px
       :width: 500 px
       :scale: 90%
       :alt: alternate text
       :align: center


    .. image:: ../_static/images/reps/image.svg
       :height: 200px
       :width: 500 px
       :scale: 80%
       :alt: alternate text
       :align: center


    Many-To-Many
    ^^^^^^^^^^^^

    To get *many-to-many* batches use the window size :math:`w` to split the data

    .. math::
        f(X_{N,K},y_{N}) \rightarrow (X_{W, N,K}, y_{W, N})

    In addition you can specify a stride.


    .. code:: python

        from pyadlml.dataset import fetch_kasteren
        from pyadlml.preprocessing import EventWindows
        data = fetch_kasteren()

        raw = StateVectorEncoder(encode='raw', t_res='10s')\
              .fit_transform(data.df_devices)
        labels = LabelEncoder().fit_transform(raw, data.df_activities)

        X = raw.values
        y = labels.values

        X, y = EventWindows(rep='many-to-many', window_length=10, stride=2)\
               .fit_transform(X, y)

    Many-To-One
    ^^^^^^^^^^^

    .. math::
        f(X_{N,K},y_{N}) \rightarrow (X_{W, N, K}, y_{N})


    .. code:: python

        from pyadlml.preprocessing import SequenceDicer

        raw = StateVectorEncoder(encode='raw', t_res='10s')\
              .fit_transform(data.df_devices)
        labels = LabelEncoder().fit_transform(raw, data.df_activities)

        X = raw.values
        y = labels.values

        X, y = SequenceDicer(rep='many-to-one', window_length='20s')\
               .fit_transform(X, y)

    """
    def __init__(self, rep: str ='many-to-many', window_size: int =10, stride: int=1):
        """
        Parameters
        ----------
        rep: str 
        window_size: int
        stride: int

        """

        TransformerMixin.__init__(self)
        XOrYTransformer.__init__(self)
        Windows.__init__(self, rep, window_size, stride)
    
    def fit(self, X, y=None):
        self.feature_names_in_ = X.columns if isinstance(X, pd.DataFrame) else None


    def fit_transform(self, X, y=None):
        """
        Parameters
        ----------
        X : np.array
            Some kind of numpy array or pandas Dataframe
        y : np.array

        Returns
        -------
        x : np.array of shape ()
        y : np.array
            todo
        """
        self.fit(X, y)
        return self.transform(X, y)

    @XOrYTransformer.x_or_y_transform
    def transform(self, X=None, y=None):
        """

        """
        assert self.rep in [self.REP_M2M, self.REP_M2O]

        if X is not None:
            assert self.window_size < len(X)
            assert self.stride < len(X)

            X = self._transform_X(X)

        if y is not None:
            assert self.window_size < len(y)
            assert self.stride < len(y)

            y = self._transform_Y(y)

        return X, y

    def _calc_new_N(self, n_old):
        return int(np.floor((n_old-self.window_size)/self.stride)+1)

    def _transform_X(self, X):
        """

        """
        if isinstance(X, pd.DataFrame) or isinstance(X, pd.Series):
            X = X.to_numpy()

        n_prime = self._calc_new_N(X.shape[0])
        new_shape =[n_prime, self.window_size, *X.shape[1:]]

        res = np.zeros(shape=new_shape, dtype=X.dtype)

        for r, i in enumerate(range(0, n_prime*self.stride, self.stride)):
            res[r] = X[i:i+self.window_size]
            #res[r, :, :] = X[i:i+self.window_size, :]

        return res.squeeze()

    def _transform_Y(self, y):
        """


        """

        if isinstance(y, pd.DataFrame):
            y = y.to_numpy().squeeze()
        elif isinstance(y, pd.Series):
            y = y.to_numpy()

        if self.rep == self.REP_M2M:
            n_prime = self._calc_new_N(y.shape[0])
            new_shape = [n_prime, self.window_size, *y.shape[1:]]

            res = np.zeros(shape=new_shape, dtype=y.dtype)

            for r, i in enumerate(range(0, n_prime*self.stride, self.stride)):
                res[r, :] = y[i: i+self.window_size]

            return res.squeeze()

        elif self.rep == self.REP_M2O:
            res = y[np.arange(self.window_size-1, y.shape[0], self.stride)]
            return res.squeeze()



    def plotly_windows_into_acts_and_devs(self, df_devs, df_acts):
        """

        """

        # Get times 
        Xt = self.fit_transform(df_devs) # (S, T, 3)


        from pyadlml.plot import plotly_activities_and_devices
        fig = plotly_activities_and_devices(df_devs, df_acts)

        # Plot times as vertical bars into acts_and_devs plot 
        for i in range(Xt.shape[0]):
            st = Xt[i][0, 0]
            et = Xt[i][-1, 0]
            fig.add_vline(x=st, line_width=2, line_color="Red", line_dash="dash")
            fig.add_vline(x=et, line_width=2, line_color="Red")

        return fig

    def plot_activities_per_window(self, X, y):
        """ For an already encoded stream count how many different
            activities are present in windows
        """

        raise NotImplementedError

    def plot_timelengths_per_window(self, X, y, times=None):
        """ Plot time length distribution over given encoded stream
        """
        Xt = self.transform(X)
        raise NotImplementedError
       

    @classmethod
    def plot_winsize_vs_activities(cls, df_devs, df_acts, window_sizes=None):
        """


        """
        window_sizes = np.arange(2, 10000, 1000) if window_sizes is None else window_sizes
        x_times = df_devs[TIME].values

        title = 'Window size vs. Activities'
        time_unit = 's'
        _ = None


        total_counts = [] 
        means = np.zeros(len(window_sizes))
        stds = np.zeros(len(window_sizes))
        med = np.zeros(len(window_sizes))
        for j, s in enumerate(window_sizes):
            Xt = cls(window_size=s, stride=s//2).fit_transform(x_times)

            # Get normalized time lengths
            counts = np.zeros(Xt.shape[0])
            for i in range(Xt.shape[0]):
                st, et = Xt[i, 0], Xt[i, 1]
                x_in_int = lambda x: (st < x) & (x < et)
                act_covers = lambda s, e: (df_acts[START_TIME] < s) & (e < df_acts[END_TIME])
                counts[i] = (x_in_int(df_acts[START_TIME]) | x_in_int(df_acts[END_TIME]) | act_covers(st, et)).sum()
            total_counts.append(counts)
            means[j] = counts.mean()
            stds[j] = counts.std()
            med[j] = np.median(counts)



        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot(window_sizes, means, label='mean') 
        ax.plot(window_sizes, med, label='median')
        ax.plot(window_sizes, means + stds, linestyle='dashed', label='$\sigma$')
        ax.plot(window_sizes, means - stds, linestyle='dashed', label='-$\sigma$')
        ax.legend()
        return fig


    @classmethod
    def plotly_winsize_vs_length(cls, X, y, window_sizes=None, z_scale='linear', y_scale='linear'):
        """
        """
        import plotly.graph_objects as go
        window_sizes = np.arange(2, 1000, 10) if window_sizes is None else window_sizes

        assert window_sizes[0] > 1, 'Length is not defined for window containing one timestamp'

        # Reduce X to only time dimension
        # TODO, refactor 
        x_times = X[TIME].values

        title = 'Window size vs. window_length'
        cbarlabel = 'length' if z_scale == 'linear' else 'log length'
        n_bins = 100
        time_unit = 's'
        _ = None


        z = np.zeros((n_bins, len(window_sizes)), dtype=np.float32)
        dur_list = []
        dur_min = float('inf') 
        dur_max = float('-inf')
        for s in window_sizes:
            Xt = cls(window_size=s).fit_transform(x_times)
            # Get normalized time lengths
            Xt_dur = (Xt[:,-1] - Xt[:,0])/np.timedelta64(1, time_unit)
            
            dur_min = min(dur_min, Xt_dur.min())
            dur_max = max(dur_max, Xt_dur.max())
            dur_list.append(Xt_dur)

        # Make equal bin size from max to min
        # If log, Bins are equally sized in log space 
        #bin_gen = np.logspace if y_scale == 'log' else np.linspace
        #if y_scale == 'log':
        #    dur_min, dur_max = np.log10(dur_min), np.log10(dur_max)
        bin_gen = np.linspace
        bins = bin_gen(dur_min, dur_max, n_bins+1)


        for pos, d in enumerate(dur_list):
            hist, edges = np.histogram(d, bins=bins)
            z[:, pos] = hist

        z = np.log(z) if z_scale == 'log' else z

        fig = go.Figure(data=go.Heatmap(
                            x=window_sizes,
                            z=z,
                            colorscale='Viridis',
        ))
        if z_scale == 'log':
            tmpltstr = '%{x} event-length<br>' \
                     + ' -> %{customdata[1]} windows durating %{customdata[0]}.<extra></extra>'
            fig.data[0].hovertemplate = tmpltstr
            y_fmt = bins[:-1].copy().astype(object)

            for i in range(len(y_fmt)):
                if y_scale == 'log':
                    y_fmt[i] = fmt_seconds2time_log(y_fmt[i])
                else:
                    y_fmt[i] = fmt_seconds2time(y_fmt[i])

            y_fmt = np.repeat(y_fmt, len(window_sizes)).reshape(len(y_fmt), len(window_sizes))

            tmp = (np.exp(z.copy()) if z_scale == 'log' else z).astype(np.int32) 

            cd = np.array([y_fmt, tmp])
            fig['data'][0]['customdata'] = np.moveaxis(cd, 0, -1)

        #fig.update_yaxes(type='log')
        fig.update_layout(yaxis=dict(tickmode='array', tickvals=np.arange(len(bins[:-1])), ticktext=edges[:-1]))

        from pyadlml.dataset.plot.plotly.activities import _set_compact_title
        _set_compact_title(fig, title=title)
        return fig


    def construct_target_times(self, times: np.ndarray) -> np.ndarray:
        times = self._transform_Y(times)
        
        if self.rep == self.REP_M2M:
            # TODO take only last y-obs per sequence??? 
            # Or average y for each position when plotting 
            raise NotImplementedError
        
        return times


    def construct_X_at_target(self, X: pd.DataFrame, dev_slice=slice(None, None, None)) -> np.ndarray:
        """ Reconstruct the datapoints that are at the points
            where the target is evaluated

        Parameters
        ----------
        X: pd.DataFrame, (Tt, F)
            Transformed data right before windowing 

        Returns
        -------
        Xtarget : (S,)
        """

        # -> (S, T) or (S, T, F)
        X = self._transform_X(X)
        if self.rep == self.REP_M2O:
            if X.ndim == 2:
                X = X[:,:, None]

            # Select last event for T
            X = X[:, -1, dev_slice]
            if X.ndim == 3:
                X = X.squeeze(1)

            assert X.ndim == 2
            return X
        else:
            raise NotImplementedError
    

    def inverse_transform(self, X, y):
        """
        
        
        """
        if self.rep == self.REP_M2M:
            raise NotImplementedError

        elif self.rep == self.REP_M2O:
            raise NotImplementedError
