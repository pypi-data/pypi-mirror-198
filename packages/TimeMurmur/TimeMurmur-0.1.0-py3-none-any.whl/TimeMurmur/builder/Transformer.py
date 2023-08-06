# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats, special
from sklearn.preprocessing import (StandardScaler, MinMaxScaler, RobustScaler,
                                   PowerTransformer, MaxAbsScaler, QuantileTransformer)


class log:

    def __init__(self):
        pass

    def fit(self, y):
        pass

    def transform(self, y):
        transformed = np.log(y)
        return transformed

    def inverse_transform(self, y):
        transformed = np.exp(y)
        return transformed


class MurmurScaler:

    def __init__(self,
                 scaler,
                 scale,
                 difference,
                 linear_trend,
                 linear_test_window,
                 seasonal_period,
                 run_dict,
                 ts_id):
        self.scaler = scaler
        self.scale = scale
        self.difference = difference
        self.linear_trend = linear_trend
        self.linear_test_window = linear_test_window
        self.linear = False
        self.seasonal_period = seasonal_period
        self.run_dict = run_dict
        self.ts_id = ts_id
        self.predict = None
        factory_mapping = {'standard': StandardScaler(),
                           'minmax': MinMaxScaler(),
                           'maxabs': MaxAbsScaler(),
                           'robust': RobustScaler(),
                           'quantile': QuantileTransformer(),
                           'boxcox': PowerTransformer(method='box-cox'),
                           'log': log()
                            }
        self.transformer = factory_mapping[self.scaler]

    def fit(self, y):
        if self.scale:
            self.transformer.fit(y)

    def get_deterministic_trend(self, y):
        trend_line, self.linear, slope, intercept, penalty = self.linear_test(y)
        if self.linear or self.linear_trend==True:
            self.run_dict['global']['IDs with Trend'].append(self.ts_id)
            series_level = np.mean(trend_line)
            trend_line = trend_line# - series_level
            y = np.subtract(y.reshape((-1,)),
                            trend_line)
            self.run_dict['local'][self.ts_id]['trend']['trend_line'] = trend_line
            self.run_dict['local'][self.ts_id]['trend']['slope'] = slope
            self.run_dict['local'][self.ts_id]['trend']['intercept'] = trend_line[0]
            self.run_dict['local'][self.ts_id]['trend']['penalty'] = penalty
            self.run_dict['local'][self.ts_id]['trend']['series_level'] = series_level
        return y

    def linear_test(self, y):
        y = y
        xi = np.arange(1, len(y) + 1)
        # xi = xi**2
        slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y.reshape(-1, ))
        trend_line = slope*xi + intercept
        if self.seasonal_period is not None:
            required_len = 1.5 * max(self.seasonal_period)
        else:
            required_len = 6
        if self.linear_trend and len(y) > required_len:
            if self.linear_test_window is not None:
                n_bins = self.linear_test_window
            else:
                n_bins = (1 + len(y)**(1/3) * 2)
            splitted_array = np.array_split(y.reshape(-1,), int(n_bins))
            mean_splits = np.array([np.mean(i) for i in splitted_array])
            asc_array = np.sort(mean_splits)
            desc_array = np.flip(asc_array)
            if all(asc_array == mean_splits):
                growth = True
            elif all(desc_array == mean_splits):
                growth = True
            else:
                growth = False
            if (r_value > .9 and growth):
                linear = True
            else:
                linear = False
        else:
            linear = False
        # slope = slope * r_value
        return trend_line, linear, slope, intercept, r_value

    def transform(self, y):
        if self.linear_trend:
            y = self.get_deterministic_trend(y)
        else:
            self.run_dict['local'][self.ts_id]['trend']['trend_line'] = None
        if self.scale:
            y = self.transformer.transform(y.reshape(-1, 1))
        if self.difference is not None and self.difference:
            self.run_dict['local'][self.ts_id]['undifference'] = y[0]
            self.run_dict['local'][self.ts_id]['last_y'] = y[-1]
            y = np.diff(y, n=1, axis=0)
            y = np.append(0, y)
        return y

    def retrend_predicted(self, y):
        slope = self.run_dict['local'][self.ts_id]['trend']['slope']
        intercept = self.run_dict['local'][self.ts_id]['trend']['intercept']
        penalty = self.run_dict['local'][self.ts_id]['trend']['penalty']
        fit_trend = self.run_dict['local'][self.ts_id]['trend']['trend_line']
        n = len(fit_trend)
        # series_level = self.run_dict['local'][ts_id]['trend']['series_level']
        linear_trend = [i for i in range(0, len(y))]
        linear_trend = np.reshape(linear_trend, (len(linear_trend), 1))
        linear_trend += n + 1
        linear_trend = np.multiply(linear_trend, slope*penalty) + intercept
        linear_trend = linear_trend# - series_level
        y = np.add(y.reshape(-1), np.reshape(linear_trend, (-1,)))
        return y

    def retrend_fitted(self, y):
        trend = self.run_dict['local'][self.ts_id]['trend']['trend_line']
        y = np.add(y.reshape(-1), trend)
        return y

    def inverse_transform(self, y, **kwargs):
        if self.difference is not None and self.difference:
            if self.predict is None:
                actuals = kwargs['actuals']
                # actuals = actuals + self.run_dict['local'][self.ts_id]['undifference']
                if self.scale:
                    y = self.transformer.inverse_transform(y.reshape((-1,1)))
                y = np.append(actuals[0], actuals)[:-1] + y.reshape((-1, ))
                # y_0 = self.run_dict['local'][self.ts_id]['undifference']
                # y = np.r_[y_0, y[1:].reshape((-1,))].cumsum()
            else:
                y_0 = self.run_dict['local'][self.ts_id]['last_y']
                y = np.r_[y_0, y.reshape((-1,))].cumsum()[1:]
                if self.scale:
                    y = self.transformer.inverse_transform(y.reshape((-1,1)))
                # y_0 = y[-1]
        elif self.scale:
            y = self.transformer.inverse_transform(y.reshape((-1,1)))
        if self.linear:
            if self.predict is None:
                y = self.retrend_fitted(y)
            else:
                y = self.retrend_predicted(y)
        if self.predict is None:
            self.predict = True
        return y

