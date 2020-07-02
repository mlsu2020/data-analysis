# %% Import libraries
import rosbag
import numpy as np
import pandas as pd
import io
import inspect

# %% Get lists of topics and types from the bag
bag = rosbag.Bag('beta_autorally4_2018-03-29-15-34-10_split0.bag')
topics = bag.get_type_and_topic_info()[1].keys()

# %% Get topics as a list, and clean topic names to use for the csv files.
topics_list = list(topics)
topics_file = [n[1:].replace("/", "-") for n in topics_list]
topic_and_file = list(zip(topics_list, topics_file))

# %% Get the data for each topic
for topic, file_name in topic_and_file:
    # Analyze one of the timeseries data points to get the future DF columns
    _, msg, t = next(bag.read_messages(topics=[topic]))
    
    # The msg object contains a header object and other attributes. The msg object isn't
    # easily subscriptable with Python's basic methods, so I used inspection.
    attrs = [(k, v) for k, v in inspect.getmembers(msg) if not k.startswith('_') and not inspect.ismethod(v) and k != 'header']
    attrs.insert(0, ('seconds', t.to_sec()))

    # %% Create DataFrame
    column_names = [k for k, v in attrs]
    df = pd.DataFrame(columns=column_names)

    # Get all rows
    for _, msg, t in bag.read_messages(topics=[topic]):
        attrs = [(k, v) for k, v in inspect.getmembers(msg) if not k.startswith('_') and not inspect.ismethod(v) and k != 'header']
        attrs.insert(0, ('seconds', t.to_sec()))
        df.loc[len(df)] = [v for k, v in attrs]

    # Save data frame
    df.to_csv('csv/' + file_name + '.csv', index=False)

# %%
