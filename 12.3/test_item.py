class TestItem:
    k = {}

    def __setitem__(self, key, value):
        self.k[key] = value

    def __getitem__(self, key):
        print(key)
        return self.k[key]

a = TestItem()
a[123] = "haha"
print(a[123])