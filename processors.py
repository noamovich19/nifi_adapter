processors_data = {
    1: {
        "start_processors": [],
        "siblings": [2, 16],
    },
    2: {
        "start_processors": [11, 19],
        "siblings": [3, 18],
    },
    3: {
        "start_processors": [],
        "siblings": [4],
    },
    4: {
        "start_processors": [],
        "siblings": [5, 6, 7],
    },
    5: {
        "start_processors": [8],
        "siblings": [],
    },
    6: {
        "start_processors": [],
        "siblings": [],
    },
    7: {
        "start_processors": [],
        "siblings": [],
    },
    8: {
        "start_processors": [],
        "siblings": [9, 10],
    },
    9: {
        "start_processors": [],
        "siblings": [],
    },
    10: {
        "start_processors": [],
        "siblings": []
    },
    11: {
        "start_processors": [],
        "siblings": [13, 12],
    },

    12: {
        "start_processors": [],
        "siblings": [],
    },
    13: {
        "start_processors": [14],
        "siblings": [],
    },
    14: {
        "start_processors": [],
        "siblings": [15]
    },
    15: {
        "start_processors": [],
        "siblings": [],
    },
    16: {
        "start_processors": [],
        "siblings": [],
    },
    17: {
        "start_processors": [],
        "siblings": [],
    },
    18: {
        "start_processors": [],
        "siblings": [],
    },
    19: {
        "start_processors": [],
        "siblings": [13],
    }

}


class Processor(object):
    def __init__(self, processor_id):
        self.processor_id = processor_id

    @property
    def start_processors(self):
        return [
            Processor(start_processor_id)
            for start_processor_id in
            processors_data[self.processor_id]["start_processors"]
        ]

    @property
    def siblings(self):
        return [
            Processor(sibling_id)
            for sibling_id in
            processors_data[self.processor_id]["siblings"]
        ]

    @property
    def is_group(self):
        return len(self.start_processors) > 0

    @property
    def id(self):
        return self.processor_id

    def __str__(self):
        return str(self.id)


processors = [Processor(processor_id) for processor_id in processors_data]
