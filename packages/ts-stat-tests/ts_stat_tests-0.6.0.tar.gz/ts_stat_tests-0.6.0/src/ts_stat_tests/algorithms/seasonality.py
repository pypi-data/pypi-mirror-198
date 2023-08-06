# ---------------------------------------------------------------------------- #
#                                                                              #
#    Setup                                                                  ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# Imports                                                                   ####
# ---------------------------------------------------------------------------- #


# Python ----
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

# Packages ----
import numpy as np
import pandas as pd
from numpy import array as arr
from pmdarima.arima.arima import ARIMA
from pmdarima.arima.auto import auto_arima
from pmdarima.arima.seasonality import CHTest, OCSBTest
from scipy.stats import chi2
from statsmodels.tools.validation import (
    array_like,
    bool_like,
    float_like,
    int_like,
    string_like,
)
from statsmodels.tsa.seasonal import STL, DecomposeResult, seasonal_decompose
from typeguard import typechecked

# Locals ----
from src.ts_stat_tests.algorithms.correlation import acf as _acf

# ---------------------------------------------------------------------------- #
# Exports                                                                   ####
# ---------------------------------------------------------------------------- #


__all__ = ["qs", "ocsb", "ch", "seasonal_strength", "trend_strength", "spikiness"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#    Algorithms                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def qs(
    x: array_like,
    freq: int_like = 0,
    diff: bool_like = True,
    residuals: bool_like = False,
    autoarima: bool_like = True,
) -> Union[Tuple[float_like, float_like], Tuple[float_like, float_like, ARIMA]]:
    r"""
    !!! summary "Summary"

        The $QS$ test, also known as the Ljung-Box test, is a statistical test used to determine whether there is any seasonality present in a time series forecasting model. It is based on the autocorrelation function (ACF) of the residuals, which is a measure of how correlated the residuals are at different lags.

        This function will implement the Python version of the R function [`qs()`](https://rdrr.io/cran/seastests/man/qs.html) from the [`seastests`](https://cran.r-project.org/web/packages/seastests/index.html) library.

    ???+ info "Details"

        If `residuals=False` the `autoarima` settings are ignored.

        If `residuals=True`, a non-seasonal ARIMA model is estimated for the time series. And the residuals of the fitted model are used as input to the test statistic. If an automatic order selection is used, the Hyndman-Khandakar algorithm is employed with: $\max(p)=\max(q)<=3$.

        The Q statistic is given by:

        $$
        QS = (n \times (n+2)) \times \sum_{k=1}^{h} \frac{r_k^2}{n-k}
        $$

        where:

        - $n$ is the sample size,
        - $r_k$ is the autocorrelation at lag $k$, and
        - $h$ is the maximum lag to be considered.

        ```
        QS = n(n+2) * sum(r_k^2 / (n-k)) for k = 1 to h
        ```

        The null hypothesis is that there is no correlation in the residuals beyond the specified lags, indicating no seasonality. The alternative hypothesis is that there is significant correlation, indicating seasonality.

        Here are the steps for performing the $QS$ test:

        1. Fit a time series model to your data, such as an ARIMA or SARIMA model.
        1. Calculate the residuals, which are the differences between the observed values and the predicted values from the model.
        1. Calculate the ACF of the residuals.
        1. Calculate the Q statistic, which is the sum of the squared values of the autocorrelations at different lags, up to a specified lag. Using the formula above.
        1. Compare the Q statistic to the critical value from the chi-squared distribution with degrees of freedom equal to the number of lags. If the Q statistic is greater than the critical value, then the null hypothesis is rejected, indicating that there is evidence of seasonality in the residuals.

        In summary, the $QS$ test is a useful tool for determining whether a time series forecasting model has adequately accounted for seasonality in the data. By detecting any seasonality present in the residuals, it helps to ensure that the model is capturing all the important patterns in the data and making accurate predictions.

    Params:
        x (array_like):
            The univariate time series data to test.
        freq (int, optional):
            The frequency of the time series data.<br>
            Defaults to `0`.
        diff (bool_like, optional):
            Whether or not to run `np.diff()` over the data.<br>
            Defaults to `True`.
        residuals (bool_like, optional):
            Whether or not to run & return the residuals from the function.<br>
            Defaults to `False`.
        autoarima (bool_like, optional):
            Whether or not to run the `AutoARIMA()` algorithm over the data.<br>
            Defaults to `True`.

    Raises:
        AttributeError: If `x` is empty, or `freq` is too low for the data to be adequately tested.
        ValueError: If, after differencing the data (by using `np.diff()`), any of the values are `None` (or `Null` or `np.nan`), then it cannot be used for QS Testing.

    Returns:
        stat (float):
            The $\text{QS}$ score for the given data set.
        pval (float):
            The p-value of the given test. Calculated using the survival function of the chi-squared algorithm (also defined as $1-\text{cdf(...)}$). For more info, see: [scipy.stats.chi2](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html)
        model (Optional[ARIMA]):
            The ARIMA model used in the calculation of this test.<br>
            Returned if `residuals` is `True`.

    !!! success "Credit"
        - All credit goes to the [`seastests`](https://cran.r-project.org/web/packages/seastests/index.html) library.

    ???+ Example "Examples"
        ```python linenums="1" title="Basic usage"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> qs(x=data, freq=12)
        {'stat': 194.4692892087745,
         'Pval': 5.90922325801522e-43,
         'model': None}
        ```
        ```python linenums="1" title="Advanced usage"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> qs(x=data, freq=12, diff=True, residuals=True, autoarima=True)
        {'stat': 101.85929391917927,
         'Pval': 7.612641184541459e-23,
         'model': ARIMA(order=(1, 1, 1), scoring_args={}, suppress_warnings=True)}
        ```

    ??? question "References"
        1. Hyndman, R. J. and Y. Khandakar (2008). Automatic Time Series Forecasting: The forecast Package for R. Journal of Statistical Software 27 (3), 1-22.
        1. Maravall, A. (2011). Seasonality Tests and Automatic Model Identification in TRAMO-SEATS. Bank of Spain.
        1. Ollech, D. and Webel, K. (2020). A random forest-based approach to identifying the most informative seasonality tests. Deutsche Bundesbank's Discussion Paper series 55/2020.

    ??? tip "See Also"
        - [github/seastests/qs.R](https://github.com/cran/seastests/blob/master/R/qs.R)
        - [rdrr/seastests/qs](https://rdrr.io/cran/seastests/man/qs.html)
        - [rdocumentation/seastests/qs](https://www.rdocumentation.org/packages/seastests/versions/0.15.4/topics/qs)
        - [Machine Learning Mastery/How to Identify and Remove Seasonality from Time Series Data with Python](https://machinelearningmastery.com/time-series-seasonality-with-python)
        - [StackOverflow/Simple tests for seasonality in Python](https://stackoverflow.com/questions/62754218/simple-tests-for-seasonality-in-python)
    """
    if x.isnull().all():
        raise AttributeError(f"All observations are NaN.")
    if diff and residuals:
        print(
            f"The differences of the residuals of a non-seasonal ARIMA model are computed and used."
            f"It may be better to either only take the differences or use the residuals."
        )
    if freq < 2:
        raise AttributeError(
            f"The number of observations per cycle is '{freq}', which is too small."
        )

    if residuals:
        if autoarima:
            max_order = 1 if freq < 8 else 3
            allow_drift = True if freq < 8 else False
            try:
                model = auto_arima(
                    y=x,
                    max_P=1,
                    max_Q=1,
                    max_p=3,
                    max_q=3,
                    seasonal=False,
                    stepwise=False,
                    max_order=max_order,
                    allow_drift=allow_drift,
                )
            except:
                try:
                    model = ARIMA(order=(0, 1, 1)).fit(y=x)
                except:
                    x = x
                    print(
                        f"Could not estimate any ARIMA model, original data series is used."
                    )
            else:
                x = model.resid()
        else:
            try:
                model = ARIMA(order=(0, 1, 1)).fit(y=x)
            except:
                x = x
                print(
                    f"Could not estimate any ARIMA model, original data series is used."
                )
            else:
                x = model.resid()
    else:
        model = None

    # Do diff
    y = np.diff(x) if diff else x

    # Pre-check
    if np.nanvar(y[~np.isnan(y)]) == 0:
        raise ValueError(
            f"The Series is a constant (possibly after transformations)."
            f"QS-Test cannot be computed on constants."
        )

    # Test Statistic
    ## Note, ignoring `mypy` check on this line because the message is:
    ## >>> error: Invalid tuple index type (actual type "List[int]", expected type "Union[int, slice]")
    ## >>>    rho = _acf(x=y, nlags=freq * 2, missing="drop")[[freq, freq * 2]]
    ## >>>                                                    ^
    ## However, the type is functionally correct... so just ignoring it.
    rho: Union[np.ndarray, Tuple[Union[np.ndarray, Optional[np.ndarray]]]] = _acf(
        x=y, nlags=freq * 2, missing="drop"
    )[[freq, freq * 2]]
    rho = arr([0, 0]) if np.any(arr(rho) <= 0) else rho
    N: int = len(y[~np.isnan(y)])
    QS: float = (
        N * (N + 2) * (rho[0] ** 2 / (N - freq) + arr(rho)[1] ** 2 / (N - freq * 2))  # type: ignore
    )
    Pval: float = chi2.sf(QS, 2)

    if residuals:
        return QS, Pval, model
    else:
        return QS, Pval


