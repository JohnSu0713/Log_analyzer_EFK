# PCIe Correctable Error
PCIe_correctable_error = {
    "track_total_hits": True,
    "min_score": 5,
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
                        "message": {
                            "query": "correctable",
                            "boost": 5
                        }
                    }
                }
            ],
            "should": {
                "match": {
                    "message": {
                        "query": "bus",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 20
}

# PCIe Uncorrectable Error
PCIe_uncorrectable_error = {
    "track_total_hits": True,
    "min_score": 5,
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
                        "message": {
                            "query": "correctable",
                            "boost": 5
                        }
                    }
                }
            ],
            "should": {
                "match": {
                    "message": {
                        "query": "bus",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 20
}
