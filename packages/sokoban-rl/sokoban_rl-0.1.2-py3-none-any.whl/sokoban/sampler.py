import random


class BaseSampler:

    """
    A sampler which has 'sample' method to sample episodes

    In order to work,
        - Set 'sample' method with *args and **kwargs as input and dictionary as output.
        - The output shall be a dictionary with prescribed keys and values as below.
            * nrow: int
            * ncol: int
            * player_position: int
            * box_position: list[int]
            * storage_position: list[int]
            * wall_position: list[int]
    
    See help(Sokoban.moving.SokobanMoving) to figure out what the numbers in the dictionary mean.
    """

    def sample(self, *args, **kwargs):
        raise NotImplementedError('A method sample must be designed')


class FixedWorldSampler(BaseSampler):
    
    """
    A sampler that always provides fixed episodes.

    Parameters
    ----------
    nrow : int
    ncol : int
    player_position : int
    box_position : list[int]
    storage_position : list[int]
    wall_position : list[int]

    See help(Sokoban.moving.SokobanMoving) to figure out what the numbers in all the parameters mean.
    """
    
    def __init__(self, nrow, ncol, player_position, box_position, storage_position, wall_position):
        self.nrow = nrow
        self.ncol = ncol
        self.player_position = player_position
        self.box_position = box_position
        self.storage_position = storage_position
        self.wall_position = wall_position
        return
    
    def sample(self, *args, **kwargs):
        result = {'nrow': self.nrow,
                  'ncol': self.ncol,
                  'player_position': self.player_position,
                  'box_position': self.box_position,
                  'storage_position': self.storage_position,
                  'wall_position': self.wall_position}
        return result


class RandomGeneratedSampler(BaseSampler):

    """
    A Sampler Which Generates Episode by Sampling Method.
        * WARNING : The parameter "extra_hint" will be deprecated.

    Description
        This sampler requires five parameters: p_straight, p_wall, n_range, n_boxes, extra_hint. And follow the procedure below to sample the episode.
            1. For one box, the total number of steps to walk (N) is sampled based on the discrete-uniform distribution covers "n_range".
            2. The box moves randomly through the gridworld for N times.
                * In the first step, the probability of up/down/left/right is the same as 0.25.
                * From the next step, the probability of going straight is p_straight, the probability of turning 90 degrees is (1 – p_straight),
                  and there is no probability of making a U-turn.
            3. The starting point of the box is the location of the player and the arrival point is the location of Storage,
               and the location of the box is randomly determined by one of the paths that have passed.
            4. If the box changes direction, secure free space for the player to move (extra_hint=True assures this work).
            5. The remaining space is randomly designated as the location of the wall with the probability of p_wall.
    
    Parameters
    ----------
    p_straight : float
    p_wall : float
    n_range : tuple(int)
    n_boxes : int
    extra_hint : bool
    """

    def __init__(self, p_straight=None, p_wall=None, n_range=None, n_boxes=None, extra_hint=True):
        self.p_straight = p_straight
        self.p_wall = p_wall
        self.n_range = n_range
        self.n_boxes = n_boxes
        self.extra_hint = extra_hint
        self.directions = {'up': ['down', (-1, 0)], 'down': ['up', (1, 0)],
                           'left': ['right', (0, -1)], 'right': ['left', (0, 1)]}
        return

    def sample(self, *args, **kwargs):
        # Exception for hyper-parameter
        assert self.n_boxes < self.n_range[0]

        # Sample all paths
        all_coords = []
        box_coords = []
        storage_coords = []
        while len(box_coords) < self.n_boxes:
            n = random.randint(*self.n_range)
            paths, extra = self.get_one_path(n)
            box_candidates = [path for path in paths[1:-1] if path not in box_coords and path != paths[0]]
            if len(box_candidates) > 0 and paths[-1] not in storage_coords:
                all_coords += paths + extra
                box_coords.append(random.sample(box_candidates, 1)[0])
                storage_coords.append(paths[-1])

        # Get a scaler for transforming coordinates into indexes
        row_min = min(all_coords, key=lambda x: x[0])[0]
        row_max = max(all_coords, key=lambda x: x[0])[0]
        col_min = min(all_coords, key=lambda x: x[1])[1]
        col_max = max(all_coords, key=lambda x: x[1])[1]
        nrow = abs(row_max - row_min) + 3
        ncol = abs(col_max - col_min) + 3
        adjuster = 1 - row_min, 1 - col_min

        # Transform coordinates into indexes
        all_position = [(pos[0] + adjuster[0]) * ncol + (pos[1] + adjuster[1]) for pos in all_coords]
        all_position = list(set(all_position))
        player_position = adjuster[0] * ncol + adjuster[1]
        box_position = [(pos[0] + adjuster[0]) * ncol + (pos[1] + adjuster[1]) for pos in box_coords]
        storage_position = [(pos[0] + adjuster[0]) * ncol + (pos[1] + adjuster[1]) for pos in storage_coords]

        # Sample wall_position
        wall_position = []
        for pos in range(nrow * ncol):
            if pos not in all_position:
                u = random.choices([0, 1], [1 - self.p_wall, self.p_wall])[0]
                if u == 1:
                    wall_position.append(pos)

        # Formatting
        result = {'nrow': nrow,
                  'ncol': ncol,
                  'player_position': player_position,
                  'box_position': box_position,
                  'storage_position': storage_position,
                  'wall_position': wall_position}
        return result

    def get_one_path(self, n):
        populations = list(self.directions)
        weights = [1 / len(populations)] * len(populations)
        paths = [[0, 0]]
        extra = []
        direction_before = None
        for _ in range(n):
            # Sample direction
            direction_new = random.choices(populations, weights)[0]
            direction_rev, (row, col) = self.directions[direction_new]

            # Adjust weights for next sampling
            weights = []
            for direction in populations:
                if direction_new == direction:
                    weights.append(self.p_straight)
                elif direction_rev == direction:
                    weights.append(0)
                else:
                    weights.append((1 - self.p_straight) / 2)

            # Calculate direction as coordinates and add it to paths
            row_before, col_before = paths[-1]
            paths.append([row_before + row, col_before + col])

            # Add extra spaces for player
            if direction_before is not None and direction_new != direction_before:
                _, (row, col) = self.directions[direction_rev]
                extra.append([row_before + row, col_before + col])
                if self.extra_hint:
                    direction_before_rev, (_, _) = self.directions[direction_before]
                    _, (row_extra, col_extra) = self.directions[direction_before_rev]
                    extra.append([row_before + row + row_extra, col_before + col + col_extra])
            direction_before = direction_new
        return paths, extra