@typechecked
def ocsb(
    x: array_like, m: int_like, lag_method: string_like = "aic", max_lag: int_like = 3
):
    """
    !!! summary "Summary"

        Compute the Osborn, Chui, Smith, and Birchenhall ($OCSB$) test for an input time series to determine whether it needs seasonal differencing. The regression equation may include lags of the dependent variable. When `lag_method="fixed"`, the lag order is fixed to `max_lag`; otherwise, `max_lag` is the maximum number of lags considered in a lag selection procedure that minimizes the `lag_method` criterion, which can be `"aic"`, `"bic"` or corrected AIC `"aicc"`.

        Critical values for the test are based on simulations, which have been smoothed over to produce critical values for all seasonal periods

    ???+ info "Details"

        The $OCSB$ test is a statistical test that is used to check the presence of seasonality in time series data. Seasonality refers to a pattern in the data that repeats itself at regular intervals.

        The $OCSB$ test is based on the null hypothesis that there is no seasonality in the time series data. If the p-value of the test is less than the significance level (usually $0.05$), then the null hypothesis is rejected, and it is concluded that there is seasonality in the data.

        The $OCSB$ test involves dividing the data into two halves and calculating the mean of each half. Then, the differences between the means of each pair of halves are calculated for each possible pair of halves. Finally, the mean of these differences is calculated, and a test statistic is computed.

        The $OCSB$ test is useful for testing seasonality in time series data because it can detect seasonal patterns that are not obvious in the original data. It is also a useful diagnostic tool for determining the appropriate seasonal differencing parameter in ARIMA models.

        The equation for the $OCSB$ test statistic for a time series of length n is:

        $$
        OCSB = \\frac{1}{(n-1)} \\times \\sum \\left( \\left( x[i] - x \\left[ \\frac{n}{2+i} \\right] \\right) - \\left( x \\left[ \\frac{n}{2+i} \\right] - x \\left[ \\frac{i+n}{2+1} \\right] \\right) \\right) ^2
        $$

        where:

        - $n$ is the sample size, and
        - $x[i]$ is the $i$-th observation in the time series.

        ```
        OCSB = (1 / (n - 1)) * sum( ((x[i] - x[n/2+i]) - (x[n/2+i] - x[i+n/2+1]))^2 )
        ```

        In this equation, the time series is split into two halves, and the difference between the means of each half is calculated for each possible pair of halves. The sum of the squared differences is then divided by the length of the time series minus one to obtain the $OCSB$ test statistic.

        The null hypothesis of the $OCSB$ test is that there is no seasonality in the time series, and the alternative hypothesis is that there is seasonality. The test statistic is compared to a critical value from a chi-squared distribution with degrees of freedom equal to the number of possible pairs of halves. If the test statistic is larger than the critical value, then the null hypothesis is rejected, and it is concluded that there is evidence of seasonality in the time series.

    Params:
        x (array_like):
            The time series vector.
        m (int):
            The seasonal differencing term. For monthly data, e.g., this would be 12. For quarterly, 4, etc. For the OCSB test to work, `m` must exceed `1`.
        lag_method (str, optional):
            The lag method to use. One of (`"fixed"`, `"aic"`, `"bic"`, `"aicc"`). The metric for assessing model performance after fitting a linear model.<br>
            Defaults to `"aic"`.
        max_lag (int, optional):
            The maximum lag order to be considered by `lag_method`.<br>
            Defaults to `3`.

    Returns:
        D (int):
            The seasonal differencing term. For different values of `m`, the OCSB statistic is compared to an estimated critical value, and returns 1 if the computed statistic is greater than the critical value, or 0 if not.

    !!! success "Credit"
        - All credit goes to the [`pmdarima`](http://alkaline-ml.com/pmdarima/index.html) library with the implementation of [`pmdarima.arima.OCSBTest`](http://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.OCSBTest.html).

    !!! example "Examples"
        _description_
        ```python linenums="1" title="Python"
        >>> _description_
        ```

    ??? question "References"
        - Osborn DR, Chui APL, Smith J, and Birchenhall CR (1988) "Seasonality and the order of integration for consumption", Oxford Bulletin of Economics and Statistics 50(4):361-377.
        - R's forecast::OCSB test source code: https://bit.ly/2QYQHno

    ??? tip "See Also"
        - [pmdarima.arima.OCSBTest](http://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.OCSBTest.html)
    """
    return OCSBTest(
        m=m, lag_method=lag_method, max_lag=max_lag
    ).estimate_seasonal_differencing_term(x)


