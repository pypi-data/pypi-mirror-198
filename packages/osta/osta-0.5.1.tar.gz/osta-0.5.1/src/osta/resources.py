#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:14:00 2023

@author: tvborm
"""
import pkg_resources
import pandas as pd


def org_data():
    """
    Get organization data.

    Arguments:

    Details:
        Get organization data that osta package is utilizing as a resource.

    Examples:
        ```
        df = org_data()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "data_municipality.csv")
    df = pd.read_csv(path, index_col=0)
    return df


def account_data():
    """
    Get account data.

    Arguments:

    Details:
        Get account data that osta package is utilizing as a resource.

    Examples:
        ```
        df = account_data()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "data_account.csv")
    df = pd.read_csv(path, index_col=0)
    return df


def service_data():
    """
    Get service data.

    Arguments:

    Details:
        Get service data that osta package is utilizing as a resource.

    Examples:
        ```
        df = service_data()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "data_service.csv")
    df = pd.read_csv(path, index_col=0)
    return df


def financial_data():
    """
    Get financial data.

    Arguments:

    Details:
        Get financial code data (only key figures) that osta package is
        utilizing as a resource.

    Examples:
        ```
        df = financial_data()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "data_financial.csv")
    df = pd.read_csv(path, index_col=0)
    return df


def land_data():
    """
    Get land data.

    Arguments:

    Details:
        Get land data that osta package is utilizing as a resource.

    Examples:
        ```
        df = land_data()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "data_land.csv")
    df = pd.read_csv(path, index_col=0)
    return df


def field_data():
    """
    Get field data.

    Arguments:

    Details:
        Get field data that osta package is utilizing as a resource.

    Examples:
        ```
        df = field_data()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "fields_mandatory.csv")
    df = pd.read_csv(path, index_col=0)
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "fields_optional.csv")
    df2 = pd.read_csv(path, index_col=0)
    df = pd.concat([df, df2])
    return df


def field_pair_data():
    """
    Get field pair data.

    Arguments:

    Details:
        Get data on what fields are name-number pairs. Data is utilized by
        osta package.

    Examples:
        ```
        df = field_pair_data()
        ```

    Output:
        pandas.DataFrame.

    """
    path = pkg_resources.resource_filename(
        "osta", "resources/" + "fields_pairs.csv")
    df = pd.read_csv(path, index_col=0)
    return df
