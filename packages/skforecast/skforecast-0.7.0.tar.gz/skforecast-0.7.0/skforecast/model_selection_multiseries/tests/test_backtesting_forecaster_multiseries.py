# Unit test backtesting_forecaster_multiseries
# ==============================================================================
import re
import pytest
import numpy as np
import pandas as pd
from pytest import approx
import sys
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.exceptions import NotFittedError
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.ForecasterAutoregMultiSeries import ForecasterAutoregMultiSeries
from skforecast.ForecasterAutoregMultiSeriesCustom import ForecasterAutoregMultiSeriesCustom
from skforecast.ForecasterAutoregMultiVariate import ForecasterAutoregMultiVariate
from skforecast.model_selection_multiseries import backtesting_forecaster_multiseries
from skforecast.model_selection_multiseries import backtesting_forecaster_multivariate

# Fixtures
from .fixtures_model_selection_multiseries import series

def create_predictors(y): # pragma: no cover
    """
    Create first 2 lags of a time series.
    """
    lags = y[-1:-3:-1]

    return lags


@pytest.mark.parametrize("initial_train_size", 
                         [20., 21.2, 'not_int'], 
                         ids = lambda value : f'initial_train_size: {value}' )
def test_backtesting_forecaster_multiseries_TypeError_when_initial_train_size_is_not_an_int_or_None(initial_train_size):
    """
    Test TypeError is raised in backtesting_forecaster_multiseries when 
    initial_train_size is not an integer or None.
    """
    forecaster = ForecasterAutoregMultiSeries(
                     regressor = Ridge(random_state=123),
                     lags      = 3
                 )
    
    err_msg = re.escape(
            (f'If used, `initial_train_size` must be an integer greater than '
             f'the window_size of the forecaster. Got {type(initial_train_size)}.')
        )
    with pytest.raises(TypeError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = 'l1',
            metric              = 'mean_absolute_error',
            initial_train_size  = initial_train_size,
            refit               = False,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


@pytest.mark.parametrize("initial_train_size", 
                         [(len(series)), (len(series) + 1)], 
                         ids = lambda value : f'len: {value}' )
def test_backtesting_forecaster_multiseries_ValueError_when_initial_train_size_more_than_or_equal_to_len_series(initial_train_size):
    """
    Test ValueError is raised in backtesting_forecaster_multiseries when 
    initial_train_size >= len(series).
    """
    forecaster = ForecasterAutoregMultiSeries(
                     regressor = Ridge(random_state=123),
                     lags      = 3
                 )
    
    err_msg = re.escape(
            (f'If used, `initial_train_size` must be an integer '
             f'smaller than the length of `series` ({len(series)}).')
        )
    with pytest.raises(ValueError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = 'l1',
            metric              = 'mean_absolute_error',
            initial_train_size  = initial_train_size,
            refit               = False,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


def test_backtesting_forecaster_multiseries_ValueError_when_initial_train_size_less_than_forecaster_window_size():
    """
    Test ValueError is raised in backtesting_forecaster_multiseries when 
    initial_train_size < forecaster.window_size.
    """
    forecaster = ForecasterAutoregMultiSeries(
                     regressor = Ridge(random_state=123),
                     lags      = 3
                 )

    initial_train_size = forecaster.window_size - 1
    
    err_msg = re.escape(
            (f'If used, `initial_train_size` must be an integer greater than '
             f'the window_size of the forecaster ({forecaster.window_size}).')
        )
    with pytest.raises(ValueError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = ['l1'],
            metric              = 'mean_absolute_error',
            initial_train_size  = initial_train_size,
            refit               = False,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


def test_backtesting_forecaster_multiseries_NotFittedError_when_initial_train_size_None_and_forecaster_not_fitted():
    """
    Test NotFittedError is raised in backtesting_forecaster_multiseries when initial_train_size 
    is None and forecaster is not fitted.
    """
    forecaster = ForecasterAutoregMultiSeries(
                     regressor = Ridge(random_state=123),
                     lags      = 2
                 )

    initial_train_size = None
    
    err_msg = re.escape('`forecaster` must be already trained if no `initial_train_size` is provided.')
    with pytest.raises(NotFittedError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = 'l1',
            metric              = 'mean_absolute_error',
            initial_train_size  = initial_train_size,
            refit               = False,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


def test_backtesting_forecaster_multiseries_TypeError_when_refit_not_bool():
    """
    Test TypeError is raised in backtesting_forecaster_multiseries when refit is not bool.
    """
    forecaster = ForecasterAutoregMultiSeries(
                     regressor = Ridge(random_state=123),
                     lags      = 2
                 )

    refit = 'not_bool'
    
    err_msg = re.escape( f'`refit` must be boolean: `True`, `False`.')
    with pytest.raises(TypeError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = 'l1',
            metric              = 'mean_absolute_error',
            initial_train_size  = 12,
            refit               = refit,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


def test_backtesting_forecaster_multiseries_ValueError_when_initial_train_size_None_and_refit_True():
    """
    Test ValueError is raised in backtesting_forecaster_multiseries when initial_train_size is None
    and refit is True.
    """
    forecaster = ForecasterAutoregMultiSeries(
                     regressor = Ridge(random_state=123),
                     lags      = 2
                 )
    forecaster.fitted = True

    initial_train_size = None
    refit = True
    
    err_msg = re.escape(f'`refit` is only allowed when `initial_train_size` is not `None`.')
    with pytest.raises(ValueError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = 'l1',
            metric              = 'mean_absolute_error',
            initial_train_size  = initial_train_size,
            refit               = refit,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


def test_backtesting_forecaster_multiseries_TypeError_when_forecaster_not_a_forecaster_multiseries():
    """
    Test TypeError is raised in backtesting_forecaster_multiseries when forecaster is not of type
    'ForecasterAutoregMultiSeries', 'ForecasterAutoregMultiSeriesCustom' or 'ForecasterAutoregMultiVariate'.
    """
    forecaster = ForecasterAutoreg(
                     regressor = Ridge(random_state=123),
                     lags      = 2
                 )
    
    err_msg = re.escape(
            ("`forecaster` must be of type `ForecasterAutoregMultiSeries`, "
             "`ForecasterAutoregMultiSeriesCustom` or `ForecasterAutoregMultiVariate`, "
             "for all other types of forecasters use the functions available in "
             f"the `model_selection` module. Got {type(forecaster).__name__}")
        )
    with pytest.raises(TypeError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = 'l1',
            metric              = 'mean_absolute_error',
            initial_train_size  = 12,
            refit               = False,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


@pytest.mark.parametrize("levels, refit", 
                         [(1    , True), 
                          (1    , False)],
                         ids=lambda d: f'levels: {d}')
def test_backtesting_forecaster_multiseries_TypeError_when_levels_not_list_str_None(levels, refit):
    """
    Test TypeError is raised in backtesting_forecaster_multiseries when 
    `levels` is not a `list`, `str` or `None`.
    """
    forecaster = ForecasterAutoregMultiSeries(
                     regressor = Ridge(random_state=123),
                     lags      = 2
                 )
    
    err_msg = re.escape(
            (f"`levels` must be a `list` of column names, a `str` of a column name "
             f"or `None` when using a `ForecasterAutoregMultiSeries` or "
             f"`ForecasterAutoregMultiSeriesCustom`. If the forecaster is of type "
             f"`ForecasterAutoregMultiVariate`, this argument is ignored.")
        )
    with pytest.raises(TypeError, match = err_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 4,
            levels              = levels,
            metric              = 'mean_absolute_error',
            initial_train_size  = 12,
            refit               = refit,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


def test_backtesting_forecaster_multiseries_UserWarning_forecaster_multivariate_and_levels():
    """
    Test UserWarning is raised when levels is not forecaster.level or None in
    ForecasterAutoregMultiVariate.
    """
    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l1',
                     lags      = 2,
                     steps     = 3
                 )
    
    warn_msg = re.escape(
                (f"`levels` argument have no use when the forecaster is of type "
                 f"`ForecasterAutoregMultiVariate`. The level of this forecaster is "
                 f"{forecaster.level}, to predict another level, change the `level` "
                 f"argument when initializing the forecaster.")
            )
    with pytest.warns(UserWarning, match = warn_msg):
        backtesting_forecaster_multiseries(
            forecaster          = forecaster,
            series              = series,
            steps               = 3,
            levels              = 'not_forecaster.level',
            metric              = 'mean_absolute_error',
            initial_train_size  = 12,
            refit               = True,
            fixed_train_size    = False,
            exog                = None,
            interval            = None,
            n_boot              = 500,
            random_state        = 123,
            in_sample_residuals = True,
            verbose             = False
        )


# ForecasterAutoregMultiSeries and ForecasterAutoregMultiSeriesCustom
# ======================================================================================================================
@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_not_refit_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom without refit with mocked 
    (mocked done in Skforecast v0.5.0).
    """
    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = False,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = True
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'],
                                    'mean_absolute_error': [0.20754847190853098]})
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.4978839 , 0.46288427, 0.48433446, 
                                              0.48767779, 0.477799  , 0.48523814, 
                                              0.49341916, 0.48967772, 0.48517846, 
                                              0.49868447, 0.4859614 , 0.48480032])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_not_refit_not_initial_train_size_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom without refit and initial_train_size 
    is None with mocked, forecaster must be fitted, (mocked done in Skforecast v0.5.0).
    """

    forecaster.fit(series=series)

    steps = 1
    initial_train_size = None

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = mean_absolute_error,
                                               initial_train_size  = initial_train_size,
                                               refit               = False,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'],
                                    'mean_absolute_error': [0.18616882305307128]})
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.48459053, 0.49259742, 0.51314434, 0.51387387, 0.49192289,
                                              0.53266761, 0.49986433, 0.496257  , 0.49677997, 0.49641078,
                                              0.52024409, 0.49255581, 0.47860725, 0.50888892, 0.51923275,
                                              0.4773962 , 0.49249923, 0.51342903, 0.50350073, 0.50946515,
                                              0.51912045, 0.50583902, 0.50272475, 0.51237963, 0.48600893,
                                              0.49942566, 0.49056705, 0.49810661, 0.51591527, 0.47512221,
                                              0.51005943, 0.5003548 , 0.50409177, 0.49838669, 0.49366925,
                                              0.50348344, 0.52748975, 0.51740335, 0.49023212, 0.50969436,
                                              0.47668736, 0.50262471, 0.50267211, 0.52623492, 0.47776998,
                                              0.50850968, 0.53127329, 0.49010354])},
                               index=pd.RangeIndex(start=2, stop=50, step=1)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_refit_fixed_train_size_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom with refit, fixed_train_size and 
    custom metric with mocked (mocked done in Skforecast v0.5.0).
    """

    steps = 3
    n_validation = 12

    def custom_metric(y_true, y_pred): # pragma: no cover
        """
        """
        metric = mean_absolute_error(y_true, y_pred)
        
        return metric

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = ['l1'],
                                               metric              = custom_metric,
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = True, 
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = True
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'],
                                    'custom_metric': [0.21651617115803679]})
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.4978839 , 0.46288427, 0.48433446, 
                                              0.50853803, 0.50006415, 0.50105623,
                                              0.46764379, 0.46845675, 0.46768947, 
                                              0.48298309, 0.47778385, 0.47776533])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_refit_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom with refit with mocked 
    (mocked done in Skforecast v0.5.0).
    """

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'], 
                                    'mean_absolute_error': [0.2124129141233719]})
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.4978838984103099, 0.46288426670127997, 0.48433446479429937, 
                                               0.510664891759972, 0.49734477162307983, 0.5009680695304023,
                                               0.48647770856843825, 0.4884651517014008, 0.48643766346259326, 
                                               0.4973047492523979, 0.4899104838474172, 0.4891085370228432])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_refit_list_metrics_with_mocked_metrics(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom with refit and list of metrics with 
    mocked and list of metrics (mocked done in Skforecast v0.5.0).
    """

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = ['mean_absolute_error', mean_absolute_error],
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame(data    = [['l1', 0.2124129141233719, 0.2124129141233719]],
                                   columns = ['levels', 'mean_absolute_error', 'mean_absolute_error'])
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.4978838984103099, 0.46288426670127997, 0.48433446479429937, 
                                               0.510664891759972, 0.49734477162307983, 0.5009680695304023,
                                               0.48647770856843825, 0.4884651517014008, 0.48643766346259326, 
                                               0.4973047492523979, 0.4899104838474172, 0.4891085370228432])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_no_refit_levels_metrics_remainder_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom with no refit, remainder, multiple 
    levels and metrics with mocked (mocked done in Skforecast v0.5.0).
    """

    steps = 5
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = None,
                                               metric              = ['mean_absolute_error', mean_absolute_error],
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = False,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame(data    = [['l1', 0.21143995953996186, 0.21143995953996186],
                                              ['l2', 0.2194174144550234, 0.2194174144550234]],
                                   columns = ['levels', 'mean_absolute_error', 'mean_absolute_error'])
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.4978839 , 0.46288427, 0.48433446, 0.48677605, 0.48562473,
                                              0.50259242, 0.49536197, 0.48478881, 0.48496106, 0.48555902,
                                              0.49673897, 0.4576795 ]),
                               'l2':np.array([0.50266337, 0.53045945, 0.50527774, 0.50315834, 0.50452649,
                                              0.47372756, 0.51226827, 0.50650107, 0.50420766, 0.50448097,
                                              0.52211914, 0.51092531])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_refit_levels_metrics_remainder_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom with refit, remainder, multiple levels 
    and metrics with mocked (mocked done in Skforecast v0.5.0).
    """

    steps = 5
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = None,
                                               metric              = ['mean_absolute_error', mean_absolute_error],
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame(data    = [['l1', 0.20809130188099298, 0.20809130188099298],
                                              ['l2', 0.22082212805693338, 0.22082212805693338]],
                                   columns = ['levels', 'mean_absolute_error', 'mean_absolute_error'])
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.4978839 , 0.46288427, 0.48433446, 0.48677605, 0.48562473,
                                              0.49724331, 0.4990606 , 0.4886555 , 0.48776085, 0.48830266,
                                              0.52381728, 0.47432451]),
                               'l2':np.array([0.50266337, 0.53045945, 0.50527774, 0.50315834, 0.50452649,
                                              0.46847508, 0.5144631 , 0.51135241, 0.50842259, 0.50838289,
                                              0.52555989, 0.51801796])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_not_refit_exog_interval_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom without refit with mocked using exog 
    and intervals (mocked done in Skforecast v0.5.0).
    """

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = ['l1'],
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = False,
                                               fixed_train_size    = False,
                                               exog                = series['l1'].rename('exog_1'),
                                               interval            = [5, 95],
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'], 
                                    'mean_absolute_error': [0.14238176570382063]})
    expected_predictions = pd.DataFrame(
                               data = np.array([[0.64371728, 0.36845896, 0.91248693],
                                                [0.47208179, 0.19871058, 0.74002421],
                                                [0.52132498, 0.24592578, 0.78440458],
                                                [0.3685079 , 0.09324957, 0.63727755],
                                                [0.42192697, 0.14855575, 0.68986939],
                                                [0.46785602, 0.19245683, 0.73093562],
                                                [0.61543694, 0.34017861, 0.88420659],
                                                [0.41627752, 0.14290631, 0.68421995],
                                                [0.4765156 , 0.20111641, 0.7395952 ],
                                                [0.65858347, 0.38332514, 0.92735312],
                                                [0.49986428, 0.22649307, 0.7678067 ],
                                                [0.51750994, 0.24211075, 0.78058954]]),
                               columns = ['l1', 'l1_lower_bound', 'l1_upper_bound'],
                               index = np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


@pytest.mark.parametrize("forecaster", 
                         [ForecasterAutoregMultiSeries(regressor=Ridge(random_state=123), 
                                                       lags=2), 
                          ForecasterAutoregMultiSeriesCustom(regressor=Ridge(random_state=123), 
                                                             fun_predictors=create_predictors, 
                                                             window_size=2)], 
                         ids=lambda forecaster: f'forecaster: {type(forecaster).__name__}')
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiSeries_refit_fixed_train_size_exog_interval_with_mocked(forecaster):
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiSeries 
    and ForecasterAutoregMultiSeriesCustom with refit and fixed_train_size with 
    mocked using exog and intervals (mocked done in Skforecast v0.5.0).
    """

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = True,
                                               exog                = series['l1'].rename('exog_1'),
                                               interval            = [5, 95],
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'], 
                                    'mean_absolute_error': [0.1509587543248219]})
    expected_predictions = pd.DataFrame(
                               data = np.array([[0.64371728, 0.36845896, 0.91248693],
                                                [0.47208179, 0.19871058, 0.74002421],
                                                [0.52132498, 0.24592578, 0.78440458],
                                                [0.38179014, 0.15353798, 0.65675721],
                                                [0.43343713, 0.19888319, 0.70802106],
                                                [0.4695322 , 0.18716947, 0.74043601],
                                                [0.57891069, 0.31913315, 0.84636925],
                                                [0.41212578, 0.15090397, 0.69394422],
                                                [0.46851038, 0.20736343, 0.76349422],
                                                [0.63190066, 0.35803673, 0.90303047],
                                                [0.49132695, 0.21857874, 0.78112082],
                                                [0.51665452, 0.26139311, 0.80879351]]),
                               columns = ['l1', 'l1_lower_bound', 'l1_upper_bound'],
                               index = np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


# ForecasterAutoregMultiVariate
# ======================================================================================================================
def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiVariate_not_refit_with_mocked():
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiVariate without refit
    with mocked (mocked done in Skforecast v0.6.0).
    """

    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l1',
                     lags      = 2,
                     steps     = 3
                 )

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multivariate(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = False,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = True
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'],
                                    'mean_absolute_error': [0.2056686186667702]})
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.55397908, 0.48026456, 0.52368724,
                                              0.48490132, 0.46928502, 0.52511441, 
                                              0.46529858, 0.45430583, 0.51706306, 
                                              0.50561424, 0.47109786, 0.45568319])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiVariate_not_refit_not_initial_train_size_with_mocked():
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiVariate 
    without refit and initial_train_size is None with mocked, forecaster must be fitted,
    (mocked done in Skforecast v0.6.0).
    """

    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l1',
                     lags      = 2,
                     steps     = 3
                 )
    forecaster.fit(series=series)

    steps = 1
    initial_train_size = None

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = ['l1'],
                                               metric              = mean_absolute_error,
                                               initial_train_size  = initial_train_size,
                                               refit               = False,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'],
                                    'mean_absolute_error': [0.17959810844511925]})
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.42102839, 0.47138953, 0.52252844, 0.54594276, 0.51253167,
                                              0.57557448, 0.45455673, 0.42240387, 0.48555804, 0.46974027,
                                              0.52264755, 0.45674877, 0.43440543, 0.47187135, 0.59653789,
                                              0.41804686, 0.53408781, 0.58853203, 0.49880785, 0.57834799,
                                              0.47345798, 0.46890693, 0.45765737, 0.59034503, 0.46198262,
                                              0.49384858, 0.54212837, 0.56867955, 0.5095804 , 0.47751184,
                                              0.50402253, 0.48993588, 0.52583999, 0.4306855 , 0.42782129,
                                              0.52841356, 0.62570147, 0.55585762, 0.48719966, 0.48508799,
                                              0.37122115, 0.53115279, 0.47119561, 0.52734455, 0.41557646,
                                              0.57546277, 0.57700474, 0.50898628])},
                               index=pd.RangeIndex(start=2, stop=50, step=1)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiVariate_refit_fixed_train_size_with_mocked():
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiVariate with refit,
    fixed_train_size and custom metric with mocked (mocked done in Skforecast v0.6.0).
    """

    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l2',
                     lags      = 2,
                     steps     = 3
                 )

    steps = 3
    n_validation = 12

    def custom_metric(y_true, y_pred): # pragma: no cover
        """
        """
        metric = mean_absolute_error(y_true, y_pred)
        
        return metric

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = None,
                                               metric              = custom_metric,
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = True, 
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = True
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l2'],
                                    'custom_metric': [0.2326510995879597]})
    expected_predictions = pd.DataFrame({
                               'l2':np.array([0.58478895, 0.56729494, 0.54469663,
                                              0.50326485, 0.53339207, 0.50892268, 
                                              0.46841857, 0.48498214, 0.52778775,
                                              0.51476103, 0.48480385, 0.53470992])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiVariate_refit_with_mocked():
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiVariate with refit
    with mocked (mocked done in Skforecast v0.6.0).
    """

    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l1',
                     lags      = 2,
                     steps     = 3
                 )

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'], 
                                    'mean_absolute_error': [0.20733067815663564]})
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.55397908, 0.48026456, 0.52368724, 
                                              0.49816586, 0.48470807, 0.54162611,
                                              0.45270749, 0.47194035, 0.53386908,
                                              0.55296942, 0.53498642, 0.44772825])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiVariate_refit_list_metrics_with_mocked_metrics():
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiVariate 
    with refit and list of metrics with mocked and list of metrics 
    (mocked done in Skforecast v0.6.0).
    """

    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l1',
                     lags      = 2,
                     steps     = 3
                 )

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = ['mean_absolute_error', mean_absolute_error],
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = False,
                                               exog                = None,
                                               interval            = None,
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame(data    = [['l1', 0.20733067815663564, 0.20733067815663564]],
                                   columns = ['levels', 'mean_absolute_error', 'mean_absolute_error'])
    expected_predictions = pd.DataFrame({
                               'l1':np.array([0.55397908, 0.48026456, 0.52368724, 
                                              0.49816586, 0.48470807, 0.54162611, 
                                              0.45270749, 0.47194035, 0.53386908, 
                                              0.55296942, 0.53498642, 0.44772825])},
                               index=np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiVariate_not_refit_exog_interval_with_mocked():
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiVariate 
    without refit with mocked using exog and intervals 
    (mocked done in Skforecast v0.7.0).
    """

    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l1',
                     lags      = 2,
                     steps     = 3
                 )

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = ['l1'],
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = False,
                                               fixed_train_size    = False,
                                               exog                = series['l1'].rename('exog_1'),
                                               interval            = [5, 95],
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'], 
                                    'mean_absolute_error': [0.080981301131163]})
    expected_predictions = pd.DataFrame(
                               data = np.array([[0.79017158, 0.65165001, 0.92309077],
                                                [0.49318335, 0.37085985, 0.6403262 ],
                                                [0.58563228, 0.46560056, 0.72877519],
                                                [0.26135924, 0.12283767, 0.39427843],
                                                [0.37825777, 0.25593427, 0.52540062],
                                                [0.45697738, 0.33694566, 0.60012028],
                                                [0.70804671, 0.56952514, 0.8409659 ],
                                                [0.33222686, 0.20990336, 0.47936971],
                                                [0.49603977, 0.37600804, 0.63918267],
                                                [0.79614494, 0.65762337, 0.92906413],
                                                [0.50007531, 0.37775181, 0.64721816],
                                                [0.55280975, 0.43277803, 0.69595266]]),
                               columns = ['l1', 'lower_bound', 'upper_bound'],
                               index = np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)


def test_output_backtesting_forecaster_multiseries_ForecasterAutoregMultiVariate_refit_fixed_train_size_exog_interval_with_mocked():
    """
    Test output of backtesting_forecaster_multiseries in ForecasterAutoregMultiVariate 
    with refit and fixed_train_size with mocked using exog and intervals 
    (mocked done in Skforecast v0.7.0).
    """

    forecaster = ForecasterAutoregMultiVariate(
                     regressor = Ridge(random_state=123),
                     level     = 'l1',
                     lags      = 2,
                     steps     = 3
                 )

    steps = 3
    n_validation = 12

    metrics_levels, backtest_predictions = backtesting_forecaster_multiseries(
                                               forecaster          = forecaster,
                                               series              = series,
                                               steps               = steps,
                                               levels              = 'l1',
                                               metric              = 'mean_absolute_error',
                                               initial_train_size  = len(series) - n_validation,
                                               refit               = True,
                                               fixed_train_size    = True,
                                               exog                = series['l1'].rename('exog_1'),
                                               interval            = [5, 95],
                                               n_boot              = 500,
                                               random_state        = 123,
                                               in_sample_residuals = True,
                                               verbose             = False
                                           )
    
    expected_metric = pd.DataFrame({'levels': ['l1'], 
                                    'mean_absolute_error': [0.07705832858897509]})
    expected_predictions = pd.DataFrame(
                               data = np.array([[0.79017158, 0.65165001, 0.92309077],
                                                [0.49318335, 0.37085985, 0.6403262 ],
                                                [0.58563228, 0.46560056, 0.72877519],
                                                [0.25636363, 0.10743222, 0.37710866],
                                                [0.37604542, 0.24241796, 0.52792491],
                                                [0.45439247, 0.32888843, 0.59559781],
                                                [0.70488052, 0.5596997 , 0.84559181],
                                                [0.32693583, 0.20085419, 0.47910327],
                                                [0.49099895, 0.35617576, 0.63524443],
                                                [0.82066806, 0.67917812, 0.95193044],
                                                [0.51109877, 0.39178411, 0.66186064],
                                                [0.54738032, 0.42195622, 0.69395717]]),
                               columns = ['l1', 'lower_bound', 'upper_bound'],
                               index = np.arange(38, 50)
                           )
                                   
    pd.testing.assert_frame_equal(expected_metric, metrics_levels)
    pd.testing.assert_frame_equal(expected_predictions, backtest_predictions)