@typechecked
def ch(x: array_like, m: int_like) -> int_like:
    """
    !!! summary "Summary"

        The Canova-Hansen test for seasonal differences. Canova and Hansen (1995) proposed a test statistic for the null hypothesis that the seasonal pattern is stable. The test statistic can be formulated in terms of seasonal dummies or seasonal cycles. The former allows us to identify seasons (e.g. months or quarters) that are not stable, while the latter tests the stability of seasonal cycles (e.g. cycles of period 2 and 4 quarters in quarterly data).

        !!! warning "Note"
            This test is generally not used directly, but in conjunction with `pmdarima.arima.nsdiffs()`, which directly estimates the number of seasonal differences.

    ???+ info "Details"

        The $CH$ test (also known as the Canova-Hansen test) is a statistical test for detecting seasonality in time series data. It is based on the idea of comparing the goodness of fit of two models: a non-seasonal model and a seasonal model. The null hypothesis of the $CH$ test is that the time series is non-seasonal, while the alternative hypothesis is that the time series is seasonal.

        The test statistic for the $CH$ test is given by:

        $$
        CH = \\frac { \\left( \\frac { SSRns - SSRs } { n - p - 1 } \\right) } { \\left( \\frac { SSRs } { n - p - s - 1 } \\right) }
        $$

        where:

        - $SSRns$ is the $SSR$ for the non-seasonal model,
        - $SSRs$ is the $SSR$ for the seasonal model,
        - $n$ is the sample size,
        - $p$ is the number of parameters in the non-seasonal model, and
        - $s$ is the number of parameters in the seasonal model.

        ```
        CH = [(SSRns - SSRs) / (n - p - 1)] / (SSRs / (n - p - s - 1))
        ```

        The test statistic is compared to a critical value from the chi-squared distribution with degrees of freedom equal to the difference in parameters between the two models. If the test statistic exceeds the critical value, the null hypothesis of non-seasonality is rejected in favor of the alternative hypothesis of seasonality.

        The $CH$ test is based on the following steps:

        1. Fit a non-seasonal autoregressive integrated moving average (ARIMA) model to the time series data, using a criterion such as Akaike Information Criterion (AIC) or Bayesian Information Criterion (BIC) to determine the optimal model order.
        1. Fit a seasonal ARIMA model to the time series data, using the same criterion to determine the optimal model order and seasonal period.
        1. Compute the sum of squared residuals (SSR) for both models.
        1. Compute the test statistic $CH$ using the formula above.
        1. Compare the test statistic to a critical value from the chi-squared distribution with degrees of freedom equal to the difference in parameters between the two models. If the test statistic exceeds the critical value, reject the null hypothesis of non-seasonality in favor of the alternative hypothesis of seasonality.

        The $CH$ test is a powerful test for seasonality in time series data, as it accounts for both the presence and the nature of seasonality. However, it assumes that the time series data is stationary, and it may not be effective for detecting seasonality in non-stationary or irregular time series data. Additionally, it may not work well for time series data with short seasonal periods or with low seasonal amplitudes. Therefore, it should be used in conjunction with other tests and techniques for detecting seasonality in time series data.

    Params:
        x (array_like):
            The time series vector.
        m (int):
            The seasonal differencing term. For monthly data, e.g., this would be 12. For quarterly, 4, etc. For the Canova-Hansen test to work, `m` must exceed 1.

    Returns:
        D (int):
            The seasonal differencing term.

            The CH test defines a set of critical values:

            ```
            (0.4617146, 0.7479655, 1.0007818,
             1.2375350, 1.4625240, 1.6920200,
             1.9043096, 2.1169602, 2.3268562,
             2.5406922, 2.7391007)
            ```

            For different values of `m`, the CH statistic is compared to a different critical value, and returns `1` if the computed statistic is greater than the critical value, or `0` if not.

    !!! success "Credit"
        - All credit goes to the [`pmdarima`](http://alkaline-ml.com/pmdarima/index.html) library with the implementation of [`pmdarima.arima.CHTest`](http://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.CHTest.html).

    !!! example "Examples"
        _description_
        ```python linenums="1" title="Python"
        >>> _description_
        ```

    ??? question "References"
        - Testing for seasonal stability using the Canova and Hansen test statistic: http://bit.ly/2wKkrZo
        - R source code for CH test: https://github.com/robjhyndman/forecast/blob/master/R/arima.R#L148

    ??? tip "See Also"
        - [`pmdarima.arima.CHTest`](http://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.CHTest.html)
    """
    return CHTest(m=m).estimate_seasonal_differencing_term(x)


