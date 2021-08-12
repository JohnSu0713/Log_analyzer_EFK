'''
curl --location --request GET 'http://localhost:9200/_search/' \
--header 'Content-Type: application/json' \
--data '{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "tag": "ex.sel.log"
                    }
                },
                {
                    "match": {
                        "message": "Lower"
                    }
                }
            ]
        }
    }
}'
'''
