
# Voltage Error
Volt_Error = {
    "track_total_hits": true,
    "min_score": 1,
    "query": {
        "bool": {
            "must": {
                "match": {
                    "status": "asserted"
                }
            },
            "should":
            {
                "match": {
                    "sensor": {
                        "query": "voltage",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 100
}

# temperature Error
Tempt_Error = {
    "track_total_hits": true,
    "min_score": 1,
    "query": {
        "bool": {
            "must": {
                "match": {
                    "status": "asserted"
                }
            },
            "should":
            {
                "match": {
                    "sensor": {
                        "query": "temperature",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 100
}

# fan Error
Fan_error = {
    "track_total_hits": True,
    "min_score": 1,
    "query": {
        "bool": {
            "must": {
                "match": {
                    "status": "asserted"
                }
            },
            "should":
            {
                "match": {
                    "sensor": {
                        "query": "fan",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 100
}

# BMC
BMC_Health_Error = {
    "track_total_hits": true,
    "min_score": 1,
    "query": {
        "bool": {
            "must": {
                "match": {
                    "status": "asserted"
                }
            },
            "should":
            {
                "match": {
                    "sensor": {
                        "query": "management",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 100
}

# Power supply Error
Power_supply_Error = {
    "track_total_hits": true,
    "min_score": 1,
    "query": {
        "bool": {
            "must": {
                "match": {
                    "status": "asserted"
                }
            },
            "should":
            {
                "match": {
                    "sensor": {
                        "query": "Power supply",
                        "boost": 10
                    }
                }
            }
        }
    },
    "size": 100
}