@typechecked
def seasonal_strength(x: array_like, m: int_like) -> float_like:
    """
    !!! summary "Summary"

        The seasonal strength test is a statistical test for detecting the strength of seasonality in time series data. It measures the extent to which the seasonal component of a time series explains the variation in the data.

    ???+ info "Details"

        The seasonal strength test involves computing the seasonal strength index ($SSI$) using the following formula:

        $$
        SSI = \\frac {Var(S)} {Var(S) + Var(R)}
        $$

        where:

        - $Var(S)$ is the variance of the seasonal component, and
        - $Var(R)$ is the variance of the residual component obtained after decomposing the time series data into its seasonal, trend, and residual components using a method such as seasonal decomposition of time series (STL) or moving average decomposition.

        ```
        SSI = Var(S) / (Var(S) + Var(R))
        ```

        The $SSI$ ranges between $0$ and $1$, with higher values indicating stronger seasonality in the data. The critical value for the $SSI$ can be obtained from statistical tables based on the sample size and level of significance. If the $SSI$ value exceeds the critical value, the null hypothesis of no seasonality is rejected in favor of the alternative hypothesis of seasonality.

        The seasonal strength test involves the following steps:

        1. Decompose the time series data into its seasonal, trend, and residual components using a method such as seasonal decomposition of time series (STL) or moving average decomposition.
        1. Compute the variance of the seasonal component ($Var(S)$).
        1. Compute the variance of the residual component ($Var(R)$).
        1. Compute the seasonal strength index ($SSI$) using the formula above.
        1. Compare the $SSI$ value to a critical value based on the sample size and level of significance. If the $SSI$ value exceeds the critical value, reject the null hypothesis of no seasonality in favor of the alternative hypothesis of seasonality.

        The seasonal strength test is a useful tool for identifying the strength of seasonality in time series data, and it can be used in conjunction with other tests and techniques for detecting seasonality. However, it assumes that the time series data is stationary and that the seasonal component is additive rather than multiplicative. Additionally, it may not be effective for time series data with short seasonal periods or with low seasonal amplitudes. Therefore, it should be used in conjunction with other tests and techniques for detecting seasonality in time series data.

    Params:
        x (array_like):
            The time series data set.
        m (int):
            The frequency of the time series data set.

    Returns:
        ssi (float):
            The seasonal strength score.

    !!! success "Credit"
        - Inspired by the `tsfeatures` library in both [`Python`](https://github.com/Nixtla/tsfeatures) and [`R`](http://pkg.robjhyndman.com/tsfeatures/).

    ???+ example "Examples"
        _description_
        ```python linenums="1"
        >>> _description_
        ```

    ??? question "References"
        - _description_

    ??? tip "See Also"
        - [`tsfeatures.stl_features`](https://github.com/Nixtla/tsfeatures/blob/main/tsfeatures/tsfeatures.py)
    """
    decomposition = seasonal_decompose(x=x, period=m, model="additive")
    seasonal = np.nanvar(decomposition.seasonal)
    residual = np.nanvar(decomposition.resid)
    return seasonal / (seasonal + residual)


