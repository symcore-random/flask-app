def lookup(collection_key_child, key_mother):
    collection_child, key_child = collection_key_child.split(':')

    mongo_lookup_syntax = {
        "$lookup": {
            "from": collection_child,  # foreign collection name
            "foreignField": key_child,  # foreign key name
            "localField": key_mother,  # local collection key name
            "as": key_mother,
        }
    }
    return mongo_lookup_syntax
