# %% Import libraries
import rosbag

# %% Get lists of topics and types from the bag
bag = rosbag.Bag('beta_autorally4_2018-03-29-15-34-10_split0.bag')
topics = bag.get_type_and_topic_info()[1].keys()
types = []
for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
    types.append(bag.get_type_and_topic_info()[1].values()[i][0])
# %% 