@typechecked
def trend_strength(x: array_like, m: int_like) -> float_like:
    """
    !!! summary "Summary"

        The trend strength test is a statistical test for detecting the strength of the trend component in time series data. It measures the extent to which the trend component of a time series explains the variation in the data.

    ???+ info "Details"

        The trend strength test involves computing the trend strength index ($TSI$) using the following formula:

        $$
        TSI = \\frac{ Var(T) } { Var(T) + Var(R) }
        $$

        where:

        - $Var(T)$ is the variance of the trend component, and
        - $Var(R)$ is the variance of the residual component obtained after decomposing the time series data into its trend, seasonal, and residual components using a method such as seasonal decomposition of time series (STL) or moving average decomposition.

        ```
        TSI = Var(T) / (Var(T) + Var(R))
        ```

        The $TSI$ ranges between $0$ and $1$, with higher values indicating stronger trend in the data. The critical value for the $TSI$ can be obtained from statistical tables based on the sample size and level of significance. If the $TSI$ value exceeds the critical value, the null hypothesis of no trend is rejected in favor of the alternative hypothesis of trend.

        The trend strength test involves the following steps:

        1. Decompose the time series data into its trend, seasonal, and residual components using a method such as seasonal decomposition of time series (STL) or moving average decomposition.
        1. Compute the variance of the trend component, denoted by $Var(T)$.
        1. Compute the variance of the residual component, denoted by $Var(R)$.
        1. Compute the trend strength index ($TSI$) using the formula above.
        1. Compare the $TSI$ value to a critical value based on the sample size and level of significance. If the $TSI$ value exceeds the critical value, reject the null hypothesis of no trend in favor of the alternative hypothesis of trend.

        The trend strength test is a useful tool for identifying the strength of trend in time series data, and it can be used in conjunction with other tests and techniques for detecting trend. However, it assumes that the time series data is stationary and that the trend component is linear. Additionally, it may not be effective for time series data with short time spans or with nonlinear trends. Therefore, it should be used in conjunction with other tests and techniques for detecting trend in time series data.

    Params:
        x (array_like):
            The time series data set.
        m (int):
            The frequency of the time series data set.

    Returns:
        float:
            The trend strength score.

    !!! success "Credit"
        - Inspired by the `tsfeatures` library in both [`Python`](https://github.com/Nixtla/tsfeatures) and [`R`](http://pkg.robjhyndman.com/tsfeatures/).

    ???+ example "Examples"
        _description_
        ```python linenums="1"
        >>> _description_
        ```

    ??? question "References"
        - _description_

    ??? tip "See Also"
        - [`tsfeatures.stl_features`](https://github.com/Nixtla/tsfeatures/blob/main/tsfeatures/tsfeatures.py)
    """
    decomposition = seasonal_decompose(x=x, period=m, model="additive")
    trend = np.nanvar(decomposition.trend)
    residual = np.nanvar(decomposition.resid)
    return trend / (trend + residual)


