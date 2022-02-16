def compute_stuff(df, date_filter=20161601, resolution="D",
                  resolution_value=30,
                  list_aggs=None):
    """
    Filter df by only taking history inferior to <date_filter> then generate aggregations each :
                                                                            <resolution_value> * <resolution>
    :param df: vaex dataframe
    :param date_filter: filter date, only take instances having a date inferior to this
    :param resolution: datetime frequency of aggregations
    :param resolution_value: number of units of <resolution> to take
    :param list_aggs: dictionary
    :return:
    """
    if list_aggs is None:
        list_aggs = []
    df_filtered = df[df.date <= date_filter]
    return df.groupby(['msno', vaex.BinnerTime(df['date_formatted'],
                                               resolution=resolution,
                                               every=resolution_value)]).agg(*list_aggs)
