import sys

sys.setrecursionlimit(64)

class MongoDictWrapper(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def preapre(self, _id, key, collection, filter_query):
        self.data = {}
        self.data['filter_query'] = filter_query
        self.data['collection'] = collection
        self.data['keys'] = key
        path = ".".join(self.data['keys'])
        # print(f"__prepare__ you are at: {path}") 
        self.data['_id'] = _id
    
    def __getitem__(self, key):
        path = ".".join(self.data['keys'])
        # print(f"__getitem__ you are at: {path}") 
        if isinstance(super().__getitem__(key), dict):
            dictwrapper = MongoDictWrapper(super().__getitem__(key))
            dictwrapper.preapre(self.data['_id'], self.data['keys']+[key], self.data['collection'], self.data['filter_query'])
            return dictwrapper
        else:
            return super().__getitem__(key)

    def __setitem__(self, key, value):
        super().__getitem__(key, value)
        # Call the parent __setitem__ method to actually set the value in the dictionary
        path = ".".join(self.data['keys'])
        # Execute your function here
        # print(f"Dictionary updated: {path}.{key}={value}")
        update = {"$set": {"{}.{}".format(path, key): value}}
        self.data['collection'].update_one(self.data['filter_query'], update)
        
class MongoDataWrapper:    
    def __init__(self, _id, key, collection, filter_query):
        self.filter_query = filter_query
        self.collection = collection
        self.key = key
        self._id = _id
    
    def get(self):
        return self.collection.find_one(self.filter_query)[self.key]

    def inArray(self, value):
        return self.collection.find_one({self.key: {"$in": [value]}})
    
    def push(self, *values, maximum=-1):
        if maximum==-1:
            return self.collection.update_one(
                self.filter_query, {"$push": {self.key: {"$each": values}}}
            ).modified_count > 0
        else:
            update_operation = {
                "$push": {
                    self.key: {
                        "$each": values,
                        "$slice": -maximum
                    }
                }
            }
            
            return self.collection.update_one(
                self.filter_query, update_operation
            ).modified_count > 0
    
    def addToSet(self, value):
        return self.collection.update_one(self.filter_query, {"$addToSet": {self.key: value}}).modified_count > 0
    
    def pop(self, direction=1):
        return self.collection.update_one(self.filter_query, {"$pop": {self.key: direction}}).modified_count > 0
    
    def pull(self, value):
        return self.collection.update_one(self.filter_query, {"$pull": {self.key: value}}).modified_count > 0
    
    def pullAll(self, *values):
        return self.collection.update_one(self.filter_query, {"$pullAll": {self.key: values}}).modified_count > 0
    
    def size(self, value):
        return bool(self.collection.find_one({self.key: {"$size": value}}))
    
    def elemMatch(self, **kvalues):
        return bool(self.collection.find_one({self.key: {"$elemMatch": kvalues}}))
    
    def all(self, *values):
        return bool(self.collection.find_one({self.key: {"$all": values}}))
    
    def update(self, field, match, **kvalues):
        update_query = {self.key +".$."+ key: value for key, value in kvalues.items()}
        self.filter_query[self.key + "." + field] = match
        return self.collection.update_one(self.filter_query, {"$set": update_query}).modified_count > 0

    def __len__(self):
        return len(self.get())
        
    def __str__(self):
        return str(self.collection.find_one(self.filter_query)[self.key])
    
    def __repr__(self):
        return str(self.collection.find_one(self.filter_query)[self.key])
    
    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            data = self.get()
            # return data[key]
            if isinstance(data[key], dict):
                dictwrapper = MongoDictWrapper(data[key])
                dictwrapper.preapre(self._id, [self.key, key], self.collection, self.filter_query)
                return dictwrapper
            else:
                return data[key]
            
    def __getitem__(self, key):
        data = self.get()
        # return data[key]
        if isinstance(data[key], dict):
            dictwrapper = MongoDictWrapper(data[key])
            dictwrapper.preapre(self._id, [self.key, key], self.collection, self.filter_query)
            return dictwrapper
        else:
            return data[key]
    
    def __setattr__(self, key, value):
        if key in ['filter_query', 'collection', 'key', '_id']:
            self.__dict__[key] = value
        else:
            self.collection.update_one(self.filter_query, {"$set": {self.key+"."+key: value}})
            # print("__setattr__", key, value)
    
    def __setitem__(self, index, value):
        update_query = {
            self.key + '.' + str(index): value
        }
        self.collection.update_one(
            self.filter_query,
            {'$set': update_query}
        )


class MongoGetterSetter(type):
    def __call__(cls, *args, **kwargs): 
        instance = super().__call__(*args, **kwargs)
        instance.__class__ = type('PyMongoGetterSetter', (cls,), {
            '__getattr__': cls.PyMongoGetterSetter.__getattr__,
            '__setattr__': cls.PyMongoGetterSetter.__setattr__,
            '__contains__': cls.PyMongoGetterSetter.__contains__,
            '__str__': cls.PyMongoGetterSetter.__str__,
            '__repr__': cls.PyMongoGetterSetter.__repr__,
        })
        return instance
    
    class PyMongoGetterSetter:
        def __getattr__(self, key):
            return MongoDataWrapper(self._id, key, self.collection, self.filter_query)

        def __setattr__(self, key, value):
            filter_query = {"id": self._id}
            self.collection.update_one(filter_query, {"$set": {key: value}})
        
        def __contains__(self, key):
            return self.collection.find_one({key: {"$exists": True}})
        
        def __str__(self):
            filter_query = {"id": self._id}
            return str(self.collection.find_one(filter_query))
        
        def __repr__(self):
            filter_query = {"id": self._id}
            return str(self.collection.find_one(filter_query))