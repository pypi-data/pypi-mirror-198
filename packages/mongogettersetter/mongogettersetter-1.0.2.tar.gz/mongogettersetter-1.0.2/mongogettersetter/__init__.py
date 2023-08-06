import sys
import json
sys.setrecursionlimit(64)

class MongoDictWrapper(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def prepare(self, _id, key, collection, filter_query):
        self.data = {}
        self.filter_query = filter_query
        self.collection = collection
        self.key = key[0]
        self.id = _id
        self._keys = key
        path = ".".join(self._keys)
        # print(f"__prepare__ you are at: {path}") 
        self.data['_id'] = _id
    
    def __getitem__(self, key):
        path = ".".join(self._keys)
        # print(f"__getitem__ you are at: {path}") 
        if isinstance(super().__getitem__(key), dict):
            dictwrapper = MongoDictWrapper(super().__getitem__(key))
            dictwrapper.prepare(self.data['_id'], self._keys+[key], self.collection, self.filter_query)
            return dictwrapper
        else:
            return super().__getitem__(key)

    def __setitem__(self, key, value):
        
        # Call the parent __setitem__ method to actually set the value in the dictionary
        path = ".".join(self._keys)
        # Execute your function here
        # # print(f"Dictionary updated: {path}.{key}={value}")
        update = {"$set": {"{}.{}".format(path, key): value}}
        result = self.collection.update_one(self.filter_query, update)
        nested_dict =  self.collection.find_one(self.filter_query)
        for k in self._keys:
            nested_dict = nested_dict[k]
        super().__setitem__(key, nested_dict[key])
    
    def __delitem__(self, key):
        super().__delitem__(key)
        path = ".".join(self._keys)
        self.collection.update_one(self.filter_query, {"$unset": {path + "." + key: ""}})
    
    def get(self, key, default=None):
       if key in self:
           return self[key]
       else:
           return default      

    def pop(self, key, default=None):
        value = super().pop(key, default)
        path = ".".join(self._keys)
        self.collection.update_one(self.filter_query, {"$unset": {path+"."+key: ""}})
        return value

    def update(self, other):
        super().update(other)
        d = dict(self)
        other.update(d)
        path = ".".join(self._keys)
        update = {"$set": {path: other}}
        self.collection.update_one(self.filter_query, update, upsert=True)
    
    def clear(self):
        # print("__clear__ ")
        path = ".".join(self._keys)
        update = {"$set": {path: {}}}
        self.collection.update_one(self.filter_query, update)
        super().clear()
        
class MongoDataWrapper:    
    def __init__(self, _id, key, collection, filter_query):
        self.filter_query = filter_query
        self.collection = collection
        self.key = key
        self.id = _id
    
    def get(self, key=None):
        if key is None:
            return self.collection.find_one(self.filter_query)[self.key]
        else:
            return self.collection.find_one(self.filter_query)[self.key][key]

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
        return json.dumps(self.collection.find_one(self.filter_query)[self.key], indent=4, default=str)
    
    def __repr__(self):
        return str(self.collection.find_one(self.filter_query)[self.key])
    
    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            data = self.get(key)
            # return data[key]
            if isinstance(data, dict):
                dictwrapper = MongoDictWrapper(data)
                dictwrapper.prepare(self.id, [self.key, key], self.collection, self.filter_query)
                return dictwrapper
            else:
                return data
            
    def __getitem__(self, key):
        data = self.get(key)
        # return data[key]
        if isinstance(data, dict):
            dictwrapper = MongoDictWrapper(data)
            dictwrapper.prepare(self.id, [self.key, key], self.collection, self.filter_query)
            return dictwrapper
        else:
            return data
    
    def __setattr__(self, key, value):
        if key in ['filter_query', 'collection', 'key', 'id']:
            self.__dict__[key] = value
        else:
            self.collection.update_one(self.filter_query, {"$set": {self.key+"."+key: value}})
            # # print("__setattr__", key, value)
    
    def __setitem__(self, index, value):
        update_query = {
            self.key + '.' + str(index): value
        }
        self.collection.update_one(
            self.filter_query,
            {'$set': update_query}
        )
        
    def __delitem__(self, key):
        self.collection.update_one(self.filter_query, {"$unset": {self.key + "." + key: ""}})
    
    def __delattr__(self, key):
        self.collection.update_one(self.filter_query, {"$unset": {self.key + "." + key: ""}})


class MongoGetterSetter(type):
    def __call__(cls, *args, **kwargs): 
        instance = super().__call__(*args, **kwargs)
        instance.__class__ = type('PyMongoGetterSetter', (cls,), {
            '__getattr__': cls.PyMongoGetterSetter.__getattr__,
            '__getitem__': cls.PyMongoGetterSetter.__getitem__,
            '__setattr__': cls.PyMongoGetterSetter.__setattr__,
            '__setitem__': cls.PyMongoGetterSetter.__setitem__,
            '__contains__': cls.PyMongoGetterSetter.__contains__,
            '__str__': cls.PyMongoGetterSetter.__str__,
            '__repr__': cls.PyMongoGetterSetter.__repr__,
            '__delattr__': cls.PyMongoGetterSetter.__delattr__,
            '__delitem__': cls.PyMongoGetterSetter.__delitem__,
        })
        return instance
    
    class PyMongoGetterSetter:
        def __getattr__(self, key):
            return MongoDataWrapper(self.id, key, self.collection, self.filter_query)
        
        def __getitem__(self, key):
            return MongoDataWrapper(self.id, key, self.collection, self.filter_query)

        def __setattr__(self, key, value):
            filter_query = self.filter_query
            self.collection.update_one(filter_query, {"$set": {key: value}})
            
        def __setitem__(self, key, value):
            filter_query = self.filter_query
            self.collection.update_one(filter_query, {"$set": {key: value}})
        
        def __contains__(self, key):
            return self.collection.find_one({key: {"$exists": True}})
        
        def __str__(self):
            filter_query = self.filter_query
            doc = self.collection.find_one(filter_query)
            return json.dumps(doc, indent=4, default=str)
        
        def __repr__(self):
            filter_query = self.filter_query
            return str(self.collection.find_one(filter_query))
        
        def __delattr__(self, name):
            # print(f"___delattr___ name = {name}")
            self.collection.update_one(self.filter_query, {"$unset": {name: ""}})
            
        def __delitem__(self, name):
            # print(f"___delattr___ name = {name}")
            self.collection.update_one(self.filter_query, {"$unset": {name: ""}})