class CurriculumSampler(RandomGeneratedSampler):

    """
    A Sampler that Samples Curriculum-Learning-Based Episodes

    Description
        For each 'sample' method call, 'n_total_steps' value is checked and mapped into an interval configured by
        pre-defined bins. Each time this interval changes, the 'sample' method sets sampling parameters differently.

    Parameters
    ----------
    bins : list[int]
        List of interval boundaries, which is for n_total_steps. DO NOT INCLUDE 0 and inf.
    labels : dict
        The keys shall consist of p_straight, p_wall, n_range, n_boxes, and extra_hint. And the values shall contain a
        list of parameter values for each interval corresponding to the bins.
    
    Examples
    --------
    Define bins and labels as follows:
    bins = [100000, 200000, 350000, 500000]
    labels = {'p_straight': [1.0, 0.1, 0.7, 0.7, 0.7],
              'p_wall': [0.5, 0.5, 0.5, 0.5, 0.5],
              'n_range': [(2, 4), (2, 3), (4, 7), (4, 7), (5, 10)],
              'n_boxes': [1, 1, 1, 2, 3],
              'extra_hint': [True, True, True, True, True]}
    Then:
        1. Step 0 ~ 99999 : p_straight=1.0, p_wall=0.5, n_range=(2, 4), n_boxes=1, extra_hint=True
        2. Step 100000 ~ 199999 : p_straight=0.1, p_wall=0.5, n_range=(2, 3), n_boxes=1, extra_hint=True
        3. Step 200000 ~ 349999 : p_straight=0.7, p_wall=0.5, n_range=(4, 7), n_boxes=1, extra_hint=True
        4. Step 350000 ~ 499999 : p_straight=0.7, p_wall=0.5, n_range=(4, 7), n_boxes=2, extra_hint=True
        5. Step 500000 ~ inf : p_straight=0.7, p_wall=0.5, n_range=(5, 10), n_boxes=3, extra_hint=True

    See Also
    --------
    See help(RandomGeneratedSampler) for detailed sampling method.
    See help(BinnedLinAnnPolicy) for implementing curriculum learning in policy.
    """

    def __init__(self, bins, labels):
        super(CurriculumSampler, self).__init__()
        self.bins = bins
        self.labels = labels
        return

    def sample(self, **kwargs):
        n = kwargs.get('n_total_steps')
        assert n is not None

        idx = sum([int(n >= bin_) for bin_ in self.bins])
        self.p_straight = self.labels['p_straight'][idx]
        self.p_wall = self.labels['p_wall'][idx]
        self.n_range = self.labels['n_range'][idx]
        self.n_boxes = self.labels['n_boxes'][idx]
        self.extra_hint = self.labels['extra_hint'][idx]

        result = super(CurriculumSampler, self).sample()
        return result
