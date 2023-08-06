class MongoMatchWrapper:
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
        return self.collection.aggregate([
            {"$match": self.filter_query},
            {
                "$project": {
                    "count": {
                        "$cond": {
                            "if": {"$isArray": "$"+self.key},
                            "then": {"$size": "$"+self.key},
                            "else": {"$strLenCP": "$"+self.key}
                        }
                    }
                }
            }
        ]).next()['count']
        
    def __str__(self):
        return str(self.collection.find_one(self.filter_query)[self.key])
    
    def __repr__(self):
        return str(self.collection.find_one(self.filter_query)[self.key])


class MongoGetterSetter(type):
    def __call__(cls, *args, **kwargs): 
        instance = super().__call__(*args, **kwargs)
        instance.__class__ = type('InstanceWithMetaclass', (cls,), {
            '__getattr__': cls.InstanceWithMetaclass.__getattr__,
            '__setattr__': cls.InstanceWithMetaclass.__setattr__,
            '__contains__': cls.InstanceWithMetaclass.__contains__,
            '__str__': cls.InstanceWithMetaclass.__str__,
        })
        return instance
    
    class InstanceWithMetaclass:
        def __getattr__(self, key):
            return MongoMatchWrapper(self._id, key, self.collection, self.filter_query)

        def __setattr__(self, key, value):
            filter_query = {"id": self._id}
            self.collection.update_one(filter_query, {"$set": {key: value}})
        
        def __contains__(self, key):
            return self.collection.find_one({key: {"$exists": True}})
        
        def __str__(self):
            filter_query = {"id": self._id}
            return str(self.collection.find_one(filter_query))