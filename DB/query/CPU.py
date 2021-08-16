# QPI_Error
QPI_Error = {
    "track_total_hits": true,
    "min_score": 10,
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
                        "sensor": {
                            "query": "Processor"
                        }
                    }
                }
            ],
            "should":
            [
                {
                    "match": {
                        "message.keyword": {
                            "query": " ",
                            "boost": 10
                        }
                    }
                },
                {
                    "match": {
                        "sensor": {
                            "query": "QPI",
                            "boost": 10
                        }
                    }
                }
            ]
        }
    },
    "size": 1000
}

# QPI_Error
Other_CPU_Error = {
    "track_total_hits": True,
    # Using min_score to set the threshold.
    "min_score": 10,
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
                        "sensor": {
                            "query": "Processor"
                        }
                    }
                }
            ],
            "should": {
                "match": {
                    "message.keyword": {
                        "query": " ",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 1000
}

# IERR Error
IERR_Error = {
    "track_total_hits": True,
    # Using min_score to set the threshold.
    "min_score": 10,
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
                        "sensor": {
                            "query": "Processor"
                        }
                    }
                }
            ],
            "should": {
                "match": {
                    "message": {
                        "query": "IERR",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 1000
}
