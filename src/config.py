DISCOUNT = 0.99
REPLAY_MEMORY_SIZE = 100_000  # How many last steps to keep for model training
MIN_REPLAY_MEMORY_SIZE = 50_000  # Minimum number of steps in a memory to start training
MINIBATCH_SIZE = 256  # How many steps (samples) to use for training
UPDATE_TARGET_EVERY = 5  # Terminal states (end of episodes)
MODEL_NAME = '20x10'
MIN_REWARD = -200  # For model save
MEMORY_FRACTION = 0.99

# Environment settings
EPISODES = 80_000

# Exploration settings

EPSILON_DECAY = 0.99975
MIN_EPSILON = 0.001

#  Stats settings
AGGREGATE_STATS_EVERY = 200  # episodes
SHOW_PREVIEW = True
