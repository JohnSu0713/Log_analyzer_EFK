# PCIe Correctable Error
{
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
                        "message": "Correctable"
                    }
                }
            ],
            "should": {
                "match": {
                    "message": "bus"
                }
            }
        }
    },
    "size": 100
}
