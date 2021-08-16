# Memory Correctable Error
Memory_correctable_error = {
    "track_total_hits": true,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "status": "asserted"
                    }
                },
                {
                    "match": {
                        {"message": "correctable",
                         "boost": 5
                         }
                    }
                }
            ],
            "should": {
                "match": {
                    "sensor": {
                        "query": "memory",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 100
}

Memory_uncorrectable_error = {
    "track_total_hits": true,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "status": "asserted"
                    }
                },
                {
                    "match": {
                        {"message": "uncorrectable",
                         "boost": 5
                         }
                    }
                }
            ],
            "should": {
                "match": {
                    "sensor": {
                        "query": "memory",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 100
}

