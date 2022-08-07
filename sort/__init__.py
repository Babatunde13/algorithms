class Sort:
    def verify_sorted(self, data):
        if (len(data)) == 0 or len(data) == 1:
            return True
        return data[0] < data[1] and self.verify_sorted(data[1:])
