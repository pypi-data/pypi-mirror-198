import _pickle as cPickle


class ShyneData:
    def __init__(self):
        self.sprites = []

    def copy(self):
        sd = ShyneData()
        for sprite in self.sprites:
            sd.sprites.append(sprite.copy())

        return sd


def save_data(filename, data):
    print("Saving...")
    with open(filename, "wb") as f:
        cPickle.dump(data, f)


def load_data(filename):
    try:
        with open(filename, "rb") as f:
            data = cPickle.load(f)
    except:
        data = ShyneData()
    return data