@typechecked
def spikiness(x: array_like, m: int_like) -> float_like:
    """
    !!! summary "Summary"

        The spikiness test is a statistical test that measures the degree of spikiness or volatility in a time series data. It aims to detect the presence of spikes or sudden changes in the data that may indicate important events or anomalies in the underlying process.

    ???+ info "Details"

        The spikiness test is a statistical test for detecting the presence of spikes or sudden changes in a time series data. It measures the degree of spikiness or the extent to which the data is volatile.

        The spikiness test involves computing the spikiness index ($SI$) using the following formula:

        $$
        SI = \\frac {R} {MAD}
        $$

        where:

        - $R$ is the range of the data, and
        - $MAD$ is the mean absolute derivation of the data.

        ```
        SI = R / MAD
        ```

        The spikiness test involves the following steps:

        1. Compute the range of the data ($R$).
        1. Compute the mean absolute deviation of the data ($MAD$).
        1. Compute the spikiness index ($SI$) using the formula above.
        1. Compare the $SI$ value to a critical value based on the sample size and level of significance. If the SI value exceeds the critical value, reject the null hypothesis of no spikes in favor of the alternative hypothesis of spikes.

        The spikiness test can be used in conjunction with other tests and techniques for detecting spikes in time series data, such as change point analysis and outlier detection. However, it assumes that the time series data is stationary and that the spikes are abrupt and sudden. Additionally, it may not be effective for time series data with long-term trends or cyclical patterns. Therefore, it should be used in conjunction with other tests and techniques for detecting spikes in time series data.

    Params:
        x (array_like):
            The time series data set.
        m (int):
            The frequency of the time series data set.

    Returns:
        float:
            The spikiness score.

    !!! success "Credit"
        - All credit to the [`tsfeatures`](http://pkg.robjhyndman.com/tsfeatures/) library.

        This code is a direct copy+paste from the [`tsfeatures.py`](https://github.com/Nixtla/tsfeatures/blob/master/tsfeatures/tsfeatures.py) module.<br>
        It is not possible to refer directly to a `spikiness` function in the `tsfeatures` package because the process to calculate seasonal strength is embedded within their `stl_features` function. Therefore, it it necessary to copy it here.

    ???+ example "Examples"
        _description_
        ```python linenums="1"
        >>> _description_
        ```

    ??? question "References"
        - _description_

    ??? tip "See Also"
        - [`tsfeatures.stl_features`](https://github.com/Nixtla/tsfeatures/blob/main/tsfeatures/tsfeatures.py)
    """
    decomposition = seasonal_decompose(x=x, model="additive", period=m)
    madr = np.mean(np.abs(decomposition.resid))
    mads = np.mean(np.abs(decomposition.seasonal))
    return madr / mads
