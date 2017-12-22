class Movies():
    def __init__(self, name, franchise, boxArt_URL, youTubeTrailer_link):
        self.name = name
        self.boxArt_URL = boxArt_URL
        self.youTubeTrailer_link = youTubeTrailer_link
        print("" + self.name + " movie created")

    def printDetails(self):
        print("Movie name: " + self.name)
        print("Movie Box Art URL: " + self.boxArt_URL)
        print("Movie YouTube trailer link: " + self.youTubeTrailer_link)
